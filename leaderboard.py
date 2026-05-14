from flask import Blueprint, jsonify

leaderboard_bp = Blueprint('leaderboard', __name__)

@leaderboard_bp.route('/leaderboard')
def leaderboard():

    fake_users = [
        {"name": "Aisha", "points": 950},
        {"name": "Ryan", "points": 920},
        {"name": "Maya", "points": 870},
        {"name": "Zayan", "points": 830}
    ]

    return jsonify(fake_users)