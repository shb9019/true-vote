from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import User,Group,Poll,Option


def create_app():
    """Construct the core application."""
    with app.app_context():
        #from . import routes  # Import routes
        db.create_all()  # Create sql tables for our data models

        return app