from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from config import Config
from bson.objectid import ObjectId
import re
from auth import token_required

patient_bp = Blueprint('patient', __name__)

client = MongoClient(Config.MONGO_URI)
db = client[Config.MONGO_DBNAME]


#get all patient
@patient_bp.route('/patients', methods=['GET'])
@token_required
def get_patients():
    patients = db.patient.find()
    result = []
    for patient in patients:
        patient['_id'] = str(patient['_id'])
        result.append(patient)
    return jsonify(result), 200

# get one patient by id
@patient_bp.route('/patients/<id>', methods=['GET'])
@token_required
def get_patients_by_id(id):
    patient = db.patient.find_one({'_id': ObjectId(id)})
    if patient:
        patient['_id'] = str(patient['_id'])
        return jsonify(patient), 200
    else:
        return jsonify({'error': 'Patient not found'}), 404

# get one patient by value
@patient_bp.route('/patients/search/<value>', methods=['GET'])
@token_required
def search_patient(value):
    try:
        numeric_value = int(value)
    except ValueError:
        numeric_value = None
    
    query = {
        "$or": [
            {"nom": re.compile(value, re.IGNORECASE)},
            {"prenom": re.compile(value, re.IGNORECASE)},
            {"date_naissance": re.compile(value, re.IGNORECASE)},
            {"age": numeric_value if numeric_value is not None else None},
            {"num_secu": re.compile(value, re.IGNORECASE)},
            {"lieu_de_naissance": re.compile(value, re.IGNORECASE)},
            {"numéro_de_mutuelle": re.compile(value, re.IGNORECASE)},
            {"nom_mutuelle": re.compile(value, re.IGNORECASE)},
            {"nom_contact": re.compile(value, re.IGNORECASE)},
            {"prenom_contact": re.compile(value, re.IGNORECASE)},
            {"num_contact": re.compile(value, re.IGNORECASE)},
            {"antecedants": re.compile(value, re.IGNORECASE)},
            {"allergies": re.compile(value, re.IGNORECASE)},
            {"adresse": re.compile(value, re.IGNORECASE)},
            {"code_postal": re.compile(value, re.IGNORECASE)},
            {"ville": re.compile(value, re.IGNORECASE)},
            {"etat": re.compile(value, re.IGNORECASE)},
            {"pays": re.compile(value, re.IGNORECASE)},
            {"num_telephone": re.compile(value, re.IGNORECASE)},
            {"email": re.compile(value, re.IGNORECASE)}
        ]
    }
    query["$or"] = [q for q in query["$or"] if q[list(q.keys())[0]] is not None]

    results = db.patient.find(query)
    patients = []
    for patient in results:
        patient['_id'] = str(patient['_id'])
        patients.append(patient)

    return jsonify(patients), 200
    
# add patients
@patient_bp.route('/patients', methods=['POST'])
@token_required
def add_patient():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    result = db.patient.insert_one(data)
    
    inserted_patient = db.patient.find_one({'_id': result.inserted_id})

    inserted_patient['_id'] = str(inserted_patient['_id'])

    return jsonify(inserted_patient), 201


# update patients
@patient_bp.route('/patients/<id>', methods=['PUT'])
@token_required
def update_patient(id):
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    result = db.patient.update_one({'_id': ObjectId(id)}, {'$set': data})

    if result.matched_count == 0:
        return jsonify({'error': 'Patient not found'}), 404

    updated_patient = db.patient.find_one({'_id': ObjectId(id)})
    updated_patient['_id'] = str(updated_patient['_id'])

    return jsonify(updated_patient), 200


# delete patients
@patient_bp.route('/patients/<id>', methods=['DELETE'])
@token_required
def delete_patient(id):
    result = db.patient.delete_one({'_id': ObjectId(id)})

    if result.deleted_count == 0:
        return jsonify({'error': 'Patient not found'}), 404

    return jsonify({'message': 'Patient deleted successfully'}), 200