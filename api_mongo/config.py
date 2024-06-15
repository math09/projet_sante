import os

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
    MONGO_DBNAME = os.getenv('MONGO_DBNAME', 'db_sante')
