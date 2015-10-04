"""Tests for the Event base class."""

from __future__ import absolute_import
import unittest

import trade


class DummyEvent(trade.Event):
    """A dummy event for the tests."""

    def __init__(self, asset, date):
        super(DummyEvent, self).__init__(asset, date)

    def update_portfolio(self, quantity, price, results=None):
        return quantity, price


class TestBaseEventBehavior(unittest.TestCase):
    """Test the Event class and its default behavior.
    """

    def setUp(self):
        self.asset = trade.Asset()
        self.date = '2015-09-29'
        self.event = DummyEvent(asset=self.asset, date=self.date)

    def test_event_should_exist(self):
        self.assertTrue(self.event)

    def test_event_asset(self):
        self.assertEqual(self.event.asset, self.asset)

    def test_event_date(self):
        self.assertEqual(self.event.date, self.date)

    def test_event_update_portfolio(self):
        expected_return = (10, 1)
        self.assertEqual(
            self.event.update_portfolio(10, 1, {}),
            expected_return
        )


class TestBaseEventAccumulation(unittest.TestCase):
    """The the accumulation of an Event object by the Accumulator.
    """

    def setUp(self):
        self.asset = trade.Asset()
        self.date = '2015-09-29'
        self.accumulator = trade.Accumulator(self.asset)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}

    def test_check_initial_quantity(self):
        self.assertEqual(self.accumulator.quantity, 100)

    def test_check_initial_price(self):
        self.assertEqual(self.accumulator.price, 10)

    def test_check_initial_results(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})

    def test_check_quantity_after_event(self):
        event = DummyEvent(asset=self.asset, date=self.date)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.quantity, 100)

    def test_check_price_after_event(self):
        event = DummyEvent(asset=self.asset, date=self.date)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.price, 10)

    def test_check_results_after_event(self):
        event = DummyEvent(asset=self.asset, date=self.date)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.results, {'trades': 1200})


class TestAbstractEventCreation(unittest.TestCase):
    """The base Event should never be created."""

    def test_abstract_event_creation(self):
        """Creating a base Event should raise TypeError."""
        try:
            event = trade.Event(
                asset=trade.Asset(symbol='a'),
                date='2015-01-01'
            )
        except TypeError:
            pass
