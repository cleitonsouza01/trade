"""Test the trade.plugins.fetch_exercises task from the Option plugin."""

from __future__ import absolute_import
import unittest
import copy

import trade

from tests.fixtures.operations import (
    EXERCISE_OPERATION2, EXERCISE_OPERATION3
)
from tests.fixtures.assets import (
    ASSET, OPTION1,
)


class TestFetchExercises(unittest.TestCase):
    """Base class for the fetch_exercises() task."""

    def setUp(self):
        self.container = trade.OperationContainer()
        self.container.tasks = [trade.plugins.fetch_exercises]


class TestFetchExercisesCase00(TestFetchExercises):
    """Test the fetch_exercises() task of the Accumulator."""

    def setUp(self):
        super(TestFetchExercisesCase00, self).setUp()
        self.container.operations = [copy.deepcopy(EXERCISE_OPERATION2)]
        self.container.fetch_positions()

    def test_container_volume(self):
        self.assertEqual(self.container.volume, 100)

    def test_container_exercises_len(self):
        self.assertEqual(
            len(self.container.positions['exercises'].values()), 2
        )

    def test_option_consuming_quantity(self):
        self.assertEqual(
            self.container.positions['exercises'][OPTION1.symbol].quantity,
            -100
        )

    def test_option_consuming_price(self):
        self.assertEqual(
            self.container.positions['exercises'][OPTION1.symbol].price, 0
        )

    def test_asset_purchase_quantity(self):
        self.assertEqual(
            self.container.positions['exercises'][ASSET.symbol].quantity, 100
        )

    def test_asset_purchase_price(self):
        self.assertEqual(
            self.container.positions['exercises'][ASSET.symbol].price, 1
        )


class TestFetchExercisesCase01(TestFetchExercises):
    """Test the fetch_exercises() task of the Accumulator."""

    def setUp(self):
        super(TestFetchExercisesCase01, self).setUp()
        self.container.operations = [
            copy.deepcopy(EXERCISE_OPERATION2),
            copy.deepcopy(EXERCISE_OPERATION3)
        ]
        self.container.fetch_positions()

    def test_container_exercises_len(self):
        self.assertEqual(
            len(self.container.positions['exercises'].values()), 2
        )

    def test_option_consuming_quantity(self):
        self.assertEqual(
            self.container.positions['exercises'][OPTION1.symbol].quantity,
            -200
        )

    def test_option_consuming_price(self):
        self.assertEqual(
            self.container.positions['exercises'][OPTION1.symbol].price, 0
        )

    def test_asset_purchase_quantity(self):
        self.assertEqual(
            self.container.positions['exercises'][ASSET.symbol].quantity, 200
        )

    def test_asset_purchase_price(self):
        self.assertEqual(
            self.container.positions['exercises'][ASSET.symbol].price, 2
        )
