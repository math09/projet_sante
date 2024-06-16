from models.prescription import Prescription
from app import db

def get_all_prescriptions():
    return Prescription.query.all()

def get_prescription_by_id(id_prescription):
    return Prescription.query.get(id_prescription)

def create_prescription(data):
    new_prescription = Prescription(**data)
    db.session.add(new_prescription)
    db.session.commit()
    return new_prescription

def update_prescription(id_prescription, data):
    prescription = Prescription.query.get(id_prescription)
    for key, value in data.items():
        setattr(prescription, key, value)
    db.session.commit()
    return prescription

def delete_prescription(id_prescription):
    prescription = Prescription.query.get(id_prescription)
    db.session.delete(prescription)
    db.session.commit()
    return prescription
