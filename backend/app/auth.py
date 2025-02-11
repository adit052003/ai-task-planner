# app/auth.py

from flask import Blueprint, request, jsonify
from .models import User
from .extensions import db
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    if not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Username, email, and password are required.'}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists.'}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered.'}), 400

    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    if not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Username and password are required.'}), 400

    user = User.query.filter_by(username=data['username']).first()
    if user is None or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid username or password.'}), 401

    access_token = create_access_token(identity={'username': user.username})
    return jsonify(access_token=access_token), 200