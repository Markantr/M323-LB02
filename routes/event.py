from collections import defaultdict
from datetime import datetime
from functools import reduce
from collections import namedtuple

from flask import request, jsonify, Blueprint, current_app
from models.event import Event
from extensions import db

event_bp = Blueprint('event_bp', __name__)


@event_bp.route('/event', methods=['POST'])
def add_event():
    data = request.get_json()
    event_date = datetime.fromisoformat(data['date'])
    new_event = Event(
        name=data['name'],
        date=event_date,
        location=data['location'],
        description=data['description']
    )
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
    data = request.get_json()
    event = Event.query.get_or_404(event_id)
    event_date = datetime.fromisoformat(data['date'])
    event.name = data['name']
    event.date = event_date
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


# B4 Endpoints

@event_bp.route('/event_names', methods=['GET'])
def get_event_names():
    events = Event.query.all()
    event_names = list(map(lambda e: e.name, events))
    return jsonify(event_names)


@event_bp.route('/future_events', methods=['GET'])
def get_future_events():
    events = Event.query.all()
    future_events = list(filter(lambda e: e.date > datetime.now(), events))
    return jsonify([e.to_dict() for e in future_events])


@event_bp.route('/total_participants', methods=['GET'])
def get_total_participants():
    events = Event.query.all()
    total_participants = reduce(lambda acc, e: acc + len(e.participants), events, 0)
    return jsonify({'total_participants': total_participants})


@event_bp.route('/average_future_participants', methods=['GET'])
def get_average_future_participants():
    events = Event.query.all()
    future_events = list(filter(lambda e: e.date > datetime.now(), events))
    total_participants = reduce(lambda acc, e: acc + len(e.participants), future_events, 0)
    average_participants = total_participants / len(future_events) if future_events else 0
    return jsonify({'average_participants': average_participants})


@event_bp.route('/events_by_month', methods=['GET'])
def get_events_by_month():
    events = Event.query.all()
    events_by_month = defaultdict(list)
    for event in events:
        events_by_month[event.date.month].append(event.to_dict())
    return jsonify(events_by_month)


# A1 Endpoints

EventTuple = namedtuple('EventTuple', ['name', 'date', 'location', 'description'])


@event_bp.route('/immutable_events', methods=['GET'])
def get_immutable_events():
    events = Event.query.all()
    immutable_events = [EventTuple(e.name, e.date, e.location, e.description) for e in events]
    return jsonify([e._asdict() for e in immutable_events])


def format_event(event):
    return f"{event.name} takes place on {event.date} in {event.location}."


@event_bp.route('/formatted_events', methods=['GET'])
def get_formatted_events():
    events = Event.query.all()
    formatted_events = [format_event(e) for e in events]
    return jsonify(formatted_events)


class EventDetailsController:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_event_details(self, event_id):
        return self.db_session.query(Event).filter_by(id=event_id).first()


# OO-Ansatz Route
@event_bp.route('/oo/event/<int:event_id>', methods=['GET'])
def get_event_details_oo(event_id):
    controller = EventDetailsController(db.session)
    event = controller.get_event_details(event_id)
    return jsonify(event.to_dict()) if event else ('', 404)


def get_event_details_procedural(event_id, db_session):
    return db_session.query(Event).filter_by(id=event_id).first()


# Prozeduraler Ansatz Route
@event_bp.route('/procedural/event/<int:event_id>', methods=['GET'])
def get_event_details_procedural_route(event_id):
    event = get_event_details_procedural(event_id, db.session)
    return jsonify(event.to_dict()) if event else ('', 404)


def query_event(event_id):
    return lambda session: session.query(Event).filter_by(id=event_id).first()


# Funktionaler Ansatz Route
@event_bp.route('/functional/event/<int:event_id>', methods=['GET'])
def get_event_details_functional(event_id):
    event_query = query_event(event_id)
    event = event_query(db.session)
    return jsonify(event.to_dict()) if event else ('', 404)


# B1 Endpoints
def calculate_average_participants(events):
    if not events:
        return 0
    total_participants = sum(len(event.participants) for event in events)
    return total_participants / len(events)


def identify_popular_event_types(events):
    type_count = {}
    for event in events:
        if event.event_type in type_count:
            type_count[event.event_type] += 1
        else:
            type_count[event.event_type] = 1

    sorted_types = sorted(type_count.items(), key=lambda x: x[1], reverse=True)
    return [event_type for event_type, count in sorted_types]


def perform_complex_analysis(events):
    average_participants = calculate_average_participants(events)
    popular_event_types = identify_popular_event_types(events)
    return {'average_participants': average_participants, 'popular_event_types': popular_event_types}


# B2 Endpoints

format_event_variable = format_event


@event_bp.route('/formatted_events_variable', methods=['GET'])
def get_formatted_events_variable():
    events = Event.query.all()
    formatted_events = [format_event_variable(e) for e in events]
    return jsonify(formatted_events)


def apply_to_all_events(func):
    events = Event.query.all()
    return [func(event) for event in events]


@event_bp.route('/apply_to_all', methods=['GET'])
def apply_function_to_all_events():
    formatted_events = apply_to_all_events(format_event)
    return jsonify(formatted_events)


def event_filter_closure(criteria):
    def filter_events(events):
        return [event for event in events if criteria(event)]

    return filter_events


@event_bp.route('/filtered_events', methods=['GET'])
def get_filtered_events():
    future_event_filter = event_filter_closure(lambda e: e.date > datetime.now())
    events = Event.query.all()
    future_events = future_event_filter(events)
    return jsonify([e.to_dict() for e in future_events])


# B3 Endpoints

format_date = lambda event: event.date.strftime('%Y-%m-%d')


@event_bp.route('/format_dates', methods=['GET'])
def format_event_dates():
    events = Event.query.all()
    formatted_dates = list(map(format_date, events))
    return jsonify(formatted_dates)


event_in_range = lambda event, start_date, end_date: start_date <= event.date <= end_date


@event_bp.route('/events_in_range', methods=['GET'])
def get_events_in_range():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    events = Event.query.all()
    filtered_events = list(filter(lambda event: event_in_range(event, start_date, end_date), events))
    return jsonify([e.to_dict() for e in filtered_events])


sort_by_participants = lambda events: sorted(events, key=lambda event: len(event.participants))


@event_bp.route('/sorted_by_participants', methods=['GET'])
def get_events_sorted_by_participants():
    events = Event.query.all()
    sorted_events = sort_by_participants(events)
    return jsonify([e.to_dict() for e in sorted_events])
