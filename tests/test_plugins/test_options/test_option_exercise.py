"""Test the exercise() method of Option objects."""

from __future__ import absolute_import
import unittest

import trade


class TestOptionExercises(unittest.TestCase):

    def setUp(self):
        self.asset = trade.Asset(symbol='GOOGL')
        self.option = trade.plugins.Option(
            symbol='GOOG151002C00540000',
            expiration_date='2015-10-02',
            underlying_assets=[self.asset]
        )


class TestOptionExerciseCase00(TestOptionExercises):
    """Test the exercise of a call."""

    def setUp(self):
        super(TestOptionExerciseCase00, self).setUp()
        self.operations = self.option.exercise(
            quantity=100,
            price=10,
            date='2015-09-30'
        )

    def test_operations_len(self):
        self.assertEqual(len(self.operations), 2)

    def test_option_consuming_operation_quantity(self):
        self.assertEqual(self.operations[0].quantity, -100)

    def test_option_consuming_operation_price(self):
        self.assertEqual(self.operations[0].price, 0)

    def test_asset_purchase_operation_quantity(self):
        self.assertEqual(self.operations[1].quantity, 100)

    def test_asset_purchase_operation_price(self):
        self.assertEqual(self.operations[1].price, 10)



class TestOptionExerciseCase01(TestOptionExercises):
    """Test the exercise of a put."""

    def setUp(self):
        super(TestOptionExerciseCase01, self).setUp()
        self.operations = self.option.exercise(
            quantity=-100,
            price=10,
            date='2015-09-30'
        )

    def test_operations_len(self):
        self.assertEqual(len(self.operations), 2)

    def test_option_consuming_operation_quantity(self):
        self.assertEqual(self.operations[0].quantity, -100)

    def test_option_consuming_operation_price(self):
        self.assertEqual(self.operations[0].price, 0)

    def test_asset_purchase_operation_quantity(self):
        self.assertEqual(self.operations[1].quantity, -100)

    def test_asset_purchase_operation_price(self):
        self.assertEqual(self.operations[1].price, 10)
