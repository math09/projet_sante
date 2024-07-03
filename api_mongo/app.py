from flask import Flask
from flask_cors import CORS
import jwt
from config import Config


from patient import patient_bp
from administration import administration_bp

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

app.register_blueprint(patient_bp)
app.register_blueprint(administration_bp)

if __name__ == '__main__':
    app.run()
