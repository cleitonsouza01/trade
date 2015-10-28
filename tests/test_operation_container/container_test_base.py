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
    volume = 0

    def setUp(self):
        self.container = trade.OperationContainer()
        self.container.commissions = self.commissions
        self.container.operations = copy.deepcopy(self.operations)
        self.container.tasks = [
            trade.plugins.fetch_exercises,
            trade.plugins.fetch_daytrades,
        ]
        self.container.fetch_positions()
        prorate_commissions(self.container)

    def test_container_volume(self):
        self.assertEqual(self.container.volume, self.volume)

    def test_operations_quantity(self):
        """Test the quantity for all positions in the container."""
        for asset in self.positions.keys():
            self.assertEqual(
                self.container.positions['operations'][asset].quantity,
                self.positions[asset]['quantity']
            )

    def test_operations_price(self):
        """Test the price for all positions in the container."""
        for asset in self.positions.keys():
            self.assertEqual(
                self.container.positions['operations'][asset].price,
                self.positions[asset]['price']
            )

    def test_operations_volume(self):
        """Test the volume for all positions in the container."""
        for asset in self.positions.keys():
            self.assertEqual(
                self.container.positions['operations'][asset].volume,
                self.positions[asset]['volume']
            )

    def test_daytrades_len(self):
        """Test the len of the daytrades in the container."""
        if 'daytrades' in self.container.positions:
            self.assertEqual(
                len(self.container.positions['daytrades'].keys()),
                len(self.daytrades.keys())
            )

    def test_operations_len(self):
        """Test the len of the positions in the container."""
        if 'operations' in self.container.positions:
            self.assertEqual(
                len(self.container.positions['operations'].keys()),
                len(self.positions.keys())
            )

    def test_daytrades_quantity(self):
        """Test the quantity for all daytrades in the container."""
        for asset in self.daytrades.keys():
            self.assertEqual(
                self.container.positions['daytrades'][asset].quantity,
                self.daytrades[asset]['quantity']
            )

    def test_daytrades_buy_price(self):
        """Test the buy price for all daytrades in the container."""
        for asset in self.daytrades.keys():
            self.assertEqual(
                self.container.positions['daytrades'][asset]\
                    .operations[0].price,
                self.daytrades[asset]['buy price']
            )

    def test_daytrades_buy_quantity(self):
        """Test the buy quantity for all daytrades in the container."""
        for asset in self.daytrades.keys():
            self.assertEqual(
                self.container.positions['daytrades'][asset]\
                    .operations[0].quantity,
                self.daytrades[asset]['buy quantity']
            )

    def test_daytrades_sale_price(self):
        """Test the sale price for all daytrades in the container."""
        for asset in self.daytrades.keys():
            self.assertEqual(
                self.container.positions['daytrades'][asset]\
                    .operations[1].price,
                self.daytrades[asset]['sale price']
            )

    def test_daytrades_sale_quantity(self):
        """Test the sale quantity for all daytrades in the container."""
        for asset in self.daytrades.keys():
            self.assertEqual(
                self.container.positions['daytrades'][asset]\
                    .operations[1].quantity,
                self.daytrades[asset]['sale quantity']
            )

    def test_daytrades_result(self):
        """Test the results for all daytrades in the container."""
        for asset in self.daytrades.keys():
            self.assertEqual(
                self.container.positions['daytrades'][asset].results,
                self.daytrades[asset]['result']
            )

    def test_daytrades_buy_discounts(self):
        """Test the discounts for all daytrades buy operations."""
        for asset in self.daytrades.keys():
            self.assertEqual(
                self.container.positions['daytrades'][asset]\
                    .operations[0].commissions,
                self.daytrades[asset]['buy commissions']
            )

    def test_daytrades_sale_discounts(self):
        """Test the discounts for all daytrades sale operations."""
        for asset in self.daytrades.keys():
            self.assertEqual(
                self.container.positions['daytrades'][asset]\
                    .operations[1].commissions,
                self.daytrades[asset]['sale commissions']
            )


    def test_container_exercises_len(self):
        if 'exercises' in self.container.positions:
            self.assertEqual(
                len(self.container.positions['exercises'].keys()),
                len(self.exercises.keys()),
            )

    def test_option_consuming_quantity(self):
        for asset in self.exercises.keys():
            self.assertEqual(
                self.container.positions['exercises'][asset].quantity,
                self.exercises[asset]['quantity']
            )

    def test_option_consuming_price(self):
        for asset in self.exercises.keys():
            self.assertEqual(
                self.container.positions['exercises'][asset].price,
                self.exercises[asset]['price']
            )
