from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from config import Config
from bson.objectid import ObjectId
import datetime
import jwt
from auth import token_required

administration_bp = Blueprint('administration', __name__)

client = MongoClient(Config.MONGO_URI)
db = client[Config.MONGO_DBNAME]


#get all administration
@administration_bp.route('/administration', methods=['GET'])
@token_required
def get_administration():
    administration = db.administration.find()
    result = []
    for ad in administration:
        ad['_id'] = str(ad['_id'])
        result.append(ad)
    return jsonify(result), 200

# get one administration
@administration_bp.route('/administration/<id>', methods=['GET'])
@token_required
def get_administration_by_id(id):
    administration = db.administration.find_one({'_id': ObjectId(id)})
    if administration:
        administration['_id'] = str(administration['_id'])
        return jsonify(administration), 200
    else:
        return jsonify({'error': 'Administration not found'}), 404
    
# add administration
@administration_bp.route('/administration', methods=['POST'])
@token_required
def add_administration():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    result = db.administration.insert_one(data)
    
    inserted_administration = db.administration.find_one({'_id': result.inserted_id})

    inserted_administration['_id'] = str(inserted_administration['_id'])

    return jsonify(inserted_administration), 201


# update administration
@administration_bp.route('/administration/<id>', methods=['PUT'])
@token_required
def update_administration(id):
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    result = db.administration.update_one({'_id': ObjectId(id)}, {'$set': data})

    if result.matched_count == 0:
        return jsonify({'error': 'Administration not found'}), 404

    updated_administration = db.administration.find_one({'_id': ObjectId(id)})
    updated_administration['_id'] = str(updated_administration['_id'])

    return jsonify(updated_administration), 200


# delete administration
@administration_bp.route('/administration/<id>', methods=['DELETE'])
@token_required
def delete_administration(id):
    result = db.administration.delete_one({'_id': ObjectId(id)})

    if result.deleted_count == 0:
        return jsonify({'error': 'Administration not found'}), 404

    return jsonify({'message': 'Administration deleted successfully'}), 200

# login administration
@administration_bp.route('/login', methods=['POST'])
def login_administration():
    data = request.get_json()
    email = data.get('email')
    mdp = data.get('mdp')
    admin = verify_administration(email, mdp)
    if admin:
        token = jwt.encode(
            {
                'email': email,
                'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1)
            },
            Config.SECRET_KEY,
            algorithm='HS256'
        )
        admin['_id'] = str(admin['_id'])
        return jsonify({'token': token, 'patient': admin}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401
    
def verify_administration(email, mdp):
    admin = db.administration.find_one({'email': email, 'mdp': mdp})
    return admin

def create_admin_user():
    admin = db.administration.find_one({'email': 'admin@gmail.com'})
    if admin:
        return
    
    admin_data = {
        'email': 'admin@gmail.com',
        'mdp': 'admin',
        'is_admin': True
    }
    db.administration.insert_one(admin_data)