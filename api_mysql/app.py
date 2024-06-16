from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from models import initialize_database
        initialize_database()

        from views import register_routes
        register_routes(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
