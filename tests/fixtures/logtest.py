"""Base class for Accumulator tests."""

from __future__ import absolute_import

import unittest

import trade
from tests.fixtures.assets import ASSET

class LogTest(unittest.TestCase):
    """Base class for Accumulator tests."""

    maxDiff = None
    initial_state = None
    occurrences = []
    expected_log = {}
    expected_state = {
        'quantity': 0,
        'price': 0,
        'results': {},
    }

    def setUp(self):
        """Creates an accumulator and accumulates all occurrences."""
        self.accumulator = trade.Accumulator(
            ASSET,
            state=self.initial_state,
            logging=True
        )
        self.accumulate_occurrences()

    def accumulate_occurrences(self):
        """Accumulates all occurrences defined in the test case."""
        for occurrence in self.occurrences:
            self.accumulator.accumulate(occurrence)

    def test_log(self):
        """Test the log for the defined occurrences."""
        if self.expected_log:
            self.assertEqual(self.accumulator.log, self.expected_log)

    def test_accumulator_state(self):
        """Verifies the state of the accumulator data."""
        for key in self.accumulator.state.keys():
            self.assertEqual(
                self.accumulator.state[key], self.expected_state[key]
            )
