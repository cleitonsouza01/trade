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
        asset = trade.Asset()
        operation_a = trade.Operation(
            asset=asset,
            quantity=100,
            price=10,
            date='2015-01-01'
        )
        operation_b = trade.Operation(
            asset=asset,
            quantity=-100,
            price=20,
            date='2015-01-01'
        )
        daytrade = trade.plugins.Daytrade(operation_a, operation_b)
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
        asset = trade.Asset()
        operation_a = trade.Operation(
            asset=asset,
            quantity=100,
            price=10,
            date='2015-01-01'
        )
        operation_b = trade.Operation(
            asset=asset,
            quantity=-100,
            price=20,
            date='2015-01-01'
        )
        daytrade = trade.plugins.Daytrade(operation_a, operation_b)
        self.accumulator.accumulate_operation(daytrade)
        self.assertEqual(list(self.accumulator.log), ['2015-01-01'])

    def test_returned_result(self):
        asset = trade.Asset()
        operation_a = trade.Operation(
            asset=asset,
            quantity=100,
            price=10,
            date='2015-01-01'
        )
        operation_b = trade.Operation(
            asset=asset,
            quantity=-100,
            price=20,
            date='2015-01-01'
        )
        daytrade = trade.plugins.Daytrade(operation_a, operation_b)
        result = self.accumulator.accumulate_operation(daytrade)
        self.assertEqual(result, {'daytrades':1000})
