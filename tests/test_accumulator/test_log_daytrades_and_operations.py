from __future__ import absolute_import
import unittest

from trade import Accumulator as AssetAccumulator
from trade import Asset, Operation, Daytrade


# TODO document this
# TODO more tests


class TestLogDaytradesAndOperations_Case_00(unittest.TestCase):

    def setUp(self):
        self.accumulator = AssetAccumulator(Asset(), logging=True)

    def test_log_first_operation(self):
        daytrade = Daytrade('2015-01-01', Asset(), 100, 10, 20)
        self.accumulator.accumulate_daytrade(daytrade)

        operation = Operation(100, 10, asset=Asset(), date='2015-01-01')
        self.accumulator.accumulate_operation(operation)

        expected_log = {
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'operations': [daytrade, operation]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_log_keys(self):
        daytrade = Daytrade('2015-01-01', Asset(), 100, 10, 20)
        self.accumulator.accumulate_daytrade(daytrade)
        operation = Operation(100, 10, asset=Asset(), date='2015-01-01')
        self.accumulator.accumulate_operation(operation)
        self.assertEqual(list(self.accumulator.log), ['2015-01-01'])

    def test_returned_result_should_be_1000(self):
        operation = Operation(100, 10, asset=Asset(), date='2015-01-01')
        self.accumulator.accumulate_operation(operation)
        daytrade = Daytrade('2015-01-01', Asset(), 100, 10, 20)
        result = self.accumulator.accumulate_daytrade(daytrade)
        self.assertEqual(result, 1000)


class TestLogDaytradesAndOperations_Case_01(unittest.TestCase):

    def setUp(self):
        self.accumulator = AssetAccumulator(Asset(), logging=True)

    def test_log_first_operation(self):
        daytrade = Daytrade('2015-01-01', Asset(), 100, 10, 20)
        self.accumulator.accumulate_daytrade(daytrade)

        operation = Operation(100, 10, asset=Asset(), date='2015-01-02')
        self.accumulator.accumulate_operation(operation)

        expected_log = {
            '2015-01-02': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'operations': [operation]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 0,
                    'price': 0
                },
                'operations': [daytrade]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_returned_result_should_be_0(self):
        daytrade = Daytrade('2015-01-01', Asset(), 100, 10, 20)
        self.accumulator.accumulate_daytrade(daytrade)
        operation = Operation(100, 10, asset=Asset(), date='2015-01-02')
        result = self.accumulator.accumulate_operation(operation)
        self.assertEqual(result, {'trades':0})


class TestLogDaytradesAndOperations_Case_02(unittest.TestCase):

    def setUp(self):
        self.accumulator = AssetAccumulator(Asset(), logging=True)

    def test_log_first_operation(self):
        daytrade = Daytrade('2015-01-01', Asset(), 100, 10, 20)
        self.accumulator.accumulate_daytrade(daytrade)

        operation = Operation(100, 10, asset=Asset(), date='2015-01-02')
        self.accumulator.accumulate_operation(operation)

        daytrade2 = Daytrade('2015-01-02', Asset(), 100, 10, 20)
        self.accumulator.accumulate_daytrade(daytrade2)

        expected_log = {
            '2015-01-02': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'operations': [operation, daytrade2]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 0,
                    'price': 0
                },
                'operations': [daytrade]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_log_keys(self):
        daytrade = Daytrade('2015-01-01', Asset(), 100, 10, 20)
        self.accumulator.accumulate_daytrade(daytrade)
        self.assertEqual(list(self.accumulator.log), ['2015-01-01'])

    def test_returned_result_should_be_1000(self):
        daytrade = Daytrade('2015-01-01', Asset(), 100, 10, 20)
        result = self.accumulator.accumulate_daytrade(daytrade)
        self.assertEqual(result, 1000)
