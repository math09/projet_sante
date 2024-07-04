# generate_all_data.py

from faker import Faker
from pymongo import MongoClient
from datetime import datetime
from config import Config

fake = Faker()

client = MongoClient(Config.MONGO_URI)
db = client[Config.MONGO_DBNAME]
patient = db['patient']
admin = db['administration']

def generate_patients(num_records):
    patients = []
    for _ in range(num_records):
        patient = {
            'num_secu': fake.unique.random_int(min=100000000000000, max=999999999999999),
            'prenom': fake.first_name(),
            'nom': fake.last_name(),
            'date_creation': fake.date_time_between(start_date='-2y', end_date='now').isoformat(),
            'date_naissance': fake.date_of_birth(minimum_age=18, maximum_age=100).isoformat(),
            'age': fake.random_int(min=18, max=100),
            'lieu_de_naissance': fake.city(),
            'numero_de_mutuelle': fake.random_number(digits=9),
            'nom_mutuelle': fake.company(),
            'nom_contact': fake.last_name(),
            'prenom_contact': fake.first_name(),
            'num_contact': fake.random_number(digits=11, fix_len=True),
            'antecedants': fake.text(),
            'allergies': fake.text(),
            'adresse': fake.street_address(),
            'code_postal': fake.zipcode(),
            'ville': fake.city(),
            'etat': fake.state(),
            'pays': fake.country(),
            'num_telephone': fake.random_number(digits=11, fix_len=True),
            'email': fake.email()
        }
        patients.append(patient)
    return patients

def generate_administration(num_records):
    admins = []
    for _ in range(num_records):
        patient = {
            'prenom': fake.first_name(),
            'nom': fake.last_name(),
            'id_administratif': fake.random_number(digits=9, fix_len=True),
            'mdp': 'password',
            'role': fake.job(),
            'date_creation': fake.date_time_between(start_date='-2y', end_date='now').isoformat(),
            'isActif': fake.boolean(),
            'email': fake.email(),
            'num_telephone': fake.random_number(digits=11, fix_len=True),
        }
        admins.append(patient)
    return admins

patients_to_insert = generate_patients(num_records=10)
admin_to_insert = generate_administration(num_records=10)

result = patient.insert_many(patients_to_insert)
result = admin.insert_many(admin_to_insert)
print(f"Inserted {len(result.inserted_ids)} patient and admin")

client.close()
