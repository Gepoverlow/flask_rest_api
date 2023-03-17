import os
from flask import Flask
from app import main
from app.main.database import db
from app.main.api import api

# Flask App Initialization
app = Flask(__name__)
app.config.from_object(main.settings[os.environ.get('APPLICATION_ENV', 'default')])

# Database ORM Initialization
from app import model
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()


# Flask API Initialization
api.init_app(app)