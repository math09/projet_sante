from sqlalchemy import Column, String, DateTime, BigInteger, ForeignKey
from app import db

class Prescription(db.Model):
    __tablename__ = 'prescription'
    id_prescription = Column(BigInteger, primary_key=True)
    date_creation = Column(DateTime, nullable=False)
    nom_medicament = Column(String(50))
    ref_medicament = Column(String(100))
    molecule = Column(String(50))
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)
    periodicite = Column(String(50))
    id_patient = Column(BigInteger, ForeignKey('patient.num_secu'))
    id_medecin = Column(BigInteger, ForeignKey('soignant.id_medecin'))

    def to_dict(self):
        return {
            'id_prescription': self.id_prescription,
            'date_creation': self.date_creation.isoformat(),
            'nom_medicament': self.nom_medicament,
            'ref_medicament': self.ref_medicament,
            'molecule': self.molecule,
            'date_debut': self.date_debut.isoformat(),
            'date_fin': self.date_fin.isoformat(),
            'periodicite': self.periodicite,
            'id_patient': self.id_patient,
            'id_medecin': self.id_medecin
        }
