from __future__ import absolute_import
import unittest

import trade


class TestExercise_Case_00(unittest.TestCase):
    """Exercising a call.
    """

    def setUp(self):

        self.asset = trade.Asset(symbol='GOOGL')
        self.option = trade.Option(
                        name='GOOG151002C00540000',
                        expiration_date='2015-10-02',
                        underlying_assets=[self.asset]
                    )
        self.exercise = trade.Exercise(
			date='2015-09-18',
			asset=self.option,
			quantity=100,
			price=10
        )
        self.operations = self.exercise.get_operations()

    def test_operations_len(self):
        self.assertEqual(len(self.operations), 2)

    def test_option_consuming_operation_quantity(self):
        self.assertEqual(self.operations[0].quantity, -100)

    def test_option_consuming_operation_price(self):
        self.assertEqual(self.operations[0].price, 0)

    def test_asset_purchase_operation_quantity(self):
        self.assertEqual(self.operations[1].quantity, 100)

    # FIXME premium!
    def test_asset_purchase_operation_price(self):
        self.assertEqual(self.operations[1].price, 10)




class TestExercise_Case_01(unittest.TestCase):
    """Being exercised on a call.
    """

    def setUp(self):

        self.asset = trade.Asset(symbol='GOOGL')
        self.option = trade.Option(
                        name='GOOG151002C00540000',
                        expiration_date='2015-10-02',
                        underlying_assets=[self.asset]
                    )
        self.exercise = trade.Exercise(
			date='2015-09-18',
			asset=self.option,
			quantity=-100,
			price=10
        )
        self.operations = self.exercise.get_operations()

    def test_operations_len(self):
        self.assertEqual(len(self.operations), 2)

    def test_option_consuming_operation_quantity(self):
        self.assertEqual(self.operations[0].quantity, -100)

    def test_option_consuming_operation_price(self):
        self.assertEqual(self.operations[0].price, 0)

    def test_asset_purchase_operation_quantity(self):
        self.assertEqual(self.operations[1].quantity, -100)

    # FIXME premium!
    def test_asset_purchase_operation_price(self):
        self.assertEqual(self.operations[1].price, 10)
