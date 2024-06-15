from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from config import Config
from bson.objectid import ObjectId

administration_bp = Blueprint('administration', __name__)

client = MongoClient(Config.MONGO_URI)
db = client[Config.MONGO_DBNAME]


#get all administration
@administration_bp.route('/administration', methods=['GET'])
def get_administration():
    administration = db.administration.find()
    result = []
    for ad in administration:
        ad['_id'] = str(ad['_id'])
        result.append(ad)
    return jsonify(result), 200

# get one administration
@administration_bp.route('/administration/<id>', methods=['GET'])
def get_administration_by_id(id):
    administration = db.administration.find_one({'_id': ObjectId(id)})
    if administration:
        administration['_id'] = str(administration['_id'])
        return jsonify(administration), 200
    else:
        return jsonify({'error': 'Administration not found'}), 404
    
# add administration
@administration_bp.route('/administration', methods=['POST'])
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
def delete_administration(id):
    result = db.administration.delete_one({'_id': ObjectId(id)})

    if result.deleted_count == 0:
        return jsonify({'error': 'Administration not found'}), 404

    return jsonify({'message': 'Administration deleted successfully'}), 200