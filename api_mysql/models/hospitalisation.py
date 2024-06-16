from sqlalchemy import Column, Text, DateTime, BigInteger, ForeignKey
from app import db

class Hospitalisation(db.Model):
    __tablename__ = 'hospitalisation'
    id_hospitalisation = Column(BigInteger, primary_key=True)
    date_debut = Column(DateTime, nullable=False)
    date_fin = Column(DateTime)
    motif = Column(Text)
    id_patient = Column(BigInteger, ForeignKey('patient.num_secu'), nullable=False)

    def to_dict(self):
        return {
            'id_hospitalisation': self.id_hospitalisation,
            'date_debut': self.date_debut.isoformat() if self.date_debut else None,
            'date_fin': self.date_fin.isoformat() if self.date_fin else None,
            'motif': self.motif,
            'id_patient': self.id_patient
        }
