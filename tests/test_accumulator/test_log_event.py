from __future__ import absolute_import
from __future__ import division

import unittest

from trade import Accumulator, Event, Asset, StockSplit


class DummyEvent(Event):

    def __init__(self, date, asset):
        self.asset = asset
        self.date = date

    def update_portfolio(self, quantity, price, results):
        return quantity, price


class TestEvent_log_event_Case_00(unittest.TestCase):

    def setUp(self):
        self.asset = Asset()
        self.accumulator = Accumulator(self.asset, logging=True)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}

    def test_check_initial_quantity(self):
        self.assertEqual(self.accumulator.quantity, 100)

    def test_check_initial_price(self):
        self.assertEqual(self.accumulator.price, 10)

    def test_check_initial_results(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})

    def test_check_quantity_after_split(self):
        event = StockSplit(
                    asset=self.asset,
                    date='2015-09-24',
                    factor=2
                )
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.quantity, 200)

    def test_check_price_after_split(self):
        event = StockSplit(
                    asset=self.asset,
                    date='2015-09-24',
                    factor=2
                )
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.price, 5)

    def test_check_results_after_split(self):
        event = StockSplit(
                    asset=self.asset,
                    date='2015-09-24',
                    factor=2
                )
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.results, {'trades': 1200})

    def test_check_log_case_00(self):
        self.event = StockSplit(
                        asset=self.asset,
                        date='2015-09-24',
                        factor=2
                    )
        self.accumulator.accumulate_event(self.event)
        expected_log = {
            '2015-09-24': {
                'position': {
                    'price': 5.0,
                    'quantity': 200
                },
                'occurrences': [self.event]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_check_log_case_01(self):
        self.event0 = StockSplit(
                            asset=self.asset,
                            date='2015-09-24',
                            factor=2
                        )
        self.accumulator.accumulate_event(self.event0)
        self.event1 = DummyEvent('2015-09-25', self.asset)
        self.accumulator.accumulate_event(self.event1)
        expected_log = {
            '2015-09-25': {
                'position': {
                    'price': 5.0,
                    'quantity': 200
                },
                'occurrences': [self.event1]
            },
            '2015-09-24': {
                'position': {
                    'price': 5.0,
                    'quantity': 200
                },
                'occurrences': [self.event0]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_check_log_case_02(self):
        self.event0 = StockSplit(
                            asset=self.asset,
                            date='2015-09-24',
                            factor=2
                        )
        self.accumulator.accumulate_event(self.event0)
        self.event1 = DummyEvent('2015-09-24', self.asset)
        self.accumulator.accumulate_event(self.event1)
        expected_log = {
            '2015-09-24': {
                'position': {
                    'price': 5.0,
                    'quantity': 200
                },
                'occurrences': [
                    self.event0,
                    self.event1
                ]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)
