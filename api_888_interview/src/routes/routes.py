# -*- coding: utf-8 -*-

from api_888_interview.src.resources.event import Event
from api_888_interview.src.resources.odds import Odds
from api_888_interview.src.resources.match import MatchByID, MatchByArgs


def add_routes(api):
    """Function responsible for group all the routes of the API"""
    api.add_resource(Event, '/api/v1/event')
    api.add_resource(MatchByID, '/api/v1/match/<event_id>')
    api.add_resource(MatchByArgs, '/api/v1/match/')
    api.add_resource(Odds, '/api/v1/odds')