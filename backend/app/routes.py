# app/routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import User, Task
from .extensions import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({'message': 'Hello, AI Task Planner!'})

# Protected route example
@main.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    current_user_identity = get_jwt_identity()
    user = User.query.filter_by(username=current_user_identity['username']).first()
    tasks = user.tasks.all()
    return jsonify([task.to_dict() for task in tasks])

@main.route('/api/test', methods=['GET'])
def test():
    return jsonify({"message": "Backend is connected!"})