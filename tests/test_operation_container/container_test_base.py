"""Base class for container tests."""

from __future__ import absolute_import
import unittest
import copy

from trade import trade
from trade.container_tasks import (
    prorate_commissions, fetch_daytrades, group_positions, find_volume
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
        tasks = [
            find_volume,
            fetch_daytrades,
            group_positions,
            prorate_commissions,
        ]
        self.container = trade.OperationContainer(
            operations=copy.deepcopy(self.operations),
            tasks=tasks
            )
        self.container.commissions = self.commissions
        if not self.volume:
            self.volume = sum(
                operation.volume for operation in self.container.operations
            )
        self.container.fetch_positions()
        self.state = {
            'operations': self.positions,
            'exercises': self.exercises,
            'daytrades': self.daytrades
        }

    def test_container_volume(self):
        """Check the volume of the OperationContainer."""
        self.assertEqual(self.container.context['volume'], self.volume)

    def len_check(self, len_type):
        """Check the len of a type of position in the container."""
        if 'positions' in self.container.context:
            if len_type in self.container.context['positions']:
                self.assertEqual(
                    len(self.container.context['positions'][len_type].keys()),
                    len(self.state[len_type].keys())
                )

    def state_check(self, position_type):
        """Check the state of a type of position in the container."""
        if position_type in self.container.context['positions']:
            for position in self.container.context['positions']\
            [position_type].values():
                position_details = position.__dict__
                for key in position_details:
                    if key in \
                        self.state[position_type][position.subject.symbol]:
                        self.assertEqual(
                            position_details[key],
                            self.state[position_type]\
                                [position.subject.symbol][key]
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
        """Check the state of the daytrade positions."""
        self.state_check('daytrades')

    def test_daytrades_buy_state(self):
        """Check the state of the daytrade positions purchases."""
        self.check_daytrade_suboperation(0, 'buy')

    def test_daytrades_sale_state(self):
        """Check the state of the daytrade positions sales."""
        self.check_daytrade_suboperation(1, 'sale')

    def check_daytrade_suboperation(self, operation_index, operation_type):
        """Check the state of the daytrade suboperations."""
        if 'daytrades' in self.container.context['positions']:
            for asset in self.daytrades.keys():
                self.assertEqual(
                    (
                        self.container.context['positions']['daytrades'][asset]\
                            .operations[operation_index].price,
                        self.container.context['positions']['daytrades'][asset]\
                            .operations[operation_index].quantity,
                        self.container.context['positions']['daytrades'][asset]\
                            .operations[operation_index].commissions,
                    ),
                    (
                        self.daytrades[asset][operation_type + ' price'],
                        self.daytrades[asset][operation_type + ' quantity'],
                        self.daytrades[asset][operation_type + ' commissions']
                    )
                )
