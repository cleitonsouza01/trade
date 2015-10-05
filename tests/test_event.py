"""Tests for the Event base class."""

from __future__ import absolute_import
import unittest

import trade


class DummyEvent(trade.Event):
    """A dummy event for the tests."""

    def __init__(self, asset, date):
        super(DummyEvent, self).__init__(asset, date)

    def update_container(self, container):
        pass


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

    def test_event_update_quantity(self):
        accumulator = trade.Accumulator()
        self.event.update_container(accumulator)
        self.assertEqual(
            accumulator.quantity,
            0
        )

    def test_event_update_price(self):
        accumulator = trade.Accumulator()
        self.event.update_container(accumulator)
        self.assertEqual(
            accumulator.price,
            0
        )

    def test_event_update_results(self):
        accumulator = trade.Accumulator()
        self.event.update_container(accumulator)
        self.assertFalse(accumulator.results)


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

    def test_initial_quantity(self):
        self.assertEqual(self.accumulator.quantity, 100)

    def test_initial_price(self):
        self.assertEqual(self.accumulator.price, 10)

    def test_initial_results(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})

    def test_quantity_after_event(self):
        event = DummyEvent(asset=self.asset, date=self.date)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.quantity, 100)

    def test_price_after_event(self):
        event = DummyEvent(asset=self.asset, date=self.date)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.price, 10)

    def test_results_after_event(self):
        event = DummyEvent(asset=self.asset, date=self.date)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.results, {'trades': 1200})
