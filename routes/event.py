from flask import request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from models.event import Event

event_bp = Blueprint('event_bp', __name__)
db = SQLAlchemy()


@event_bp.route('/event', methods=['POST'])
def add_event():
    data = request.get_json()
    new_event = Event(name=data['name'], date=data['date'], location=data['location'], description=data['description'])
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Event added'}), 201


@event_bp.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    output = []
    for event in events:
        event_data = {'id': event.id, 'name': event.name, 'date': event.date, 'location': event.location,
                      'description': event.description}
        output.append(event_data)
    return jsonify({'events': output}), 200


@event_bp.route('/event/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    return jsonify(
        {'name': event.name, 'date': event.date, 'location': event.location, 'description': event.description}), 200


@event_bp.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    event = Event.query.get_or_404(event_id)
    data = request.get_json()
    event.name = data['name']
    event.date = data['date']
    event.location = data['location']
    event.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Event updated'}), 200


@event_bp.route('/event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({'message': 'Event deleted'}), 200
