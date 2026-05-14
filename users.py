from flask import Blueprint, request, jsonify
import json
import os

users_bp = Blueprint('users', __name__)

USERS_FILE = 'data/users.json'

@users_bp.route('/save-user', methods=['POST'])
def save_user():

    data = request.json

    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump([], f)

    with open(USERS_FILE, 'r') as f:
        users = json.load(f)

    users.append(data)

    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

    return jsonify({'message': 'User saved successfully'})