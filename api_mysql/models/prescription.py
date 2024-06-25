from sqlalchemy import Column, String, DateTime, BigInteger, ForeignKey, Text, JSON
from app import db

class Prescription(db.Model):
    __tablename__ = 'prescription'
    id_prescription = Column(BigInteger, primary_key=True)
    date_creation = Column(DateTime, nullable=False)
    champs_libre = Column(Text)
    traitement = Column(JSON)
    id_patient = Column(BigInteger, ForeignKey('patient.num_secu'))
    id_medecin = Column(BigInteger, ForeignKey('soignant.id_medecin'))
    signature = Column(String(256), nullable=False)

    def to_dict(self):
        return {
            'id_prescription': self.id_prescription,
            'date_creation': self.date_creation.isoformat(),
            'champs_libre': self.champs_libre,
            'traitement' : self.traitement,
            'id_patient': self.id_patient,
            'id_medecin': self.id_medecin,
            'signature': self.signature
        }
