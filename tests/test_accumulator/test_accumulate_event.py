"""Tests the method accumulate_occurrence() of the Accumulator."""

from __future__ import absolute_import
from __future__ import division

import unittest

import trade
import trade.plugins

from . fixture_operations import ASSET


class EventThatChangeResults(trade.plugins.Event):
    """A fictional event for the tests."""

    def update_container(self, container):
        """Increment all results in the container with the factor."""
        for key in container.results.keys():
            container.results[key] += self.factor


class TestEventThatChangeResultsCase00(unittest.TestCase):
    """Test the accumulation of an Event object.

    In this test we use the EventThatChangeResults object
    to test the consequences of an Event accumulation.
    """
    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}
        self.event = EventThatChangeResults(ASSET, '2015-09-27', 2)
        self.accumulator.accumulate_occurrence(self.event)

    def test_check_quantity_after_split(self):
        self.assertEqual(self.accumulator.quantity, 100)

    def test_check_price_after_split(self):
        self.assertEqual(self.accumulator.price, 10)

    def test_check_results_after_split(self):
        self.assertEqual(self.accumulator.results, {'trades': 1202})
