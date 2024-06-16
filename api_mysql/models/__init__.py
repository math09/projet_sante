from app import db
from .patient import Patient
from .soignant import Soignant
from .examen import Examen
from .hospitalisation import Hospitalisation
from .constante import Constante
from .prescription import Prescription

def initialize_database():
    db.create_all()
