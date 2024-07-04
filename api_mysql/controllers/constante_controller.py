from models.constante import Constante
from app import db
from sqlalchemy import asc
import datetime

def get_all_constantes():
    return Constante.query.order_by(asc(Constante.date_releve)).all()

def get_constante_by_id(id_constante):
    return Constante.query.get(id_constante)

def create_constante(data):
    new_constante = Constante(**data)
    new_constante.date_releve = datetime.datetime.now(datetime.timezone.utc)
    db.session.add(new_constante)
    db.session.commit()
    return new_constante

def update_constante(id_constante, data):
    constante = Constante.query.get(id_constante)
    for key, value in data.items():
        setattr(constante, key, value)
    db.session.commit()
    return constante

def delete_constante(id_constante):
    constante = Constante.query.get(id_constante)
    db.session.delete(constante)
    db.session.commit()
    return constante
