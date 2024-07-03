from werkzeug.security import generate_password_hash
from app import db
from datetime import datetime
from .patient import Patient
from .soignant import Soignant
from .examen import Examen
from .hospitalisation import Hospitalisation
from .constante import Constante
from .prescription import Prescription
from .medicament import Medicament

def initialize_database():
    db.create_all()
    create_admin_user()

def create_admin_user():
    admin_email = 'admin@gmail.com'
    admin_password = generate_password_hash('admin')

    admin = Soignant.query.filter_by(email=admin_email).first()
    if not admin:
        new_admin = Soignant(
            nom='Admin',
            prenom='Admin',
            mdp=admin_password,
            role='admin',
            date_creation=datetime.now(),
            isActif=True,
            email=admin_email,
            num_telephone='0636656565'
        )
        db.session.add(new_admin)
        db.session.commit()