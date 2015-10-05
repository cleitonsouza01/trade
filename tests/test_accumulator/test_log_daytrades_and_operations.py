"""Tests the logging of Operation and Daytrade objects."""

from __future__ import absolute_import
import unittest

import trade


class TestLogDaytradesAndOperationsCase00(unittest.TestCase):
    """Tests the logging of Operation and Daytrade objects.

    Try to log a daytrade and a operation on the same date.
    """

    def setUp(self):
        self.asset = trade.Asset()
        self.accumulator = trade.Accumulator(self.asset, logging=True)

    def test_log_occurrences(self):
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

        operation = trade.Operation(
            quantity=100,
            price=10,
            asset=self.asset,
            date='2015-01-01'
        )
        self.accumulator.accumulate_operation(operation)

        expected_log = {
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [daytrade, operation]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)


class TestLogDaytradesAndOperationsCase01(unittest.TestCase):
    """Tests the logging of Operation and Daytrade objects.

    Logs one daytrade and then one operation on a posterior
    date.
    """

    def setUp(self):
        self.asset = trade.Asset()
        self.accumulator = trade.Accumulator(self.asset, logging=True)

    def test_log_occurrences(self):
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

        operation = trade.Operation(
            quantity=100,
            price=10,
            asset=self.asset,
            date='2015-01-02'
        )
        self.accumulator.accumulate_operation(operation)

        expected_log = {
            '2015-01-02': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [operation]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 0,
                    'price': 0
                },
                'occurrences': [daytrade]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)


class TestLogDaytradesAndOperationsCase02(unittest.TestCase):
    """Tests the logging of Operation and Daytrade objects.

    One daytrade first,
    then one operation and one daytrade on a posterior date.
    """

    def setUp(self):
        self.asset = trade.Asset()
        self.accumulator = trade.Accumulator(self.asset, logging=True)

    def test_log_occurrences(self):
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

        operation = trade.Operation(
            quantity=100,
            price=10,
            asset=self.asset,
            date='2015-01-02'
        )
        self.accumulator.accumulate_operation(operation)

        asset = trade.Asset()
        operation_a = trade.Operation(
            asset=asset,
            quantity=100,
            price=10,
            date='2015-01-02'
        )
        operation_b = trade.Operation(
            asset=asset,
            quantity=-100,
            price=20,
            date='2015-01-02'
        )
        daytrade2 = trade.plugins.Daytrade(operation_a, operation_b)
        self.accumulator.accumulate_operation(daytrade2)

        expected_log = {
            '2015-01-02': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [operation, daytrade2]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 0,
                    'price': 0
                },
                'occurrences': [daytrade]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)
