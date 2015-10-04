"""Tests the real_value property of Operation objects."""

from __future__ import absolute_import
from __future__ import division
import unittest

import trade


class Test_operation_real_real_valu_case_00(unittest.TestCase):
    """Test the real_value property of Operation objects.

    The real value of an operation is its value (quantity*price)
    with all commissions and taxes considered.
    """

    def setUp(self):
        self.asset = trade.Asset(name='some asset')

    def test_real_price_with_no_discount(self):
        operation = trade.Operation(
            price=10,
            quantity=20
        )
        self.assertEqual(operation.real_value, 200)

    def test_real_value_with_one_discount(self):
        operation = trade.Operation(
            price=10,
            quantity=20,
            commissions={
                'some discount': 3
            }
        )
        self.assertEqual(operation.real_value, 203)

    def test_trade_real_value_with_multiple_discounts_case_1(self):
        operation = trade.Operation(
            price=10,
            quantity=20,
            commissions={
                'some discount': 3,
                'other discount': 1
            }
        )
        self.assertEqual(operation.real_value, 204)

    def test_trade_real_value_with_multiple_discounts_case_2(self):
        operation = trade.Operation(
            price=10,
            quantity=20,
            commissions={
                'some discount': 3,
                'other discount': 1,
                'more discounts': 2
            }
        )
        self.assertEqual(operation.real_value, 206)

    def test_trade_real_value_with_multiple_discounts_case_3(self):
        operation = trade.Operation(
            price=10,
            quantity=20,
            commissions={
                'some discount': 3,
                'other discount': 1,
                'negative discount': -1
            }
        )
        self.assertEqual(operation.real_value, 203)


class Test_operation_real_value_Case_01(unittest.TestCase):
    """Test the real_value property of Operation objects.

    In this TestCase we define multiple taxes.
    """

    def setUp(self):
        self.asset = trade.Asset(name='some asset')
        self.operation = trade.Operation(
            date='2015-09-18',
            asset=self.asset,
            quantity=10,
            price=10,
            commissions={
                'brokerage': 2,
                'some tax': 1.5,
                'other tax': 1,
            },
            fees={
                'some tax': 0.005,
                'some other tax': 0.0275,
            }
        )

    def test_trade_exists(self):
        self.assertTrue(self.operation)

    def test_trade_asset(self):
        self.assertEqual(self.operation.asset, self.asset)

    def test_trade_date_should_be_2015_09_18(self):
        self.assertEqual(self.operation.date, '2015-09-18')

    def test_trade_quantity_should_be_20(self):
        self.assertEqual(self.operation.quantity, 10)

    def test_trade_price_should_be_10(self):
        self.assertEqual(self.operation.price, 10)

    def test_trade_commissions_dict(self):
        commissions = {
            'brokerage': 2,
            'some tax': 1.5,
            'other tax': 1,
        }
        self.assertEqual(self.operation.commissions, commissions)

    def test_trade_taxes_dict(self):
        taxes = {
            'some tax': 0.005,
            'some other tax': 0.0275
        }
        self.assertEqual(self.operation.fees, taxes)

    def test_trade_total_tax_value(self):
        self.assertEqual(
            round(self.operation.total_fees_value, 8),
            0.03250000
        )

    def test_trade_real_price(self):
        self.assertEqual(
            round(self.operation.real_price, 8),
            10.45325000
        )

    def test_trade_real_value(self):
        self.assertEqual(
            round(self.operation.real_value, 8),
            104.532500
        )
