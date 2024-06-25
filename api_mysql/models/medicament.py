from sqlalchemy import Column, String, DateTime, BigInteger
from app import db

class Medicament(db.Model):
    __tablename__ = 'medicament'
    id_medicament = Column(BigInteger, primary_key=True)
    nom_medicament = Column(String(50))
    ref_medicament = Column(String(100))
    molecule = Column(String(50))

    def to_dict(self):
        return {
            'id_medicament': self.id_medicament,
            'nom_medicament': self.nom_medicament,
            'ref_medicament': self.ref_medicament,
            'molecule': self.molecule
        }
