# -*- coding:utf-8 -*-
__author__ = 'fansly'

from flask import Flask
from wepub.extensions import db


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
MONGODB_URI = os.getenv('DATABASE_URL')

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('WePub')
    app.config.from_object(config[config_name])

db = client.test_database