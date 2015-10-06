"""Test the trade.plugins.fetch_exercises task from the Option plugin."""

from __future__ import absolute_import
import unittest

import trade


class TestFetchExercises(unittest.TestCase):

    def setUp(self):
        self.asset = trade.Asset(symbol='GOOGL')
        self.option = trade.plugins.Option(
            symbol='GOOG151002C00540000',
            expiration_date='2015-10-02',
            underlying_assets={self.asset: 1}
        )
        self.exercise0 = trade.plugins.Exercise(
            date='2015-09-18',
            asset=self.option,
            quantity=100,
            price=1
        )
        self.container = trade.OperationContainer()
        self.container.tasks = [trade.plugins.fetch_exercises]


class TestFetchExercisesCase00(TestFetchExercises):
    """Test the fetch_exercises() task of the Accumulator."""

    def setUp(self):
        super(TestFetchExercisesCase00, self).setUp()
        self.container.operations = [self.exercise0]
        self.container.fetch_positions()

    def test_container_volume(self):
        self.assertEqual(self.container.volume, 100)

    def test_container_exercises_len(self):
        self.assertEqual(
            len(self.container.positions['exercises'].values()),
            2
        )

    def test_option_consuming_quantity(self):
        self.assertEqual(
            self.container.positions['exercises'][self.option.symbol].quantity,
            -100
        )

    def test_option_consuming_price(self):
        self.assertEqual(
            self.container.positions['exercises'][self.option.symbol].price,
            0
        )

    def test_asset_purchase_quantity(self):
        self.assertEqual(
            self.container.positions['exercises'][self.asset.symbol].quantity,
            100
        )

    def test_asset_purchase_price(self):
        self.assertEqual(
            self.container.positions['exercises'][self.asset.symbol].price,
            1
        )


class TestFetchExercisesCase01(TestFetchExercises):
    """Test the fetch_exercises() task of the Accumulator."""

    def setUp(self):
        super(TestFetchExercisesCase01, self).setUp()
        self.exercise1 = trade.plugins.Exercise(
            date='2015-09-18',
            asset=self.option,
            quantity=100,
            price=3
        )
        self.container.operations = [self.exercise0, self.exercise1]
        self.container.fetch_positions()

    def test_container_exercises_len(self):
        self.assertEqual(
            len(self.container.positions['exercises'].values()),
            2
        )

    def test_option_consuming_quantity(self):
        self.assertEqual(
            self.container.positions['exercises'][self.option.symbol].quantity,
            -200
        )

    def test_option_consuming_price(self):
        self.assertEqual(
            self.container.positions['exercises'][self.option.symbol].price,
            0
        )

    def test_asset_purchase_quantity(self):
        self.assertEqual(
            self.container.positions['exercises'][self.asset.symbol].quantity,
            200
        )

    def test_asset_purchase_price(self):
        self.assertEqual(
            self.container.positions['exercises'][self.asset.symbol].price,
            2
        )
