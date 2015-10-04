"""Tests the logging of Daytrade objects."""

from __future__ import absolute_import
import unittest

import trade


class TestLogDaytrade(unittest.TestCase):
    """Test the logging of a Daytrade object."""

    def setUp(self):
        self.asset = trade.Asset()
        self.accumulator = trade.Accumulator(self.asset, logging=True)

    def test_log_first_operation(self):
        daytrade = trade.plugins.Daytrade(
            date='2015-01-01',
            asset=self.asset,
            quantity=100,
            purchase_price=10,
            sale_price=20
        )
        self.accumulator.accumulate_operation(daytrade)
        expected_log = {
            '2015-01-01': {
                'position': {
                    'quantity': 0,
                    'price': 0
                },
                'occurrences': [daytrade]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_log_keys(self):
        daytrade = trade.plugins.Daytrade(
            date='2015-01-01',
            asset=self.asset,
            quantity=100,
            purchase_price=10,
            sale_price=20,
        )
        self.accumulator.accumulate_operation(daytrade)
        self.assertEqual(list(self.accumulator.log), ['2015-01-01'])

    def test_returned_result_should_be_1000(self):
        daytrade = trade.plugins.Daytrade(
            date='2015-01-01',
            asset=self.asset,
            quantity=100,
            purchase_price=10,
            sale_price=20
        )
        result = self.accumulator.accumulate_operation(daytrade)
        self.assertEqual(result, {'daytrades':1000})
