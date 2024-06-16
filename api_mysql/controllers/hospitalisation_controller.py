from models.hospitalisation import Hospitalisation
from app import db

def get_all_hospitalisations():
    return Hospitalisation.query.all()

def get_hospitalisation_by_id(id_hospitalisation):
    return Hospitalisation.query.get(id_hospitalisation)

def create_hospitalisation(data):
    new_hospitalisation = Hospitalisation(**data)
    db.session.add(new_hospitalisation)
    db.session.commit()
    return new_hospitalisation

def update_hospitalisation(id_hospitalisation, data):
    hospitalisation = Hospitalisation.query.get(id_hospitalisation)
    for key, value in data.items():
        setattr(hospitalisation, key, value)
    db.session.commit()
    return hospitalisation

def delete_hospitalisation(id_hospitalisation):
    hospitalisation = Hospitalisation.query.get(id_hospitalisation)
    db.session.delete(hospitalisation)
    db.session.commit()
    return hospitalisation
