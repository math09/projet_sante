from flask import Blueprint, jsonify, request
from controllers.prescription_controller import (
    get_all_prescriptions, get_prescription_by_id,
    create_prescription, update_prescription, delete_prescription
)

prescription_bp = Blueprint('prescription', __name__)

@prescription_bp.route('/prescriptions', methods=['GET'])
def get_prescriptions():
    prescriptions = get_all_prescriptions()
    return jsonify([prescription.to_dict() for prescription in prescriptions])

@prescription_bp.route('/prescriptions/<int:id_prescription>', methods=['GET'])
def get_prescription(id_prescription):
    prescription = get_prescription_by_id(id_prescription)
    if prescription is None:
        return jsonify({'error': 'Prescription not found'}), 404
    return jsonify(prescription.to_dict())

@prescription_bp.route('/prescriptions', methods=['POST'])
def add_prescription():
    data = request.get_json()
    new_prescription = create_prescription(data)
    return jsonify(new_prescription.to_dict()), 201

@prescription_bp.route('/prescriptions/<int:id_prescription>', methods=['PUT'])
def edit_prescription(id_prescription):
    data = request.get_json()
    updated_prescription = update_prescription(id_prescription, data)
    return jsonify(updated_prescription.to_dict())

@prescription_bp.route('/prescriptions/<int:id_prescription>', methods=['DELETE'])
def remove_prescription(id_prescription):
    delete_prescription(id_prescription)
    return '', 204
