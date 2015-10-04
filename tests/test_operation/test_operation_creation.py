"""Tests the creation of Operation objects."""

from __future__ import absolute_import
from __future__ import division
import unittest

import trade


class TestOperationCreation(unittest.TestCase):
    """Test the creation of Operation objects."""

    def setUp(self):
        self.asset = trade.Asset(name='some asset')
        self.operation = trade.Operation(
            date='2015-09-18',
            asset=self.asset,
            quantity=20,
            price=10,
            commissions={
                'some discount': 3
            }
        )

    def test_trade_exists(self):
        self.assertTrue(self.operation)

    def test_trade_asset(self):
        self.assertEqual(self.operation.asset, self.asset)

    def test_trade_date_should_be_2015_09_18(self):
        self.assertEqual(self.operation.date, '2015-09-18')

    def test_trade_quantity_should_be_20(self):
        self.assertEqual(self.operation.quantity, 20)

    def test_trade_price_should_be_10(self):
        self.assertEqual(self.operation.price, 10)

    def test_trade_discounts_dict(self):
        discounts={
            'some discount': 3
        }
        self.assertEqual(self.operation.commissions, discounts)
