"""Tests logging of Event objects."""

from __future__ import absolute_import
from __future__ import division

import unittest

from trade import Accumulator, Asset, Event


class DummyEvent(Event):
    """A dummy event for the tests."""

    def __init__(self, asset, date):
        super(DummyEvent, self).__init__(asset, date)

    def update_portfolio(self, quantity, price, results):
        return quantity, price


class StockSplit(Event):
    """A stock split event for the tests."""

    def __init__(self, asset, date, factor):
        super(StockSplit, self).__init__(asset, date)
        self.factor = factor

    def update_portfolio(self, quantity, price, results):
        quantity = quantity * self.factor
        price = price / self.factor
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
        self.event1 = DummyEvent(
            self.asset,
            '2015-09-25'
        )
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
        self.event1 = DummyEvent(
            self.asset,
            '2015-09-24'
        )
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
