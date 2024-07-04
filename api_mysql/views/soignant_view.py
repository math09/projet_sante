from flask import Blueprint, jsonify, request
from config import Config
import jwt
import datetime
from werkzeug.security import generate_password_hash 
from controllers.soignant_controller import (
    get_all_soignants, get_soignant_by_id,
    create_soignant, update_soignant, delete_soignant,
    verify_soignant
)
from auth import token_required

soignant_bp = Blueprint('soignant', __name__)

@soignant_bp.route('/soignants', methods=['GET'])
@token_required
def get_soignants():
    soignants = get_all_soignants()
    return jsonify([soignant.to_dict() for soignant in soignants])

@soignant_bp.route('/soignants/<int:id_medecin>', methods=['GET'])
@token_required
def get_soignant(id_medecin):
    soignant = get_soignant_by_id(id_medecin)
    if soignant is None:
        return jsonify({'error': 'Soignant not found'}), 404
    return jsonify(soignant.to_dict())

@soignant_bp.route('/soignants', methods=['POST'])
@token_required
def add_soignant():
    data = request.get_json()
    data['mdp'] = generate_password_hash(data['mdp'])
    new_soignant = create_soignant(data)
    return jsonify(new_soignant.to_dict()), 201

@soignant_bp.route('/soignants/<int:id_medecin>', methods=['PUT'])
@token_required
def edit_soignant(id_medecin):
    data = request.get_json()
    if 'mdp' in data:
        data['mdp'] = generate_password_hash(data['mdp'])
    updated_soignant = update_soignant(id_medecin, data)
    return jsonify(updated_soignant.to_dict())

@soignant_bp.route('/soignants/<int:id_medecin>', methods=['DELETE'])
@token_required
def remove_soignant(id_medecin):
    delete_soignant(id_medecin)
    return '', 204

@soignant_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    mdp = data.get('mdp')
    soignant = verify_soignant(email, mdp)
    if soignant:
        token = jwt.encode(
            {
                'email': email, 
                'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1)
            }, 
            Config.SECRET_KEY, 
            algorithm='HS256'
        )
        return jsonify({'token': token, 'soignant': soignant.to_dict()})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401