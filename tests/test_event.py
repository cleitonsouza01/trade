"""Tests for the Event base class."""

from __future__ import absolute_import
import unittest

import trade


class DummyEvent(trade.plugins.Event):
    """A dummy event for the tests."""

    def __init__(self, asset, date, factor=1):
        super(DummyEvent, self).__init__(asset, date, factor)

    def update_container(self, container):
        pass


class TestBaseEventBehavior(unittest.TestCase):
    """Test the Event class and its default behavior.
    """

    def setUp(self):
        asset = trade.Asset()
        date = '2015-09-29'
        event = DummyEvent(asset=asset, date=date)
        self.accumulator = trade.Accumulator()
        event.update_container(self.accumulator)

    def test_event_update_quantity(self):
        self.assertEqual(
            self.accumulator.quantity,
            0
        )

    def test_event_update_price(self):
        self.assertEqual(
            self.accumulator.price,
            0
        )

    def test_event_update_results(self):
        self.assertFalse(self.accumulator.results)


class TestBaseEventAccumulation(unittest.TestCase):
    """The the accumulation of an Event object by the Accumulator.
    """

    def setUp(self):
        asset = trade.Asset()
        date = '2015-09-29'
        self.accumulator = trade.Accumulator(asset)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}
        event = DummyEvent(asset=asset, date=date)
        self.accumulator.accumulate(event)

    def test_quantity_after_event(self):
        self.assertEqual(self.accumulator.quantity, 100)

    def test_price_after_event(self):
        self.assertEqual(self.accumulator.price, 10)

    def test_results_after_event(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})
