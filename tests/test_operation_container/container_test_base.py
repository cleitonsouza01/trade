"""Base class for container tests."""

from __future__ import absolute_import
import unittest
import copy

import trade
from trade.plugins import (
    prorate_commissions,
)


class TestFetchPositions(unittest.TestCase):
    """Create the default operations for the test cases."""

    commissions = {}
    operations = []
    positions = {}
    daytrades = {}
    exercises = {}
    volume = False

    def setUp(self):
        self.container = trade.OperationContainer()
        self.container.commissions = self.commissions
        self.container.operations = copy.deepcopy(self.operations)
        if not self.volume:
            self.volume = sum(
                operation.volume for operation in self.container.operations
            )
        self.container.tasks = [
            trade.plugins.fetch_exercises,
            trade.plugins.fetch_daytrades,
        ]
        self.container.fetch_positions()
        prorate_commissions(self.container)

        self.state = {
            'operations': self.positions,
            'exercises': self.exercises,
            'daytrades': self.daytrades
        }

    def test_container_volume(self):
        """Check the volume of the OperationContainer."""
        self.assertEqual(self.container.volume, self.volume)

    def len_check(self, len_type):
        """Check the len of a type of position in the container."""
        if len_type in self.container.positions:
            self.assertEqual(
                len(self.container.positions[len_type].keys()),
                len(self.state[len_type].keys())
            )

    def state_check(self, position_type):
        """Check the state of a type of position in the container."""
        if position_type in self.container.positions:
            for position in self.container.positions[position_type].values():
                position_details = position.__dict__
                for key in position_details:
                    if key in \
                        self.state[position_type][position.subject.symbol]:
                        self.assertEqual(
                            position_details[key],
                            self.state\
                                [position_type][position.subject.symbol][key]
                        )

    def test_operations_len(self):
        """Check the len of the common operations positions."""
        self.len_check('operations')

    def test_operations_states(self):
        """Check the state of the common operations positions."""
        self.state_check('operations')

    def test_exercises_len(self):
        """Check the len of the exercise positions."""
        self.len_check('exercises')

    def test_exercise_states(self):
        """Check the state of the exercise positions."""
        self.state_check('exercises')

    def test_daytrades_len(self):
        """Check the len of the daytrade positions."""
        self.len_check('daytrades')

    def test_daytrades_states(self):
        self.state_check('daytrades')

    def test_daytrades_buy_state(self):
        """Test the buy price for all daytrades in the container."""
        for asset in self.daytrades.keys():
            self.assertEqual(
                (
                    self.container.positions['daytrades'][asset]\
                        .operations[0].price,
                    self.container.positions['daytrades'][asset]\
                        .operations[0].quantity,
                    self.container.positions['daytrades'][asset]\
                        .operations[0].commissions,
                ),
                (
                    self.daytrades[asset]['buy price'],
                    self.daytrades[asset]['buy quantity'],
                    self.daytrades[asset]['buy commissions']
                )
            )

    def test_daytrades_sale_state(self):
        """Test the sale price for all daytrades in the container."""
        for asset in self.daytrades.keys():
            self.assertEqual(
                (
                    self.container.positions['daytrades'][asset]\
                        .operations[1].price,
                    self.container.positions['daytrades'][asset]\
                        .operations[1].quantity,
                    self.container.positions['daytrades'][asset]\
                        .operations[1].commissions,
                ),
                (
                    self.daytrades[asset]['sale price'],
                    self.daytrades[asset]['sale quantity'],
                    self.daytrades[asset]['sale commissions']
                )
            )
