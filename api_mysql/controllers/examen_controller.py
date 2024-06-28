from models.examen import Examen
from app import db

def get_all_examens():
    return Examen.query.all()

def get_examen_by_id(id_examens):
    return Examen.query.get(id_examens)

def get_examens_by_patient_id(id_patient):
    return Examen.query.filter_by(id_patient=id_patient).all()

def create_examen(data):
    new_examen = Examen(**data)
    db.session.add(new_examen)
    db.session.commit()
    return new_examen

def update_examen(id_examens, data):
    examen = Examen.query.get(id_examens)
    for key, value in data.items():
        setattr(examen, key, value)
    db.session.commit()
    return examen

def delete_examen(id_examens):
    examen = Examen.query.get(id_examens)
    db.session.delete(examen)
    db.session.commit()
    return examen
