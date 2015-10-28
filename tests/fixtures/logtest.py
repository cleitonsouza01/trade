"""Base class for Accumulator tests."""

from __future__ import absolute_import

import unittest
import copy

import trade
from tests.fixtures.assets import ASSET

class LogTest(unittest.TestCase):
    """Base class for Accumulator tests."""

    maxDiff = None
    initial_state = {}
    occurrences = []
    expected_log = {}
    expected_state = {
        'quantity': 0,
        'price': 0,
        'results': {},
    }

    def setUp(self):
        """Creates an accumulator and accumulates all occurrences."""
        self.accumulator = trade.Accumulator(ASSET, logging=True)
        if self.initial_state:
            self.accumulator.data = copy.deepcopy(self.initial_state)
        self.accumulate_occurrences()

    def accumulate_occurrences(self):
        """Accumulates all occurrences defined in the test case."""
        for occurrence in self.occurrences:
            self.accumulator.accumulate(occurrence)

    def test_purchase_result_log(self):
        """Test the log for the defined occurrences."""
        if self.expected_log:
            self.assertEqual(self.accumulator.log, self.expected_log)

    def test_accumulated_result(self):
        """Test the results for the defined occurrences."""
        self.assertEqual(
            self.accumulator.data['results'], self.expected_state['results'])

    def test_current_quantity(self):
        """Test the quantity for the defined occurrences."""
        self.assertEqual(
            self.accumulator.data['quantity'], self.expected_state['quantity'])

    def test_current_price(self):
        """Test the price for the defined occurrences."""
        self.assertEqual(
            round(self.accumulator.data['price'], 2), self.expected_state['price'])
