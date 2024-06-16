from sqlalchemy import Column, Integer, String, Text, DateTime, BigInteger
from sqlalchemy.orm import relationship
from app import db

class Patient(db.Model):
    __tablename__ = 'patient'
    num_secu = Column(BigInteger, primary_key=True)
    prenom = Column(String(100), nullable=False)
    nom = Column(String(100), nullable=False)
    date_creation = Column(DateTime, nullable=False)
    date_naissance = Column(DateTime, nullable=False)
    age = Column(Integer)
    lieu_de_naissance = Column(String(100))
    numero_de_mutuelle = Column(String(9))
    nom_mutuelle = Column(String(100))
    nom_contact = Column(String(100))
    prenom_contact = Column(String(100))
    num_contact = Column(String(10))
    antecedants = Column(Text)
    allergies = Column(Text)
    adresse = Column(String(100))
    code_postal = Column(String(5))
    ville = Column(String(100))
    etat = Column(String(100))
    pays = Column(String(100))
    num_telephone = Column(String(11))
    email = Column(String(255))
    examens = relationship("Examen", backref="patient")
    hospitalisations = relationship("Hospitalisation", backref="patient")
    constantes = relationship("Constante", backref="patient")
    prescriptions = relationship("Prescription", backref="patient")

    def to_dict(self):
        return {
            'num_secu': self.num_secu,
            'prenom': self.prenom,
            'nom': self.nom,
            'date_creation': self.date_creation.isoformat(),
            'date_naissance': self.date_naissance.isoformat(),
            'age': self.age,
            'lieu_de_naissance': self.lieu_de_naissance,
            'numero_de_mutuelle': self.numero_de_mutuelle,
            'nom_mutuelle': self.nom_mutuelle,
            'nom_contact': self.nom_contact,
            'prenom_contact': self.prenom_contact,
            'num_contact': self.num_contact,
            'antecedants': self.antecedants,
            'allergies': self.allergies,
            'adresse': self.adresse,
            'code_postal': self.code_postal,
            'ville': self.ville,
            'etat': self.etat,
            'pays': self.pays,
            'num_telephone': self.num_telephone,
            'email': self.email,
            'examens': [examen.to_dict() for examen in self.examens],
            'hospitalisations': [hospitalisation.to_dict() for hospitalisation in self.hospitalisations],
            'constantes': [constante.to_dict() for constante in self.constantes],
            'prescriptions': [prescription.to_dict() for prescription in self.prescriptions]
        }