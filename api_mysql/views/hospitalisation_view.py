from flask import Blueprint, jsonify, request
from controllers.hospitalisation_controller import (
    get_all_hospitalisations, get_hospitalisation_by_id,
    create_hospitalisation, update_hospitalisation, delete_hospitalisation
)
from auth import token_required

hospitalisation_bp = Blueprint('hospitalisation', __name__)

@hospitalisation_bp.route('/hospitalisations', methods=['GET'])
@token_required
def get_hospitalisations():
    hospitalisations = get_all_hospitalisations()
    return jsonify([hospitalisation.to_dict() for hospitalisation in hospitalisations])

@hospitalisation_bp.route('/hospitalisations/<int:id_hospitalisation>', methods=['GET'])
@token_required
def get_hospitalisation(id_hospitalisation):
    hospitalisation = get_hospitalisation_by_id(id_hospitalisation)
    if hospitalisation is None:
        return jsonify({'error': 'Hospitalisation not found'}), 404
    return jsonify(hospitalisation.to_dict())

@hospitalisation_bp.route('/hospitalisations', methods=['POST'])
@token_required
def add_hospitalisation():
    data = request.get_json()
    new_hospitalisation = create_hospitalisation(data)
    return jsonify(new_hospitalisation.to_dict()), 201

@hospitalisation_bp.route('/hospitalisations/<int:id_hospitalisation>', methods=['PUT'])
@token_required
def edit_hospitalisation(id_hospitalisation):
    data = request.get_json()
    updated_hospitalisation = update_hospitalisation(id_hospitalisation, data)
    return jsonify(updated_hospitalisation.to_dict())

@hospitalisation_bp.route('/hospitalisations/<int:id_hospitalisation>', methods=['DELETE'])
@token_required
def remove_hospitalisation(id_hospitalisation):
    delete_hospitalisation(id_hospitalisation)
    return '', 204
