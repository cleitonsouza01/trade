"""Tests the method accumulate() of the Accumulator."""

from __future__ import absolute_import
from __future__ import division

import unittest

import trade
import trade.plugins

from tests.fixtures.operations import ASSET


class EventThatChangeResults(trade.plugins.Event):
    """A fictional event for the tests."""

    def update_accumulator(self, accumulator):
        """Increment all results in the container with the factor."""
        for key in accumulator.data['results'].keys():
            accumulator.data['results'][key] += self.factor


class TestEventThatChangeResultsCase00(unittest.TestCase):
    """Test the accumulation of an Event object.

    In this test we use the EventThatChangeResults object
    to test the consequences of an Event accumulation.
    """
    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET)
        self.accumulator.data['quantity'] = 100
        self.accumulator.data['price'] = 10
        self.accumulator.data['results'] = {'trades': 1200}
        self.event = EventThatChangeResults(ASSET, '2015-09-27', 2)
        self.accumulator.accumulate(self.event)

    def test_check_quantity_after_split(self):
        self.assertEqual(self.accumulator.data['quantity'], 100)

    def test_check_price_after_split(self):
        self.assertEqual(self.accumulator.data['price'], 10)

    def test_check_results_after_split(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 1202})
