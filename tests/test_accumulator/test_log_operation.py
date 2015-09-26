from __future__ import absolute_import
import unittest

from trade import Accumulator as AssetAccumulator
from trade import Asset, Operation


# TODO document this
# TODO more tests


class TestLogOperation(unittest.TestCase):

    def setUp(self):
        self.accumulator = AssetAccumulator(Asset(), logging=True)

    def test_log_first_operation(self):
        operation = Operation(100, 10, asset=Asset(), date='2015-01-01')
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
        operation = Operation(100, 10, asset=Asset(), date='2015-01-01')
        self.accumulator.accumulate_operation(operation)
        self.assertEqual(list(self.accumulator.log), ['2015-01-01'])

    def test_returned_result_should(self):
        operation = Operation(100, 10, asset=Asset(), date='2015-01-01')
        result = self.accumulator.accumulate_operation(operation)
        self.assertEqual(result, {'trades': 0})
