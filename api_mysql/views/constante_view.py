from flask import Blueprint, jsonify, request
from controllers.constante_controller import (
    get_all_constantes, get_constante_by_id,
    create_constante, update_constante, delete_constante
)

constante_bp = Blueprint('constante', __name__)

@constante_bp.route('/constantes', methods=['GET'])
def get_constantes():
    constantes = get_all_constantes()
    return jsonify([constante.to_dict() for constante in constantes])

@constante_bp.route('/constantes/<int:id_constante>', methods=['GET'])
def get_constante(id_constante):
    constante = get_constante_by_id(id_constante)
    if constante is None:
        return jsonify({'error': 'Constante not found'}), 404
    return jsonify(constante.to_dict())

@constante_bp.route('/constantes', methods=['POST'])
def add_constante():
    data = request.get_json()
    new_constante = create_constante(data)
    return jsonify(new_constante.to_dict()), 201

@constante_bp.route('/constantes/<int:id_constante>', methods=['PUT'])
def edit_constante(id_constante):
    data = request.get_json()
    updated_constante = update_constante(id_constante, data)
    return jsonify(updated_constante.to_dict())

@constante_bp.route('/constantes/<int:id_constante>', methods=['DELETE'])
def remove_constante(id_constante):
    delete_constante(id_constante)
    return '', 204
