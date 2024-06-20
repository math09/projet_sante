from sqlalchemy import Column, String, DateTime, BigInteger, ForeignKey, Text
from app import db

class Prescription(db.Model):
    __tablename__ = 'prescription'
    id_prescription = Column(BigInteger, primary_key=True)
    date_creation = Column(DateTime, nullable=False)
    champs_libre = Column(Text)
    id_patient = Column(BigInteger, ForeignKey('patient.num_secu'))
    id_medecin = Column(BigInteger, ForeignKey('soignant.id_medecin'))
    signature = Column(String, nullable=False)

    def to_dict(self):
        return {
            'id_prescription': self.id_prescription,
            'date_creation': self.date_creation.isoformat(),
            'champs_libre': self.champs_libre,
            'id_patient': self.id_patient,
            'id_medecin': self.id_medecin,
            'signature': self.signature
        }
