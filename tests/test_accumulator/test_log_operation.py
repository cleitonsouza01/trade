from __future__ import absolute_import
import unittest

from trade import Accumulator as AssetAccumulator


# TODO document this
# TODO more tests


class TestLogOperation(unittest.TestCase):

    #maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', logging=True)

    def test_log_first_operation(self):
        self.accumulator.accumulate(100, 10, date='2015-01-01')
        expected_log = {
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'operations': [
                    {
                        'quantity': 100,
                        'price': 10,
                        'results': {'trades': 0}
                    }
                ]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_log_keys(self):
        self.accumulator.accumulate(100, 10, date='2015-01-01')
        #self.assertEqual(self.accumulator.log.keys(), ['2015-01-01'])
        self.assertEqual(list(self.accumulator.log), ['2015-01-01'])
