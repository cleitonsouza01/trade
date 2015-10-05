"""Tests logging of Event objects."""

from __future__ import absolute_import
from __future__ import division

import unittest

from trade import Accumulator, Asset, Event


class DummyEvent(Event):
    """A dummy event for the tests."""

    def __init__(self, asset, date):
        super(DummyEvent, self).__init__(asset, date)

    def update_portfolio(self, operation):
        pass


class StockSplit(Event):
    """A stock split event for the tests."""

    def __init__(self, asset, date, factor):
        super(StockSplit, self).__init__(asset, date)
        self.factor = factor

    def update_portfolio(self, container):
        container.quantity = container.quantity * self.factor
        container.price = container.price / self.factor


class TestLogEvent00(unittest.TestCase):

    def setUp(self):
        self.asset = Asset()
        self.accumulator = Accumulator(self.asset, logging=True)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}
        self.event = StockSplit(
            asset=self.asset,
            date='2015-09-24',
            factor=2
        )
        self.accumulator.accumulate_event(self.event)

    def test_check_quantity_after_split(self):
        self.assertEqual(self.accumulator.quantity, 200)

    def test_check_price_after_split(self):
        self.assertEqual(self.accumulator.price, 5)

    def test_check_results_after_split(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})

    def test_check_log_case_00(self):
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


class TestLogEvent01(unittest.TestCase):

    def setUp(self):
        self.asset = Asset()
        self.accumulator = Accumulator(self.asset, logging=True)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}
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

    def test_check_log_case_01(self):
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


class TestLogEvent02(unittest.TestCase):

    def setUp(self):
        self.asset = Asset()
        self.accumulator = Accumulator(self.asset, logging=True)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}
        self.event0 = StockSplit(
            asset=self.asset,
            date='2015-09-25',
            factor=2
        )
        self.accumulator.accumulate_event(self.event0)
        self.event1 = DummyEvent(
            self.asset,
            '2015-09-25'
        )
        self.accumulator.accumulate_event(self.event1)

    def test_log_position(self):
        expected_log = {
            'price': 5.0,
            'quantity': 200
        }
        self.assertEqual(
            self.accumulator.log['2015-09-25']['position'],
            expected_log
        )

    def test_log_occurrences(self):
        expected_log = [
            self.event0,
            self.event1
        ]
        self.assertEqual(
            self.accumulator.log['2015-09-25']['occurrences'],
            expected_log
        )
