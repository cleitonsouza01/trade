"""Tests for the Event base class."""

from __future__ import absolute_import
import unittest
from trade import Accumulator, Event
from tests.fixtures.assets import ASSET


class DummyEvent(Event):
    """A dummy event for the tests."""

    def __init__(self, asset, date, factor=1):
        super(DummyEvent, self).__init__(asset, date, factor)

    def update_accumulator(self, accumulator):
        pass


class TestBaseEventBehavior(unittest.TestCase):
    """Test the Event class and its default behavior."""

    def setUp(self):
        event = DummyEvent(asset=ASSET, date='2015-09-29')
        self.acc = Accumulator(ASSET)
        event.update_accumulator(self.acc)

    def test_event_update_quantity(self):
        self.assertEqual(
            self.acc.state['quantity'],
            0
        )

    def test_event_update_price(self):
        self.assertEqual(
            self.acc.state['price'],
            0
        )

    def test_event_update_results(self):
        self.assertFalse(self.acc.state['results'])


class TestBaseEventAccumulation(unittest.TestCase):
    """The the accumulation of an Event object by the Accumulator."""

    def setUp(self):
        self.acc = Accumulator(ASSET)
        self.acc.state['quantity'] = 100
        self.acc.state['price'] = 10
        self.acc.state['results'] = {'trades': 1200}
        event = DummyEvent(asset=ASSET, date='2015-09-29')
        self.acc.accumulate(event)

    def test_quantity_after_event(self):
        self.assertEqual(self.acc.state['quantity'], 100)

    def test_price_after_event(self):
        self.assertEqual(self.acc.state['price'], 10)

    def test_results_after_event(self):
        self.assertEqual(self.acc.state['results'], {'trades': 1200})
