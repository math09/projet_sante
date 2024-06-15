from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from config import Config
from bson.objectid import ObjectId

patient_bp = Blueprint('patient', __name__)

client = MongoClient(Config.MONGO_URI)
db = client[Config.MONGO_DBNAME]


#get all patient
@patient_bp.route('/patients', methods=['GET'])
def get_patients():
    patients = db.patient.find()
    result = []
    for patient in patients:
        patient['_id'] = str(patient['_id'])
        result.append(patient)
    return jsonify(result), 200

# get one patient
@patient_bp.route('/patients/<id>', methods=['GET'])
def get_patients_by_id(id):
    patient = db.patient.find_one({'_id': ObjectId(id)})
    if patient:
        patient['_id'] = str(patient['_id'])
        return jsonify(patient), 200
    else:
        return jsonify({'error': 'Patient not found'}), 404
    
# add patients
@patient_bp.route('/patients', methods=['POST'])
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
def delete_patient(id):
    result = db.patient.delete_one({'_id': ObjectId(id)})

    if result.deleted_count == 0:
        return jsonify({'error': 'Patient not found'}), 404

    return jsonify({'message': 'Patient deleted successfully'}), 200