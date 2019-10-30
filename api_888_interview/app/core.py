# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from .routes import add_routes


def core_app():
    """Function responsible for start the Flask API"""
    app = Flask(__name__)
    api = Api(app)
    add_routes(api)

    return app