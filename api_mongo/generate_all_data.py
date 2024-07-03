# generate_all_data.py

from faker import Faker
from pymongo import MongoClient
from datetime import datetime
from config import Config

fake = Faker()

client = MongoClient(Config.MONGO_URI)
db = client[Config.MONGO_DBNAME]
collection = db['patients']

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
            'num_contact': fake.phone_number(),
            'antecedants': fake.text(),
            'allergies': fake.text(),
            'adresse': fake.street_address(),
            'code_postal': fake.zipcode(),
            'ville': fake.city(),
            'etat': fake.state(),
            'pays': fake.country(),
            'num_telephone': fake.phone_number(),
            'email': fake.email()
        }
        patients.append(patient)
    return patients

patients_to_insert = generate_patients(num_records=10)

result = collection.insert_many(patients_to_insert)
print(f"Inserted {len(result.inserted_ids)} patients")

client.close()
