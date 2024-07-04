import time
import pymongo
import mysql.connector
from datetime import datetime, timedelta

# Configuration MongoDB
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["db_sante"]
mongo_collection = mongo_db["patient"]

# Configuration MySQL
mysql_config = {
    'user': 'root',
    'password': 'rootpassword',
    'host': 'localhost',
    'database': 'projet_sante'
}

def fetch_patients_from_mongo():
    # Récupère tous les patients de MongoDB
    patients = mongo_collection.find()
    return patients

def fetch_existing_patients_from_mysql(cursor):
    # Récupère les dates de création et de modification des patients déjà présents dans MySQL
    query = "SELECT num_secu, date_creation, date_modification FROM patient"
    cursor.execute(query)
    existing_patients = cursor.fetchall()
    return {patient[0]: {'date_creation': patient[1], 'date_modification': patient[2]} for patient in existing_patients}

def insert_or_update_patient_in_mysql(cursor, patient):
    # Insère ou met à jour un patient dans MySQL
    query = """
        INSERT INTO patient (num_secu, prenom, nom, date_creation, date_modification, date_naissance, lieu_de_naissance, numero_de_mutuelle, nom_mutuelle, nom_contact, prenom_contact, num_contact, adresse, code_postal, ville, etat, pays, num_telephone, email)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        num_secu = VALUES(num_secu),
        prenom = VALUES(prenom),
        nom = VALUES(nom),
        date_creation = VALUES(date_creation),
        date_modification = VALUES(date_modification),
        date_naissance = VALUES(date_naissance),
        lieu_de_naissance = VALUES(lieu_de_naissance),
        numero_de_mutuelle = VALUES(numero_de_mutuelle),
        nom_mutuelle = VALUES(nom_mutuelle),
        nom_contact = VALUES(nom_contact),
        prenom_contact = VALUES(prenom_contact),
        num_contact = VALUES(num_contact),
        adresse = VALUES(adresse),
        code_postal = VALUES(code_postal),
        ville = VALUES(ville),
        etat = VALUES(etat),
        pays = VALUES(pays),
        num_telephone = VALUES(num_telephone),
        email = VALUES(email)  
    """
    
    if(patient.get("date_modification") is not None):
        patient["date_modification"] = patient["date_modification"].strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute(query, (
        patient.get("num_secu"),
        patient.get("prenom"),
        patient.get("nom"),
        patient.get("date_creation") or None,
        patient.get("date_modification") or None,
        patient.get("date_naissance") or None,
        patient.get("lieu_de_naissance") or None,
        patient.get("numero_de_mutuelle") or None,
        patient.get("nom_mutuelle")  or None,
        patient.get("nom_contact") or None,
        patient.get("prenom_contact") or None,
        patient.get("num_contact") or None,
        patient.get("adresse") or None,
        patient.get("code_postal") or None,
        patient.get("ville") or None,
        patient.get("etat") or None,
        patient.get("pays") or None,
        patient.get("num_telephone") or None,
        patient.get("email") or None
    ))

def main():
    while True:
        try:
            # Connexion à MySQL
            mysql_connection = mysql.connector.connect(**mysql_config)
            mysql_cursor = mysql_connection.cursor()

            # Récupère les patients de MongoDB
            patients = fetch_patients_from_mongo()
            # Récupère les patients existants dans MySQL
            existing_patients = fetch_existing_patients_from_mysql(mysql_cursor)

            for patient in patients:
                patient_id = str(patient["num_secu"])
                if patient_id not in existing_patients or \
                    patient["date_modification"] > existing_patients[patient_id]["date_modification"]:
                    insert_or_update_patient_in_mysql(mysql_cursor, patient)

            # Commit les changements
            mysql_connection.commit()

        except Exception as e:
            print(f"Une erreur s'est produite: {e}")

        finally:
            mysql_cursor.close()
            mysql_connection.close()

        # Attendre 5 minutes avant de recommencer
        time.sleep(60)

if __name__ == "__main__":
    main()