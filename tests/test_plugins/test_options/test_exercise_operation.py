"""Test Exercise operations.

Exercise operations calls the exercise() method of its
assets to get the underlying operations of the exercise.
"""

from __future__ import absolute_import
import unittest

import trade


class TestExerciseOperation(unittest.TestCase):

    def setUp(self):
        self.asset = trade.Asset(symbol='GOOGL')
        self.option = trade.plugins.Option(
            name='GOOG151002C00540000',
            expiration_date='2015-10-02',
            underlying_assets={self.asset: 1}
        )

class TestExerciseCase00(TestExerciseOperation):
    """Exercising a call."""

    def setUp(self):
        super(TestExerciseCase00, self).setUp()
        self.exercise = trade.plugins.Exercise(
            date='2015-09-18',
            asset=self.option,
            quantity=100,
            price=10
        )
        self.operations = self.exercise.fetch_operations()

    def test_operations_len(self):
        self.assertEqual(len(self.exercise.operations), 2)

    def test_option_consuming_quantity(self):
        self.assertEqual(self.exercise.operations[0].quantity, -100)

    def test_option_consuming_price(self):
        self.assertEqual(self.exercise.operations[0].price, 0)

    def test_asset_purchase_quantity(self):
        self.assertEqual(self.exercise.operations[1].quantity, 100)

    def test_asset_purchase_price(self):
        self.assertEqual(self.exercise.operations[1].price, 10)


class TestExerciseCase01(TestExerciseOperation):
    """Being exercised on a call."""

    def setUp(self):
        super(TestExerciseCase01, self).setUp()
        self.exercise = trade.plugins.Exercise(
            date='2015-09-18',
            asset=self.option,
            quantity=-100,
            price=10
        )
        self.exercise.fetch_operations()

    def test_operations_len(self):
        self.assertEqual(len(self.exercise.operations), 2)

    def test_option_consuming_quantity(self):
        self.assertEqual(self.exercise.operations[0].quantity, -100)

    def test_option_consuming_price(self):
        self.assertEqual(self.exercise.operations[0].price, 0)

    def test_asset_purchase_quantity(self):
        self.assertEqual(self.exercise.operations[1].quantity, -100)

    def test_asset_purchase_price(self):
        self.assertEqual(self.exercise.operations[1].price, 10)
