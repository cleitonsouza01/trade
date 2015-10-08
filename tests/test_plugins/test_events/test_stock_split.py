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
        self.accumulator.data['quantity'] = 100
        self.accumulator.data['price'] = 10
        self.accumulator.data['results'] = {'trades': 1200}
        self.event = StockSplit(
            asset=asset,
            date='2015-09-24',
            factor=2
        )
        self.accumulator.accumulate(self.event)

    def test_check_quantity_after_split(self):
        self.assertEqual(self.accumulator.data['quantity'], 200)

    def test_check_price_after_split(self):
        self.assertEqual(self.accumulator.data['price'], 5)

    def test_check_results_after_split(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 1200})

    def test_check_log_case_00(self):
        expected_log = {
            '2015-09-24': {
                'data': {
                    'price': 5.0,
                    'quantity': 200,
                    'results': {'trades': 1200}
                },
                'occurrences': [self.event]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)
