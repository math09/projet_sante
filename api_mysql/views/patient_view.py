from flask import Blueprint, jsonify, request
from controllers.patient_controller import (
    get_all_patients, get_patient_by_id, get_patient_by_value,
    create_patient, update_patient, delete_patient
)
from auth import token_required

patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/patients', methods=['GET'])
@token_required
def get_patients():
    patients = get_all_patients()
    return jsonify([patient.to_dict() for patient in patients])

@patient_bp.route('/patients/<num_secu>', methods=['GET'])
@token_required
def get_patient(num_secu):
    patient = get_patient_by_id(num_secu)
    if patient is None:
        return jsonify({'error': 'Patient not found'}), 404
    return jsonify(patient.to_dict())

@patient_bp.route('/patients/search/<value>', methods=['GET'])
@token_required
def get_patient_value(value):
    patients = get_patient_by_value(value)
    result = [{
    'num_secu': patient.num_secu,
    'prenom': patient.prenom,
    'nom': patient.nom,
    'date_naissance': patient.date_naissance.isoformat()
    } for patient in patients]
    return jsonify(result)

@patient_bp.route('/patients', methods=['POST'])
@token_required
def add_patient():
    data = request.get_json()
    new_patient = create_patient(data)
    return jsonify(new_patient.to_dict()), 201

@patient_bp.route('/patients/<num_secu>', methods=['PUT'])
@token_required
def edit_patient(num_secu):
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Patient not found'}), 404
    updated_patient = update_patient(num_secu, data)
    return jsonify(updated_patient.to_dict())

@patient_bp.route('/patients/<num_secu>', methods=['DELETE'])
@token_required
def remove_patient(num_secu):
    delete_patient(num_secu)
    return 'patient successfully deleted', 204
