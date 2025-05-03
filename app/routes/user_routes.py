from flask import Blueprint, jsonify

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/', methods=['GET'])
def get_users():
    return jsonify({'users': ['Alice', 'Bob']})
