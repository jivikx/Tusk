from flask import Blueprint, jsonify
import json

parental_bp = Blueprint('parental', __name__)

@parental_bp.route('/parent-data')
def parent_data():

    try:
        with open('data/scores.json', 'r') as f:
            scores = json.load(f)

        with open('data/streaks.json', 'r') as f:
            streaks = json.load(f)

        return jsonify({
            'scores': scores,
            'streak_freezes': streaks
        })

    except:
        return jsonify({
            'scores': [],
            'streak_freezes': []
        })
