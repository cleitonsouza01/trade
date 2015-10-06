"""Tests the real_value property of Operation objects."""

from __future__ import absolute_import
from __future__ import division
import unittest

import trade


class TestOperationRealValueCase00(unittest.TestCase):
    """Test the real_value property of Operation objects.

    The real value of an operation is its value (quantity*price)
    with all commissions and taxes considered.
    """

    def setUp(self):
        self.operation = trade.Operation(
            price=10,
            quantity=20,
        )

    def test_no_discount(self):
        self.assertEqual(self.operation.real_value, 200)

    def test_one_discount(self):
        self.operation.commissions = {
            'some discount': 3
        }
        self.assertEqual(self.operation.real_value, 203)

    def test_multiple_discounts_case_1(self):
        self.operation.commissions = {
            'some discount': 3,
            'other discount': 1
        }
        self.assertEqual(self.operation.real_value, 204)

    def test_multiple_discounts_case_2(self):
        self.operation.commissions = {
            'some discount': 3,
            'other discount': 1,
            'more discounts': 2
        }
        self.assertEqual(self.operation.real_value, 206)

    def test_multiple_discounts_case_3(self):
        self.operation.commissions = {
            'some discount': 3,
            'other discount': 1,
            'negative discount': -1
        }
        self.assertEqual(self.operation.real_value, 203)


class TestOperationRealValueCase01(unittest.TestCase):
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
        )
        self.operation.commissions = {
            'brokerage': 2,
            'some tax': 1.5,
            'other tax': 1,
        }
        self.operation.fees = {
            'some tax': 0.005,
            'some other tax': 0.0275,
        }

    def test_trade_exists(self):
        self.assertTrue(self.operation)

    def test_asset(self):
        self.assertEqual(self.operation.asset, self.asset)

    def test_date(self):
        self.assertEqual(self.operation.date, '2015-09-18')

    def test_quantity(self):
        self.assertEqual(self.operation.quantity, 10)

    def test_price(self):
        self.assertEqual(self.operation.price, 10)

    def test_commissions_dict(self):
        commissions = {
            'brokerage': 2,
            'some tax': 1.5,
            'other tax': 1,
        }
        self.assertEqual(self.operation.commissions, commissions)

    def test_fees_dict(self):
        taxes = {
            'some tax': 0.005,
            'some other tax': 0.0275
        }
        self.assertEqual(self.operation.fees, taxes)

    def test_total_fees_value(self):
        self.assertEqual(
            round(self.operation.total_fees_value, 8),
            0.03250000
        )

    def test_real_price(self):
        self.assertEqual(
            round(self.operation.real_price, 8),
            10.45325000
        )

    def test_real_value(self):
        self.assertEqual(
            round(self.operation.real_value, 8),
            104.532500
        )
