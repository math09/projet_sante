from sqlalchemy import Column, String, Float, DateTime, BigInteger, ForeignKey
from app import db

class Constante(db.Model):
    __tablename__ = 'constante'
    id_constante = Column(BigInteger, primary_key=True)
    frequence_cardiaque = Column(Float)
    tension = Column(Float)
    temperature = Column(Float)
    groupe_sanguin = Column(String(3))
    poids = Column(Float)
    taille = Column(Float)
    imc = Column(Float)
    date_releve = Column(DateTime, nullable=False)
    id_patient = Column(BigInteger, ForeignKey('patient.num_secu'))

    def to_dict(self):
        return {
            'id_constante': self.id_constante,
            'frequence_cardiaque': self.frequence_cardiaque,
            'tension': self.tension,
            'temperature': self.temperature,
            'groupe_sanguin': self.groupe_sanguin,
            'poids': self.poids,
            'taille': self.taille,
            'imc': self.imc,
            'date_releve': self.date_releve.isoformat(),
            'id_patient': self.id_patient
        }
