from flask import Blueprint, request, jsonify
from app.models.user import User, Address, Geo, Company
from app.extensions import db
from app.schemas.user_schema import UserSchema

user_blueprint = Blueprint('users', __name__)
user_schema = UserSchema()

@user_blueprint.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': u.id, 'username': u.username} for u in users])


@user_blueprint.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()
    
    errors = user_schema.validate(data)
    if errors:
        return jsonify({"errors": errors}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error":"User with this email already exists"}), 409
    
    geo_data = data['address']['geo']
    geo = Geo(lat=geo_data['lat'], lng=geo_data['lng'])
    db.session.add(geo)
    db.session.flush()  # Assign ID without committing
    
    address_data = data['address']
    address = Address(
        street=address_data['street'],
        suite=address_data['suite'],
        city=address_data['city'],
        zipcode=address_data['zipcode'],
        geo=geo
    )
    db.session.add(address)
    db.session.flush()
    
    company_data = data['company']
    company = Company(
        name=company_data['name'],
        catchPhrase=company_data['catchPhrase'],
        bs=company_data['bs']
    )
    db.session.add(company)
    db.session.flush()
    
    user = User(
        name=data['name'],
        username=data['username'],
        email=data['email'],
        phone=data['phone'],
        website=data['website'],
        address=address,
        company=company
    )
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message':'user created'}), 201
    
    
@user_blueprint.route('/', methods=['DELETE'])
def remove_user():
    user_id = request.args.get('id')
    
    if not user_id:
        return jsonify({"error":"Missing user ID in query parameter"}), 400
    
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"error":"User not found"}), 404
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({"message": f"User with ID {user_id} deleted"}), 200