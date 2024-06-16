from flask import Blueprint, jsonify, request
from controllers.soignant_controller import (
    get_all_soignants, get_soignant_by_id,
    create_soignant, update_soignant, delete_soignant
)

soignant_bp = Blueprint('soignant', __name__)

@soignant_bp.route('/soignants', methods=['GET'])
def get_soignants():
    soignants = get_all_soignants()
    return jsonify([soignant.to_dict() for soignant in soignants])

@soignant_bp.route('/soignants/<int:id_medecin>', methods=['GET'])
def get_soignant(id_medecin):
    soignant = get_soignant_by_id(id_medecin)
    if soignant is None:
        return jsonify({'error': 'Soignant not found'}), 404
    return jsonify(soignant.to_dict())

@soignant_bp.route('/soignants', methods=['POST'])
def add_soignant():
    data = request.get_json()
    new_soignant = create_soignant(data)
    return jsonify(new_soignant.to_dict()), 201

@soignant_bp.route('/soignants/<int:id_medecin>', methods=['PUT'])
def edit_soignant(id_medecin):
    data = request.get_json()
    updated_soignant = update_soignant(id_medecin, data)
    return jsonify(updated_soignant.to_dict())

@soignant_bp.route('/soignants/<int:id_medecin>', methods=['DELETE'])
def remove_soignant(id_medecin):
    delete_soignant(id_medecin)
    return '', 204
