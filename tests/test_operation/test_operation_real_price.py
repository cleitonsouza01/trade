"""Tests the real_price property of Operation objects."""

from __future__ import absolute_import
from __future__ import division
import unittest

import trade


class TestOperationRealPrice(unittest.TestCase):
    """Test the real_price property of Operation objects.

    The real price of an operation (the real unitary price of the
    asset) if the operation's price with all rated commissions
    and taxes.
    """

    def setUp(self):
        self.operation = trade.Operation(
            price=10,
            quantity=20,
        )

    def test_no_discount(self):
        self.assertEqual(self.operation.real_price, 10)

    def test_one_discount(self):
        self.operation.commissions = {
            'some discount': 3
        }
        self.assertEqual(self.operation.real_price, 10.15)

    def test_multiple_discounts_case_1(self):
        self.operation.commissions = {
            'some discount': 3,
            'other discount': 1
        }
        self.assertEqual(self.operation.real_price, 10.2)

    def test_multiple_discounts_case_2(self):
        self.operation.commissions = {
            'some discount': 3,
            'other discount': 1,
            'more discounts': 2
        }
        self.assertEqual(self.operation.real_price, 10.3)

    def test_multiple_discounts_case_3(self):
        self.operation.commissions = {
            'some discount': 3,
            'other discount': 1,
            'negative discount': -1
        }
        self.assertEqual(self.operation.real_price, 10.15)
