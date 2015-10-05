"""Test the trade.plugins.fetch_exercises task from the Option plugin."""

from __future__ import absolute_import
import unittest

import trade


class TestFetchExercisesCase00(unittest.TestCase):
    """Test the fetch_exercises() task of the Accumulator."""

    def setUp(self):
        self.asset = trade.Asset(symbol='GOOGL')
        self.option = trade.plugins.Option(
            symbol='GOOG151002C00540000',
            expiration_date='2015-10-02',
            underlying_assets=[self.asset]
        )
        self.exercise = trade.plugins.Exercise(
            date='2015-09-18',
            asset=self.option,
            quantity=100,
            price=10
        )
        self.container = trade.OperationContainer(
            operations=[self.exercise]
        )
        self.container.tasks = [
            trade.plugins.fetch_exercises,
        ]
        self.container.fetch_positions()

    def test_operation_container_volume(self):
        self.assertEqual(self.container.volume, 1000)

    def test_container_exercise_operations_len(self):
        self.assertEqual(
            len(self.container.positions['exercises'].values()),
            2
        )

    def test_option_consuming_operation_quantity(self):
        self.assertEqual(
            self.container.positions['exercises'][self.option.symbol].quantity,
            -100
        )

    def test_option_consuming_operation_price(self):
        self.assertEqual(
            self.container.positions['exercises'][self.option.symbol].price,
            0
        )

    def test_asset_purchase_operation_quantity(self):
        self.assertEqual(
            self.container.positions['exercises'][self.asset.symbol].quantity,
            100
        )

    def test_asset_purchase_operation_price(self):
        self.assertEqual(
            self.container.positions['exercises'][self.asset.symbol].price,
            10
        )


class TestFetchExercisesCase01(unittest.TestCase):
    """Test the fetch_exercises() task of the Accumulator."""

    def setUp(self):
        self.asset = trade.Asset(symbol='GOOGL')
        self.option = trade.plugins.Option(
            symbol='GOOG151002C00540000',
            expiration_date='2015-10-02',
            underlying_assets=[self.asset]
        )
        self.exercise0 = trade.plugins.Exercise(
            date='2015-09-18',
            asset=self.option,
            quantity=100,
            price=1
        )
        self.exercise1 = trade.plugins.Exercise(
            date='2015-09-18',
            asset=self.option,
            quantity=100,
            price=3
        )
        self.container = trade.OperationContainer(
            operations=[self.exercise0, self.exercise1]
        )
        self.container.tasks = [
            trade.plugins.fetch_exercises,
        ]

    def test_container_exercise_operations_len(self):
        self.container.fetch_positions()
        self.assertEqual(
            len(self.container.positions['exercises'].values()),
            2
        )

    def test_option_consuming_operation_quantity(self):
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['exercises'][self.option.symbol].quantity,
            -200
        )

    def test_option_consuming_operation_price(self):
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['exercises'][self.option.symbol].price,
            0
        )

    def test_asset_purchase_operation_quantity(self):
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['exercises'][self.asset.symbol].quantity,
            200
        )

    def test_asset_purchase_operation_price(self):
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['exercises'][self.asset.symbol].price,
            2
        )
