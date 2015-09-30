from __future__ import absolute_import
import unittest

from trade import Accumulator as AssetAccumulator
from trade import Asset, Daytrade


class TestLogDaytrade(unittest.TestCase):

    def setUp(self):
        self.asset = Asset()
        self.accumulator = AssetAccumulator(self.asset, logging=True)

    def test_log_first_operation(self):
        daytrade = Daytrade(
                        date='2015-01-01',
                        asset=self.asset,
                        quantity=100,
                        purchase_price=10,
                        sale_price=20
                    )
        #self.accumulator.accumulate_daytrade(daytrade)
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
        daytrade = Daytrade(
                        date='2015-01-01',
                        asset=self.asset,
                        quantity=100,
                        purchase_price=10,
                        sale_price=20
                    )
        #self.accumulator.accumulate_daytrade(daytrade)
        self.accumulator.accumulate_operation(daytrade)
        self.assertEqual(list(self.accumulator.log), ['2015-01-01'])

    def test_returned_result_should_be_1000(self):
        daytrade = Daytrade('2015-01-01', self.asset, 100, 10, 20)
        #result = self.accumulator.accumulate_daytrade(daytrade)
        result = self.accumulator.accumulate_operation(daytrade)
        self.assertEqual(result, {'daytrades':1000})
