"""Base class for Portfolio tests."""

from __future__ import absolute_import
import copy
import unittest
import accumulator

class TestPortfolio(unittest.TestCase):
    """Base class for Portfolio tests."""

    initial_state = None
    operations = []
    state = {}

    def setUp(self):
        self.portfolio = accumulator.Portfolio(state=self.initial_state)
        for operation in self.operations:
            self.portfolio.accumulate(copy.deepcopy(operation))

    def test_accumulators_states(self):
        """Test the state of each accumulator."""
        for asset, state in self.state.items():
            for key in state.keys():
                self.assertEqual(
                    self.portfolio.subjects[asset].state[key],
                    state[key]
                )

    def test_keys(self):
        """Test the each accumulator key."""
        self.assertEqual(
            len(self.portfolio.subjects.keys()),
            len(self.state.keys())
        )
