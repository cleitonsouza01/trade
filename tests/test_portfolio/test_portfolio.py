"""Base class for Portfolio tests."""

from __future__ import absolute_import
import copy
import unittest
import trade

class TestPortfolio(unittest.TestCase):
    """Base class for Portfolio tests."""

    operations = []
    state = {}

    def setUp(self):
        self.portfolio = trade.Portfolio()
        for operation in self.operations:
            self.portfolio.accumulate(copy.deepcopy(operation))

    def test_accumulators_quantities(self):
        """Test the quantity of each accumulator."""
        for asset, state in self.state.items():
            self.assertEqual(
                self.portfolio.subjects[asset].data['quantity'],
                state['quantity']
            )

    def test_accumulators_prices(self):
        """Test the price of each accumulator."""
        for asset, state in self.state.items():
            self.assertEqual(
                self.portfolio.subjects[asset].data['price'],
                state['price']
            )

    def test_keys(self):
        """Test the each accumulator key."""
        self.assertEqual(
            len(self.portfolio.subjects.keys()),
            len(self.state.keys())
        )
