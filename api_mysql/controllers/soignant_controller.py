from models.soignant import Soignant
from app import db
from werkzeug.security import check_password_hash

def get_all_soignants():
    return Soignant.query.all()

def get_soignant_by_id(id_medecin):
    return Soignant.query.get(id_medecin)

def create_soignant(data):
    new_soignant = Soignant(**data)
    db.session.add(new_soignant)
    db.session.commit()
    return new_soignant

def update_soignant(id_medecin, data):
    soignant = Soignant.query.get(id_medecin)
    for key, value in data.items():
        setattr(soignant, key, value)
    db.session.commit()
    return soignant

def delete_soignant(id_medecin):
    soignant = Soignant.query.get(id_medecin)
    db.session.delete(soignant)
    db.session.commit()
    return soignant

def verify_soignant(email, mdp):
    soignant = Soignant.query.filter_by(email=email).first()
    if soignant and check_password_hash(soignant.mdp, mdp):
        return soignant
    return None
