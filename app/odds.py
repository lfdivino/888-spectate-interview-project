# -*- coding: utf-8 -*-
from flask_restful import Resource

from app.commands import *
from app.odds_commands import Odd


class Odds(Resource):
    def post(self):
        json_args = get_request_json()

        if not json_args:
            return 'Invalid request json', 400

        return Odd(json_args).update_odds()
