import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
    MONGO_DBNAME = os.getenv('MONGO_DBNAME', 'db_sante')
    SECRET_KEY = os.getenv('SECRET_KEY') or 'uneCleeTropTopSecrete'