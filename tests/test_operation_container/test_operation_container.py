"""Test the creation of OperationContainer objects."""

from __future__ import absolute_import
import unittest

import trade

from tests.fixtures.fixture_operations import (
    ASSET
)


class TestContainerCreationCase00(unittest.TestCase):
    """Test the creation of a OperationContainer."""

    def setUp(self):
        self.container = trade.OperationContainer()

    def test_container_exists(self):
        self.assertTrue(self.container)


class TestContainerCreationCase01(unittest.TestCase):
    """Test the creation of a OperationContainer."""

    def setUp(self):
        commissions = {
            'brokerage': 2.3,
            'other': 1
        }
        self.container = trade.OperationContainer(
            commissions=commissions
        )
        self.container.fetch_positions_tasks = [
            trade.plugins.fetch_exercises,
            trade.plugins.fetch_daytrades,
        ]
        self.container.fetch_positions()

    def test_container_exists(self):
        self.assertTrue(self.container)

    def test_container_commissions(self):
        commissions = {
            'brokerage': 2.3,
            'other': 1
        }
        self.assertEqual(self.container.commissions, commissions)


class TestContainerAddToPositions(unittest.TestCase):
    """Test add_to_position_operations method."""

    def setUp(self):
        operation = trade.Operation(
            date='2015-09-21',
            asset=ASSET,
            quantity=10,
            price=2
        )
        self.container = trade.OperationContainer(operations=[operation])
        self.container.fetch_positions_tasks = [
            trade.plugins.fetch_exercises,
            trade.plugins.fetch_daytrades,
        ]
        self.container.fetch_positions()
        operation2 = trade.Operation(
            date='2015-09-21',
            asset=ASSET,
            quantity=10,
            price=4
        )
        self.container.add_to_position_operations(operation2)

    def test_common_trades_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)

    def test_for_no_daytrades(self):
        self.assertEqual(len(self.container.positions), 1)

    def test_operations0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].quantity,
            20
        )

    def test_operations0_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].price,
            3
        )
