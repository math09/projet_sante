from flask import Blueprint, jsonify, request
from controllers.examen_controller import (
    get_all_examens, get_examen_by_id, get_examens_by_patient_id,
    create_examen, update_examen, delete_examen
)

examen_bp = Blueprint('examen', __name__)

@examen_bp.route('/examens', methods=['GET'])
def get_examens():
    examens = get_all_examens()
    return jsonify([examen.to_dict() for examen in examens])

@examen_bp.route('/examens/<int:id_examens>', methods=['GET'])
def get_examen(id_examens):
    examen = get_examen_by_id(id_examens)
    if examen is None:
        return jsonify({'error': 'Examen not found'}), 404
    return jsonify(examen.to_dict())

@examen_bp.route('/examens/patient/<int:id_patient>', methods=['GET'])
def get_examen_patient(id_patient):
    examens = get_examens_by_patient_id(id_patient)
    return jsonify([examen.to_dict() for examen in examens])

@examen_bp.route('/examens', methods=['POST'])
def add_examen():
    data = request.get_json()
    new_examen = create_examen(data)
    return jsonify(new_examen.to_dict()), 201

@examen_bp.route('/examens/<int:id_examens>', methods=['PUT'])
def edit_examen(id_examens):
    data = request.get_json()
    updated_examen = update_examen(id_examens, data)
    return jsonify(updated_examen.to_dict())

@examen_bp.route('/examens/<int:id_examens>', methods=['DELETE'])
def remove_examen(id_examens):
    delete_examen(id_examens)
    return 'test', 204
