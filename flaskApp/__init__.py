import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
#create secret key
app.config['SECRET_KEY'] = 'babatyr123'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from flaskApp import views