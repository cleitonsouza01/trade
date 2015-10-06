"""Tests for StockSplit events."""

from __future__ import absolute_import
import unittest

import trade
from trade.plugins import StockSplit


class TestStockSplitCase00(unittest.TestCase):
    """Test a StockSplit effect on the Accumulator."""

    def setUp(self):
        asset = trade.Asset()
        self.accumulator = trade.Accumulator(asset, logging=True)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}
        self.event = StockSplit(
            asset=asset,
            date='2015-09-24',
            factor=2
        )
        self.accumulator.accumulate_occurrence(self.event)

    def test_check_quantity_after_split(self):
        self.assertEqual(self.accumulator.quantity, 200)

    def test_check_price_after_split(self):
        self.assertEqual(self.accumulator.price, 5)

    def test_check_results_after_split(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})

    def test_check_log_case_00(self):
        expected_log = {
            '2015-09-24': {
                'position': {
                    'price': 5.0,
                    'quantity': 200
                },
                'occurrences': [self.event]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)
