from flask import request, jsonify, Blueprint
from models.participant import Participant
from extensions import db

participant_bp = Blueprint('participant_bp', __name__)


@participant_bp.route('/participant', methods=['POST'])
def add_participant():
    data = request.get_json()
    new_participant = Participant(name=data['name'], email=data['email'], event_id=data['event_id'])
    db.session.add(new_participant)
    db.session.commit()
    return jsonify({'message': 'Participant added'}), 201
