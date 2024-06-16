from sqlalchemy import Column, String, Text, DateTime, BigInteger, ForeignKey
from app import db

class Examen(db.Model):
    __tablename__ = 'examen'
    id_examens = Column(BigInteger, primary_key=True)
    motif = Column(String(100))
    observation = Column(Text)
    diagnostic = Column(Text)
    resultat_analyse = Column(Text)
    conclusion = Column(Text)
    date_examen = Column(DateTime, nullable=False)
    id_patient = Column(BigInteger, ForeignKey('patient.num_secu'))
    id_medecin = Column(BigInteger, ForeignKey('soignant.id_medecin'))

    def to_dict(self):
        return {
            'id_examens': self.id_examens,
            'motif': self.motif,
            'observation': self.observation,
            'diagnostic': self.diagnostic,
            'resultat_analyse': self.resultat_analyse,
            'conclusion': self.conclusion,
            'date_examen': self.date_examen.isoformat() if self.date_examen else None,
            'id_patient': self.id_patient,
            'id_medecin': self.id_medecin
        }
