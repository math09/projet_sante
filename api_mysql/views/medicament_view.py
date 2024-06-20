from flask import Blueprint, jsonify, request
from controllers.medicament_controller import (
get_all_medicaments, get_medicament_by_id,
create_medicament, update_medicament, delete_medicament
)

medicament_bp = Blueprint('medicament', __name__)

@medicament_bp.route('/medicaments', methods=['GET'])
def get_medicaments():
    medicaments = get_all_medicaments()
    return jsonify([medicament.to_dict() for medicament in medicaments])

@medicament_bp.route('/medicaments/<int:id_medicament>', methods=['GET'])
def get_medicament(id_medicament):
    medicament = get_medicament_by_id(id_medicament)
    if medicament is None:
        return jsonify({'error': 'Hospitalisation not found'}), 404
    return jsonify(medicament.to_dict())

@medicament_bp.route('/medicaments', methods=['POST'])
def add_medicament():
    data = request.get_json()
    new_medicament = create_medicament(data)
    return jsonify(new_medicament.to_dict()), 201

@medicament_bp.route('/medicaments/<int:id_medicament>', methods=['PUT'])
def edit_medicament(id_medicament):
    data = request.get_json()
    updated_medicament = update_medicament(id_medicament, data)
    return jsonify(updated_medicament.to_dict())

@medicament_bp.route('/medicaments/<int:id_medicament>', methods=['DELETE'])
def remove_medicament(id_medicament):
    delete_medicament(id_medicament)
    return '', 204