from models.patient import Patient
from app import db

def get_all_patients():
    return Patient.query.all()

def get_patient_by_id(num_secu):
    return Patient.query.get(num_secu)

def get_patient_by_value(value):
    return Patient.query.filter((Patient.num_secu == value) | (Patient.nom == value) | (Patient.prenom == value)).all()

def create_patient(data):
    new_patient = Patient(**data)
    db.session.add(new_patient)
    db.session.commit()
    return new_patient

def update_patient(num_secu, data):
    patient = Patient.query.get(num_secu)
    for key, value in data.items():
        setattr(patient, key, value)
    db.session.commit()
    return patient

def delete_patient(num_secu):
    patient = Patient.query.get(num_secu)
    db.session.delete(patient)
    db.session.commit()
    return patient