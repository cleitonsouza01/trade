from __future__ import absolute_import
from __future__ import division

import unittest

from trade import Accumulator, Event


# TODO document this
# TODO more tests


class StockSplit(Event):

    def __init__(self, name, factor):
        self.factor = factor
        self.name = name

    def update_portfolio(self, quantity, price, results):
        quantity = quantity * self.factor
        price = price / self.factor
        return quantity, price


class EventThatChangeResults(Event):

    def __init__(self, name, some_value):
        self.something = some_value
        self.name = name

    def update_portfolio(self, quantity, price, results):
        for key in results.keys():
            results[key] += self.something
        return quantity, price


class TestEvent_AssetSplit_case_00(unittest.TestCase):

    def setUp(self):
        self.accumulator = Accumulator('Some asset')
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
        event = StockSplit('stock split', 2)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.quantity, 200)

    def test_check_price_after_split(self):
        event = StockSplit('stock split', 2)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.price, 5)

    def test_check_quantity_after_split(self):
        event = StockSplit('stock split', 2)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.results, {'trades': 1200})


class TestEvent_EventThatChangeResults_case_00(unittest.TestCase):

    def setUp(self):
        self.accumulator = Accumulator('Some asset')
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
        event = EventThatChangeResults('some event', 2)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.quantity, 100)

    def test_check_price_after_split(self):
        event = EventThatChangeResults('some event',2)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.price, 10)

    def test_check_quantity_after_split(self):
        event = EventThatChangeResults('some event',2)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.results, {'trades': 1202})
