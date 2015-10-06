"""Tests the logging of Daytrade objects."""

from __future__ import absolute_import
import unittest

import trade


ASSET = trade.Asset()
OPERATION_A = trade.Operation(
    asset=ASSET,
    quantity=100,
    price=10,
    date='2015-01-01'
)
OPERATION_B = trade.Operation(
    asset=ASSET,
    quantity=-100,
    price=20,
    date='2015-01-01'
)
DAYTRADE = trade.plugins.Daytrade(OPERATION_A, OPERATION_B)


class TestLogDaytrade(unittest.TestCase):
    """Test the logging of a Daytrade object."""

    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(DAYTRADE)

    def test_log_first_operation(self):
        expected_log = {
            '2015-01-01': {
                'position': {
                    'quantity': 0,
                    'price': 0
                },
                'occurrences': [DAYTRADE]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_log_keys(self):
        self.assertEqual(list(self.accumulator.log), ['2015-01-01'])

    def test_returned_result(self):
        self.assertEqual(DAYTRADE.results, {'daytrades':1000})
