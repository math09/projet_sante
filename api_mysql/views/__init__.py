from .patient_view import patient_bp
from .soignant_view import soignant_bp
from .examen_view import examen_bp
from .hospitalisation_view import hospitalisation_bp
from .prescription_view import prescription_bp
from .constante_view import constante_bp
from .medicament_view import medicament_bp

def register_routes(app):
    app.register_blueprint(patient_bp)
    app.register_blueprint(soignant_bp)
    app.register_blueprint(examen_bp)
    app.register_blueprint(hospitalisation_bp)
    app.register_blueprint(prescription_bp)
    app.register_blueprint(constante_bp)
    app.register_blueprint(medicament_bp)
