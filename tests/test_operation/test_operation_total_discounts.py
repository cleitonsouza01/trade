"""Tests the total_commissions property of Operation objects."""

from __future__ import absolute_import
from __future__ import division
import unittest

import trade

OPERATION = trade.Operation(
    quantity=1,
    price=1,

)

class TestOperationTotalDiscounts(unittest.TestCase):
    """Test the total_commissions property of Operation objects."""

    def setUp(self):
        self.asset = trade.Asset(name='some asset')

    def test_one_discount(self):
        OPERATION.commissions = {
            'some discount': 3
        }
        self.assertEqual(OPERATION.total_commissions, 3)

    def test_multiple_discounts_case_1(self):
        OPERATION.commissions = {
            'some discount': 3,
            'other discount': 1
        }
        self.assertEqual(OPERATION.total_commissions, 4)

    def test_multiple_discounts_case_2(self):
        OPERATION.commissions = {
            'some discount': 3,
            'other discount': 1,
            'more discounts': 2
        }
        self.assertEqual(OPERATION.total_commissions, 6)

    def test_multiple_discounts_case_3(self):
        OPERATION.commissions = {
            'some discount': 3,
            'other discount': 1,
            'negative discount': -1
        }
        self.assertEqual(OPERATION.total_commissions, 3)
