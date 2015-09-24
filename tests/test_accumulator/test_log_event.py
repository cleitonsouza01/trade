from __future__ import absolute_import
from __future__ import division

import unittest

from trade import Accumulator, Event


# TODO document this
# TODO more tests


class StockSplit(Event):

    def __init__(self, date, name,  factor):
        self.factor = factor
        self.name = name
        self.date = date

    def update_portfolio(self, quantity, price, results):
        quantity = quantity * self.factor
        price = price / self.factor
        return quantity, price


class DummyEvent(Event):

    def __init__(self, date, name):
        self.name = name
        self.date = date

    def update_portfolio(self, quantity, price, results):
        return quantity, price


class TestEvent_log_event_Case_00(unittest.TestCase):

    def setUp(self):
        self.accumulator = Accumulator('Some asset', logging=True)
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
        event = StockSplit('2015-09-24', 'stock split', 2)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.quantity, 200)

    def test_check_price_after_split(self):
        event = StockSplit('2015-09-24', 'stock split', 2)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.price, 5)

    def test_check_quantity_after_split(self):
        event = StockSplit('2015-09-24', 'stock split', 2)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.results, {'trades': 1200})

    def test_check_log_case_00(self):
        event = StockSplit('2015-09-24', 'stock split', 2)
        self.accumulator.accumulate_event(event)
        expected_log = {
            '2015-09-24': {
                'position': {
                    'price': 5.0,
                    'quantity': 200
                },
                'events': [
                    {
                        'name': 'stock split',
                        'factor': 2,
                        'date': '2015-09-24'
                    }
                ]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_check_log_case_01(self):
        event = StockSplit('2015-09-24', 'stock split', 2)
        self.accumulator.accumulate_event(event)
        event = DummyEvent('2015-09-25', 'other event')
        self.accumulator.accumulate_event(event)
        expected_log = {
            '2015-09-25': {
                'position': {
                    'price': 5.0,
                    'quantity': 200
                },
                'events': [
                    {
                        'name': 'other event',
                        'date': '2015-09-25'
                    }
                ]
            },
            '2015-09-24': {
                'position': {
                    'price': 5.0,
                    'quantity': 200
                },
                'events': [
                    {
                        'name': 'stock split',
                        'factor': 2,
                        'date': '2015-09-24'
                    }
                ]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_check_log_case_02(self):
        event = StockSplit('2015-09-24', 'stock split', 2)
        self.accumulator.accumulate_event(event)
        event = DummyEvent('2015-09-24', 'other event')
        self.accumulator.accumulate_event(event)
        expected_log = {
            '2015-09-24': {
                'position': {
                    'price': 5.0,
                    'quantity': 200
                },
                'events': [
                    {
                        'name': 'stock split',
                        'factor': 2,
                        'date': '2015-09-24'
                    },
                    {
                        'name': 'other event',
                        'date': '2015-09-24'
                    }
                ]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)
