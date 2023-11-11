from flask import Flask
from extensions import db
from routes.event import event_bp
from routes.participant import participant_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'

    db.init_app(app)

    app.register_blueprint(event_bp)
    app.register_blueprint(participant_bp)

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
