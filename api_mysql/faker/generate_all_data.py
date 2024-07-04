import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from faker import Faker
import random
import json

# Ajouter le répertoire parent et le répertoire models au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../models')))

from config import Config
from app import db
from models.soignant import Soignant
from models.examen import Examen
from models.patient import Patient
from models.constante import Constante
from models.hospitalisation import Hospitalisation
from models.medicament import Medicament
from models.prescription import Prescription

fake = Faker()

def generate_patients(session, num_records=10):
    patient_ids = []
    for _ in range(num_records):
        patient = Patient(
            num_secu=fake.unique.random_int(min=1000000000, max=9999999999),
            prenom=fake.first_name(),
            nom=fake.last_name(),
            date_creation=datetime.now(),
            date_naissance=fake.date_of_birth(minimum_age=0, maximum_age=100),
            age=fake.random_int(min=0, max=100),
            lieu_de_naissance=fake.city(),
            numero_de_mutuelle=fake.random_number(digits=9, fix_len=True),
            nom_mutuelle=fake.company(),
            nom_contact=fake.first_name(),
            prenom_contact=fake.last_name(),
            num_contact=fake.phone_number()[:10],
            antecedants=fake.text(),
            allergies=fake.text(),
            adresse=fake.address(),
            code_postal=fake.postcode()[:5],
            ville=fake.city(),
            etat=fake.state(),
            pays=fake.country(),
            num_telephone=fake.phone_number()[:11],
            email=fake.email()
        )
        session.add(patient)
        session.commit()  # Commit après chaque insertion pour récupérer les IDs
        patient_ids.append(patient.num_secu)
    return patient_ids

def generate_soignants(session, num_records=10):
    for _ in range(num_records):
        soignant = Soignant(
            nom=fake.last_name(),
            prenom=fake.first_name(),
            mdp="password",
            role=fake.job(),
            date_creation=datetime.now(),
            isActif=fake.boolean(),
            email=fake.email(),
            num_telephone=fake.phone_number()[:11]
        )
        session.add(soignant)
    session.commit()

def generate_examens(session, patient_ids, num_records=10):
    soignants = session.query(Soignant).all()
    for _ in range(num_records):
        examen = Examen(
            motif=fake.sentence(),
            observation=fake.text(),
            diagnostic=fake.text(),
            resultat_analyse=fake.text(),
            conclusion=fake.text(),
            date_examen=datetime.now(),
            id_patient=fake.random_element(elements=patient_ids),
            id_medecin=fake.random_element(elements=[soignant.id_medecin for soignant in soignants])
        )
        session.add(examen)
    session.commit()

def generate_constantes(session, patient_ids, num_records=10):
    for _ in range(num_records*10):
        constante = Constante(
            frequence_cardiaque=fake.random_int(min=60, max=100),  # battements par minute
            tension=fake.pyfloat(left_digits=2, right_digits=1, positive=True, min_value=10.0, max_value=20.0),  # tension artérielle
            temperature=fake.pyfloat(left_digits=2, right_digits=1, positive=True, min_value=36.0, max_value=40.0),  # degrés Celsius
            groupe_sanguin=fake.random_element(elements=('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')),
            poids=fake.pyfloat(left_digits=3, right_digits=1, positive=True, min_value=40.0, max_value=120.0),  # kg
            taille=fake.pyfloat(left_digits=2, right_digits=2, positive=True, min_value=1.5, max_value=2.0),  # m
            imc=fake.pyfloat(left_digits=3, right_digits=1, positive=True, min_value=15.0, max_value=35.0),  # kg/m^2
            date_releve=datetime.now(),
            id_patient=fake.random_element(elements=patient_ids)
        )
        session.add(constante)
    session.commit()

def generate_hospitalisations(session, patient_ids, num_records=10):
    for _ in range(num_records):
        hospitalisation = Hospitalisation(
            date_debut=fake.past_datetime(),
            date_fin=fake.future_datetime(end_date='+30d'),
            motif=fake.text(),
            id_patient=fake.random_element(elements=patient_ids)
        )
        session.add(hospitalisation)
    session.commit()

def generate_medicaments(session, num_records=10):
    for _ in range(num_records):
        medicament = Medicament(
            nom_medicament=fake.word(),
            ref_medicament=fake.unique.random_int(min=1000, max=9999),
            molecule=fake.word()
        )
        session.add(medicament)
    session.commit()

def generate_prescriptions(session, patient_ids, soignant_ids, medicament_ids, num_records=10):
    for _ in range(num_records):
        prescription = Prescription(
            date_creation=datetime.now(),
            champs_libre=fake.text(),
            traitement=json.dumps({
                'id_medicament': fake.random_element(elements=medicament_ids),
                'dosage': fake.random_int(min=1, max=3),
                'frequence': fake.random_element(elements=('Matin', 'Midi', 'Soir')),
                'duree': fake.random_int(min=5, max=30)
            }),
            id_patient=fake.random_element(elements=patient_ids),
            id_medecin=fake.random_element(elements=soignant_ids),
            signature=fake.sha256()
        )
        session.add(prescription)
    session.commit()

def main():
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    Session = sessionmaker(bind=engine)
    session = Session()

    patient_ids = generate_patients(session, num_records=10)
    generate_soignants(session, num_records=10)
    generate_examens(session, patient_ids, num_records=10)
    generate_constantes(session, patient_ids, num_records=10)
    generate_hospitalisations(session, patient_ids, num_records=5)
    generate_medicaments(session, num_records=10)

    patients = session.query(Patient).all()
    soignants = session.query(Soignant).all()
    medicaments = session.query(Medicament).all()

    patient_ids = [patient.num_secu for patient in patients]
    soignant_ids = [soignant.id_medecin for soignant in soignants]
    medicament_ids = [medicament.id_medicament for medicament in medicaments]

    generate_prescriptions(session, patient_ids, soignant_ids, medicament_ids, num_records=10)

    session.close()

if __name__ == "__main__":
    main()
