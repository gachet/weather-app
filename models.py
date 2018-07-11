from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/tcd55/Documents/weather-app/database.db'


class Temperatures(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    timestamp = db.Column(db.DateTime,default=datetime.utcnow)
    temperatures = db.Column(db.String(20))