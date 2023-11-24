import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

user = 'postgres'
password = '030507500301'
database = 'data'
cloud_sql_connection_name = 'projectcsci341-406020:europe-central2:postgres-db-csci341'


#create secret key
app.config['SECRET_KEY'] = 'babatyr123'
basedir = os.path.abspath(os.path.dirname(__file__))

tmp_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tmp'))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/data.db'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{user}:{password}@/cloudsql/{cloud_sql_connection_name}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from flaskApp import views