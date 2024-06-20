from models.medicament import Medicament
from app import db

def get_all_medicaments():
    return Medicament.query.all()

def get_medicament_by_id(id_medicament):
    return Medicament.query.get(id_medicament)

def create_medicament(data):
    new_medicament = Medicament(**data)
    db.session.add(new_medicament)
    db.session.commit()
    return new_medicament

def update_medicament(id_medicament, data):
    medicament = Medicament.query.get(id_medicament)
    for key, value in data.items():
        setattr(medicament, key, value)
    db.session.commit()
    return medicament

def delete_medicament(id_medicament):
    medicament = Medicament.query.get(id_medicament)
    db.session.delete(medicament)
    db.session.commit()
    return medicament