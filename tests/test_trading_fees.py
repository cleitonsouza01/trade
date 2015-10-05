"""Tests for the TradingFees base class."""

from __future__ import absolute_import
import unittest

import trade


class TestTaxManager(unittest.TestCase):
    """Test the default dummy tax manager.

    The default tax manager should return a empty dict
    for both daytrade and common operation rates.
    """
    def setUp(self):
        self.tax_manager = trade.TradingFees

    def test_assert_tax_manager_exists(self):
        self.assertTrue(self.tax_manager)

    def test_get_rates_for_operation(self):
        operation = trade.Operation(
            asset=trade.Asset(),
            quantity=10,
            price=1,
            date='2015-09-25'
        )
        self.assertEqual(
            self.tax_manager.get_fees(operation, 'common operations'),
            {}
        )

    def test_get_rates_for_daytrade(self):
        daytrade = trade.plugins.Daytrade(
            date='2015-09-25',
            asset=trade.Asset(),
            quantity=100,
            purchase_price=10,
            sale_price=20
        )
        self.assertEqual(
            self.tax_manager.get_fees(daytrade, 'daytrades'),
            {}
        )
