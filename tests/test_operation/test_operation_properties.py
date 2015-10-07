"""Tests the real_price property of Operation objects."""

from __future__ import absolute_import
from __future__ import division
import unittest

import trade


class TestOperationProperties(unittest.TestCase):

    def setUp(self):
        self.operation1 = trade.Operation(
            price=10,
            quantity=20
        )
        self.operation2 = trade.Operation(
            price=10,
            quantity=-20
        )


class TestOperationRealPrice(TestOperationProperties):
    """Test the real_price property of Operation objects.

    The real price of an operation (the real unitary price of the
    asset) if the operation's price with all rated commissions
    and taxes.
    """

    def test_price_no_discount(self):
        self.assertEqual(self.operation1.real_price, 10)

    def test_price_one_discount(self):
        self.operation1.commissions = {
            'some discount': 3
        }
        self.assertEqual(self.operation1.real_price, 10.15)

    def test_discounts_case1(self):
        self.operation1.commissions = {
            'some discount': 3,
            'other discount': 1
        }
        self.assertEqual(self.operation1.real_price, 10.2)

    def test_discounts_case2(self):
        self.operation1.commissions = {
            'some discount': 3,
            'other discount': 1,
            'more discounts': 2
        }
        self.assertEqual(self.operation1.real_price, 10.3)

    def test_discounts_case3(self):
        self.operation1.commissions = {
            'some discount': 3,
            'other discount': 1,
            'negative discount': -1
        }
        self.assertEqual(self.operation1.real_price, 10.15)

    def test_value_no_discount(self):
        self.assertEqual(self.operation1.real_value, 200)

    def test_value_one_discount(self):
        self.operation1.commissions = {
            'some discount': 6
        }
        self.assertEqual(self.operation1.real_value, 206)

    def test_value_multiple_discounts_case_1(self):
        self.operation1.commissions = {
            'some discount': 7,
            'other discount': 1
        }
        self.assertEqual(self.operation1.real_value, 208)

    def test_value_multiple_discounts_case_2(self):
        self.operation1.commissions = {
            'some discount': 10,
            'other discount': 1,
            'more discounts': 2
        }
        self.assertEqual(self.operation1.real_value, 213)

    def test_value_multiple_discounts_case_3(self):
        self.operation1.commissions = {
            'some discount': 5,
            'other discount': 1,
            'negative discount': -1
        }
        self.assertEqual(self.operation1.real_value, 205)


class TestOperationRealValueCase01(TestOperationProperties):
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


class TestOperationTotalDiscounts(TestOperationProperties):
    """Test the total_commissions property of Operation objects."""

    def test_one_discount(self):
        self.operation1.commissions = {
            'some discount': 3
        }
        self.assertEqual(self.operation1.total_commissions, 3)

    def test_multiple_discounts_case_1(self):
        self.operation1.commissions = {
            'some discount': 3,
            'other discount': 1
        }
        self.assertEqual(self.operation1.total_commissions, 4)

    def test_multiple_discounts_case_2(self):
        self.operation1.commissions = {
            'some discount': 3,
            'other discount': 1,
            'more discounts': 2
        }
        self.assertEqual(self.operation1.total_commissions, 6)

    def test_multiple_discounts_case_3(self):
        self.operation1.commissions = {
            'some discount': 3,
            'other discount': 1,
            'negative discount': -1
        }
        self.assertEqual(self.operation1.total_commissions, 3)


class TestOperationVolumeCase00(TestOperationProperties):
    """Test the volume property of Operation objects.

    The volume of the operation is its absolute quantity * its price.
    """

    def test_purchase(self):
        self.assertEqual(self.operation1.volume, 200)

    def test_sale(self):
        self.assertEqual(self.operation1.volume, 200)

    def test_sale_with_discounts(self):
        self.operation1.commissions = {
            'brokerage': 2,
            'some tax': 1.5,
            'other tax': 1,
        },
        self.operation1.fees = {
            'some tax': 0.005,
            'some other tax': 0.0275
        }
        self.assertEqual(self.operation1.volume, 200)
