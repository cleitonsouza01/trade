"""Tests logging of Event objects."""

from __future__ import absolute_import
from __future__ import division

import unittest

import trade
from trade import Accumulator, Asset
from trade.plugins import StockSplit


ASSET = Asset()


class DummyEvent(trade.plugins.Event):
    """A dummy event for the tests."""

    def update_container(self, operation):
        pass


class TestLogEvent(unittest.TestCase):

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}
        self.event = StockSplit(
            asset=ASSET,
            date='2015-09-24',
            factor=2
        )
        self.accumulator.accumulate_occurrence(self.event)


class TestLogEvent00(TestLogEvent):
    """Tests the logging of 1 Event object."""

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


class TestLogEvent01(TestLogEvent):
    """Tests the logging of 2 Event objects."""

    def setUp(self):
        super(TestLogEvent01, self).setUp()
        self.event1 = DummyEvent(
            ASSET,
            '2015-09-25',
            factor=1
        )
        self.accumulator.accumulate_occurrence(self.event1)

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
                'occurrences': [self.event]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)


class TestLogEvent02(TestLogEvent):
    """Tests the logging of multiple Event objects."""

    def setUp(self):
        super(TestLogEvent02, self).setUp()
        self.event1 = DummyEvent(
            ASSET,
            '2015-09-24',
            factor=1,
        )
        self.accumulator.accumulate_occurrence(self.event1)

    def test_log_position(self):
        expected_log = {
            'price': 5.0,
            'quantity': 200
        }
        self.assertEqual(
            self.accumulator.log['2015-09-24']['position'],
            expected_log
        )

    def test_log_occurrences(self):
        expected_log = [
            self.event,
            self.event1
        ]
        self.assertEqual(
            self.accumulator.log['2015-09-24']['occurrences'],
            expected_log
        )
