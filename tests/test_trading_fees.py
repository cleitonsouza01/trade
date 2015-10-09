"""Tests for the TradingFees base class."""

from __future__ import absolute_import
import unittest

import trade
from trade.plugins import TradingFees


class TestTaxManager(unittest.TestCase):
    """Test the default dummy tax manager.

    The default tax manager should return a empty dict
    for both daytrade and common operation rates.
    """
    def setUp(self):
        self.tax_manager = TradingFees

    def test_assert_tax_manager_exists(self):
        self.assertTrue(self.tax_manager)

    def test_get_rates_for_operation(self):
        operation = trade.Operation(
            subject=trade.Asset(),
            quantity=10,
            price=1,
            date='2015-09-25'
        )
        self.assertEqual(
            self.tax_manager.get_fees(operation, 'common operations'),
            {}
        )

    def test_get_rates_for_daytrade(self):
        asset = trade.Asset()
        operation_a = trade.Operation(
            subject=asset,
            quantity=100,
            price=10,
            date='2015-09-25'
        )
        operation_b = trade.Operation(
            subject=asset,
            quantity=-100,
            price=12,
            date='2015-09-25'
        )
        daytrade = trade.plugins.Daytrade(operation_a, operation_b)
        self.assertEqual(
            self.tax_manager.get_fees(daytrade, 'daytrades'),
            {}
        )
