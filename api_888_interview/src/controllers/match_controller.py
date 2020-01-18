# -*- coding: utf-8 -*-

from api_888_interview.src.database.db_match import DBMatch


class MatchController:
    """Class responsible to treat the data from the matches search parameters
    and call the match database functions

    :param event_id: A Integer, One of the querystring parameter
    :param name: A String, One of the querystring parameter
    :param sport: A String, One of the querystring parameter
    :param ordering: A String, One of the querystring parameter

    """
    def __init__(self, event_id=None, name=None, sport=None, ordering=None):
        self.event_id = event_id
        self.name = name
        self.sport = sport.capitalize() if sport else sport
        self.ordering = ordering
        self.db_match = DBMatch()

    def get_events(self):
        """Return all the events in the collection"""
        event = [event for event in self.db_match.select_events()]

        return self.verify_event_db_return(event)

    def get_event_by_id(self):
        """Return the match by its 'id'"""
        event = self.db_match.select_event_by_id(int(self.event_id))

        return self.verify_event_db_return(event)

    def get_event_by_name(self):
        """Return the match by its 'name'"""
        event = self.db_match.select_event_by_name(self.name)

        return self.verify_event_db_return(event)

    def get_event_by_sport(self):
        """Return all matches by its 'sport' name"""
        events = [event for event in self.db_match.select_event_by_sport(
            self.sport, self.ordering)]

        return self.verify_event_db_return(events)

    @staticmethod
    def verify_event_db_return(event):
        if not event:
            return 'Match not found!', 404

        return event, 200
