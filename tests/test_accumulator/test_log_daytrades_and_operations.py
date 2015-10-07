"""Tests the logging of Operation and Daytrade objects."""

from __future__ import absolute_import
import unittest

import trade

from . fixture_operations import ASSET, OPERATION1, OPERATION18


DAYTRADE = trade.plugins.Daytrade(
    trade.Operation(
        asset=ASSET,
        quantity=100,
        price=10,
        date='2015-01-01'
    ),
    trade.Operation(
        asset=ASSET,
        quantity=-100,
        price=20,
        date='2015-01-01'
    )
)

DAYTRADE2 = trade.plugins.Daytrade(
    trade.Operation(
        asset=ASSET,
        quantity=100,
        price=10,
        date='2015-01-02'
    ),
    trade.Operation(
        asset=ASSET,
        quantity=-100,
        price=20,
        date='2015-01-02'
    )
)


class TestLogDaytradesAndOperations(unittest.TestCase):

    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET, logging=True)


class TestLogDaytradesAndOperationsCase00(TestLogDaytradesAndOperations):
    """Tests the logging of Operation and Daytrade objects.

    Try to log a daytrade and a operation on the same date.
    """

    def test_log_occurrences(self):
        self.accumulator.accumulate_occurrence(DAYTRADE)
        self.accumulator.accumulate_occurrence(OPERATION18)
        expected_log = {
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [DAYTRADE, OPERATION18]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)


class TestLogDaytradesAndOperationsCase01(TestLogDaytradesAndOperations):
    """Tests the logging of Operation and Daytrade objects.

    Logs one daytrade and then one operation on a posterior
    date.
    """

    def test_log_occurrences(self):
        self.accumulator.accumulate_occurrence(DAYTRADE)
        self.accumulator.accumulate_occurrence(OPERATION1)
        expected_log = {
            '2015-01-02': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [OPERATION1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 0,
                    'price': 0
                },
                'occurrences': [DAYTRADE]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)


class TestLogDaytradesAndOperationsCase02(TestLogDaytradesAndOperations):
    """Tests the logging of Operation and Daytrade objects.

    One daytrade first,
    then one operation and one daytrade on a posterior date.
    """

    def test_log_occurrences(self):
        self.accumulator.accumulate_occurrence(DAYTRADE)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(DAYTRADE2)
        expected_log = {
            '2015-01-02': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [OPERATION1, DAYTRADE2]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 0,
                    'price': 0
                },
                'occurrences': [DAYTRADE]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)
