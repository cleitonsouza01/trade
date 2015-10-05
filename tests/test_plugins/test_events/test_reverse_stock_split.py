"""Tests for ReverseStockSplit events."""

from __future__ import absolute_import
import unittest

import trade


class TestReverseStockSplitCase00(unittest.TestCase):
    """Test the accumulation of a ReverseStockSplit event."""

    def setUp(self):
        asset = trade.Asset()
        self.accumulator = trade.Accumulator(asset, logging=True)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}
        #event = trade.plugins.ReverseStockSplit(
        event = trade.plugins.StockSplit(
            asset=asset,
            date='2015-09-24',
            factor=0.5
        )
        self.accumulator.accumulate_event(event)

    def test_check_quantity_after_split(self):
        self.assertEqual(self.accumulator.quantity, 50)

    def test_check_price_after_split(self):
        self.assertEqual(self.accumulator.price, 20)

    def test_check_results_after_split(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})
