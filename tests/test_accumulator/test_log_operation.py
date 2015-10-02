from __future__ import absolute_import
import unittest

from trade import Accumulator
from trade import Asset, Operation


class TestLogOperation(unittest.TestCase):

    def setUp(self):
        self.asset = Asset()
        self.accumulator = Accumulator(self.asset, logging=True)

    def test_log_first_operation(self):
        operation = Operation(
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
                'occurrences': [operation]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_log_keys(self):
        operation = Operation(
                        quantity=100,
                        price=10,
                        asset=self.asset,
                        date='2015-01-01'
                    )
        self.accumulator.accumulate_operation(operation)
        self.assertEqual(list(self.accumulator.log), ['2015-01-01'])

    def test_returned_result(self):
        operation = Operation(
                        quantity=100,
                        price=10,
                        asset=self.asset,
                        date='2015-01-01'
                    )
        result = self.accumulator.accumulate_operation(operation)
        self.assertEqual(result, {'trades': 0})
