from __future__ import absolute_import
import unittest

from trade import Accumulator as AssetAccumulator
from trade import Asset, Daytrade


# TODO document this
# TODO more tests


class TestLogDaytrade(unittest.TestCase):

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', logging=True)

    def test_log_first_operation(self):
        daytrade = Daytrade('2015-01-01', Asset(), 100, 10, 20)
        self.accumulator.accumulate_daytrade(daytrade)
        expected_log = {
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
