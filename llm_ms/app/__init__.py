from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from dotenv import load_dotenv
from flask_cors import CORS


load_dotenv()


app = Flask(__name__)
CORS(app)


app.config.from_object('app.config.Config')


db = SQLAlchemy(app)
ma = Marshmallow(app)

from app.routes import *


with app.app_context():
    db.create_all()
