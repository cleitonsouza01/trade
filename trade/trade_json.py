"""trade JSON interface.

https://github.com/rochars/trade
http://trade.readthedocs.org/
License: MIT

Copyright (c) 2015 Rafael da Silva Rocha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from __future__ import absolute_import

import json
from accumulator import Portfolio

from . trade import OperationContainer


class TradeJSON(object):
    """trade JSON interface."""

    def __init__(self, container_tasks, types):
        self.subjects = {}
        self.occurrences = []
        self.containers = {}
        self.container_tasks = container_tasks
        self.types = types

        self.totals = {
            'total_operations': 0,
            'sale_operations': 0,
            'purchase_operations': 0,
            'sale_volume': 0,
            'purchase_volume': 0,
            'total_daytrades': 0
        }

        self.portfolio = None

    def create_subjects(self, data):
        """creates a subject object for all subjects in the json."""
        for subject, details in data['subjects'].items():
            self.subjects[subject] = {
                'object': self.types[details['type']](
                    name=details['name'],
                    symbol=subject,
                    expiration_date=details.get('expiration_date', None),
                    underlying_assets=details.get('underlying_assets', {})
                ),
                'sales': 0,
                'purchases': 0,
                'daytrades': 0,
                'operations': 0
            }

        for subject, obj in self.subjects.items():
            if obj['object'].underlying_assets:
                original_underlying = obj['object'].underlying_assets
                underlying_assets = {}
                for underlying, ratio in original_underlying.items():
                    underlying_assets\
                        [self.subjects[underlying]['object']] = ratio
                obj['object'].underlying_assets = underlying_assets

    def create_occurrences(self, data):
        """Creates all the occurrences described in the json."""
        self.occurrences = []
        for occurrence in data['occurrences']:
            self.occurrences.append(
                self.types[occurrence['type']](
                    quantity=occurrence['quantity'],
                    price=occurrence['price'],
                    date=occurrence['date'],
                    subject=self.subjects[occurrence['subject']]['object']
                )
            )
            self.totals['total_operations'] += 1
            self.subjects[occurrence['subject']]['operations'] += 1
            volume = abs(occurrence['quantity'] * occurrence['price'])
            if occurrence['quantity'] > 0:
                self.totals['purchase_operations'] += 1
                self.totals['purchase_volume'] += volume
                self.subjects[occurrence['subject']]['purchases'] += 1
            else:
                self.totals['sale_operations'] += 1
                self.totals['sale_volume'] += volume
                self.subjects[occurrence['subject']]['sales'] += 1

    def create_containers(self):
        """Creates a container for each operation date.

        The containers are then filled with the respective operations.
        """
        for occurrence in self.occurrences:
            if occurrence.date not in self.containers:
                self.containers[occurrence.date] = OperationContainer(
                    #tasks=[fetch_daytrades]
                    tasks=self.container_tasks
                )
            self.containers[occurrence.date].operations.append(occurrence)

    def create_portfolio(self, data):
        """Create a portfolio to store the positions."""
        initial_state = {}
        for asset_name, asset_state in data['initial state'].items():
            initial_state[self.subjects[asset_name]['object']] = asset_state
        self.portfolio = Portfolio(state=initial_state)

    def accumulate_positions(self):
        """Accumulate each container position on the portoflio."""
        for key in sorted(self.containers.keys()):
            self.containers[key].fetch_positions()
            for position_type, position_asset in \
                self.containers[key].positions.items():
                for asset_symbol, position in position_asset.items():
                    self.portfolio.accumulate(position)
                    if position_type == 'daytrades':
                        self.totals['total_daytrades'] += 1
                        self.subjects[asset_symbol]['daytrades'] += 1

    def get_base_log(self):
        """Get the structure of the return json."""
        return {
            'totals': {
                "sales": {
                    "volume": self.totals['sale_volume'],
                    "operations": self.totals['sale_operations']
                },
                "purchases": {
                    "volume": self.totals['purchase_volume'],
                    "operations": self.totals['purchase_operations']
                },
                "operations": self.totals['total_operations'],
                "daytrades": self.totals['total_daytrades'],
                'results' : {}
            },
            'assets': {}
        }

    def get_states(self):
        """Fill the return json with the log of each accumulator."""
        logs = self.get_base_log()
        for accumulator in self.portfolio.subjects.values():
            if accumulator.subject.symbol not in logs['assets']:
                logs['assets'][accumulator.subject.symbol] = {
                    'totals': {
                        "sales": self.subjects\
                            [accumulator.subject.symbol]['sales'],
                        "purchases": self.subjects\
                            [accumulator.subject.symbol]['purchases'],
                        "operations": self.subjects\
                            [accumulator.subject.symbol]['operations'],
                        "daytrades": self.subjects\
                            [accumulator.subject.symbol]['daytrades'],
                        "results": accumulator.state['results']
                    },
                    'states': {}
                }
            logs['assets'][accumulator.subject.symbol]['states'] = \
                accumulator.log
            for key in accumulator.state['results'].keys():
                if key not in logs['totals']['results']:
                    logs['totals']['results'][key] = 0
                logs['totals']['results'][key] += accumulator.state['results']\
                    [key]
        return logs

    def get_trade_results(self, data):
        """json in, json out"""

        data = json.loads(data)

        # creates an object for all subjects in the json
        self.create_subjects(data)

        # Get all the occurrences described in the json
        self.create_occurrences(data)

        # create a Portfolio with the initial state
        self.create_portfolio(data)

        # Put the operations in containers
        self.create_containers()

        # Fetch the positions on each container
        # and accumulates the positions
        self.accumulate_positions()

        # get the current log and current state of
        # all accumulators
        json_output = json.dumps(self.get_states())

        # returns a json
        return json_output
