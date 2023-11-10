from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.event import event_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.register_blueprint(event_bp)
    app.run(debug=True)
