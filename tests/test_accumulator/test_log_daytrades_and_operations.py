from __future__ import absolute_import
import unittest

from trade import Accumulator as AssetAccumulator
from trade import Asset, Operation, Daytrade


class TestLogDaytradesAndOperations_Case_00(unittest.TestCase):

    def setUp(self):
        self.asset = Asset()
        self.accumulator = AssetAccumulator(self.asset, logging=True)

    def test_log_occurrences(self):
        daytrade = Daytrade(
                        date='2015-01-01',
                        asset=self.asset,
                        quantity=100,
                        purchase_price=10,
                        sale_price=20
                    )
        self.accumulator.accumulate_daytrade(daytrade)

        operation = Operation(100, 10, asset=self.asset, date='2015-01-01')
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


class TestLogDaytradesAndOperations_Case_01(unittest.TestCase):

    def setUp(self):
        self.asset = Asset()
        self.accumulator = AssetAccumulator(self.asset, logging=True)

    def test_log_occurrences(self):
        daytrade = Daytrade(
                        date='2015-01-01',
                        asset=self.asset,
                        quantity=100,
                        purchase_price=10,
                        sale_price=20
                    )
        self.accumulator.accumulate_daytrade(daytrade)

        operation = Operation(100, 10, asset=self.asset, date='2015-01-02')
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


class TestLogDaytradesAndOperations_Case_02(unittest.TestCase):

    def setUp(self):
        self.asset = Asset()
        self.accumulator = AssetAccumulator(self.asset, logging=True)

    def test_log_occurrences(self):
        daytrade = Daytrade(
                        date='2015-01-01',
                        asset=self.asset,
                        quantity=100,
                        purchase_price=10,
                        sale_price=20
                    )
        self.accumulator.accumulate_daytrade(daytrade)

        operation = Operation(
                        quantity=100,
                        price=10,
                        asset=self.asset,
                        date='2015-01-02'
                    )
        self.accumulator.accumulate_operation(operation)

        daytrade2 = Daytrade(
                        date='2015-01-02',
                        asset=self.asset,
                        quantity=100,
                        purchase_price=10,
                        sale_price=20
                    )
        self.accumulator.accumulate_daytrade(daytrade2)

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
