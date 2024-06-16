from sqlalchemy import Column, String, DateTime, BigInteger, Boolean
from sqlalchemy.orm import relationship
from app import db

class Soignant(db.Model):
    __tablename__ = 'soignant'
    id_medecin = Column(BigInteger, primary_key=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    mdp = Column(String(256), nullable=False)
    role = Column(String(100), nullable=False)
    date_creation = Column(DateTime, nullable=False)
    isActif = Column(Boolean, default=True)
    email = Column(String(100), nullable=False)
    num_telephone = Column(String(11), nullable=False)
    prescriptions = relationship("Prescription", backref="soignant")
    examens = relationship("Examen", backref="soignant")

    def to_dict(self):
        return {
            'id_medecin': self.id_medecin,
            'nom': self.nom,
            'prenom': self.prenom,
            'mdp': self.mdp,
            'role': self.role,
            'date_creation': self.date_creation.isoformat(),
            'isActif': self.isActif,
            'email': self.email,
            'num_telephone': self.num_telephone,
            'prescriptions': [prescription.to_dict() for prescription in self.prescriptions],
            'examens': [examen.to_dict() for examen in self.examens]
        }
