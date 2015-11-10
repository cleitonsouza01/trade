"""Prototype for a trade module JSON interface."""

from __future__ import absolute_import

import json

from .trade import Asset, Operation, OperationContainer
from accumulator import Portfolio
from .options import Option, Exercise, fetch_exercises
from .daytrades import fetch_daytrades


class TradeJSON(object):
    """trade module JSON interface.

    json_input = {
        "subjects": {
            "GOOG": {
                "type": "Asset",
                "name": "Google Inc",
                "expiration_date": "2019-01-01"
            },
            "AAPL": {
                "type": "Asset",
                "name": "Apple Inc.",
                "expiration_date": ""
            },
            ...
        },
        "occurrences": [
            {
                "type": "Operation",
                "subject": "GOOG",
                "date": "2015-01-01",
                "quantity": 10,
                "price": 650.11,
                "commissions": {},
                "raw_results": {},
                "operations": []
            },
            ...
        ],
        "initial state": {
            "AAPL": {
                "date": "2015-11-09",
                "quantity": 92,
                "price": 31.21,
                "results": {"trades": 5000.72}
            },
            ...
        }
    }

    json_output = {
        "GOOG": {
            "2015-01-01": {
                "quantity": 10,
                "price": 650.11,
                "results": {}
            },
            ...
        },
        "AAPL": {
            "2015-11-09": {
                "quantity": 92,
                "price": 31.21,
                "results": {"trades": 5000.72}
            },
            ...
        }
    }
    """

    TYPES = {
        'Asset': Asset,
        'Option': Option,
        'Operation': Operation,
        'Exercise': Exercise
    }

    def __init__(self):
        self.subjects = {}
        self.occurrences = []
        self.containers = {}

    def create_subjects(self, data):
        """creates a subject object for all subjects in the json."""
        for subject, details in data['subjects'].items():
            self.subjects[subject] = self.TYPES[details['type']](
                name=details['name'],
                symbol=subject,
                expiration_date=details['expiration_date']
            )

    def get_trade_results(self, data):
        """json in, json out"""
        data = json.loads(data)

        # creates an object for all subjects in the json
        self.create_subjects(data)

        # Get all the occurrences described in the json
        self.occurrences = []
        for occurrence in data['occurrences']:
            self.occurrences.append(
                self.TYPES[occurrence['type']](
                    quantity=occurrence['quantity'],
                    price=occurrence['price'],
                    date=occurrence['date'],
                    subject=self.subjects[occurrence['subject']]
                )
            )

        # Put the operations in containers
        for occurrence in self.occurrences:
            if occurrence.date not in self.containers:
                self.containers[occurrence.date] = OperationContainer(
                    tasks=[fetch_daytrades, fetch_exercises]
                )
            self.containers[occurrence.date].operations.append(occurrence)

        initial_state = {}
        for asset_name, asset_state in data['initial state'].items():
            initial_state[self.subjects[asset_name]] = asset_state

        # create a Portfolio with the initial state
        portfolio = Portfolio(state=initial_state)

        # Fetch the positions on each container
        # and accumulates the positions
        for key in sorted(self.containers.keys()):
            self.containers[key].fetch_positions()
            for position_type in self.containers[key].positions.values():
                for position in position_type.values():
                    portfolio.accumulate(position)

        logs = {}
        for accumulator in portfolio.subjects.values():
            logs[accumulator.subject.symbol] = accumulator.log

        # get the current log and current state of
        # all accumulators
        logs = json.dumps(logs)

        # returns a json
        return logs
