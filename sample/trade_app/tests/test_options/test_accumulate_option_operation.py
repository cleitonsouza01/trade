"""Test the accumulation of operations with Option objects."""

from __future__ import absolute_import
import unittest
import copy
from accumulator import Accumulator

from fixtures.assets import OPTION1
from fixtures.operations import OPTION_OPERATION3


class TestAccumulateOption00(unittest.TestCase):
    """Accumulate a Option operation."""

    def setUp(self):
        self.operation = copy.deepcopy(OPTION_OPERATION3)
        self.accumulator = Accumulator(OPTION1)
        self.accumulator.accumulate(self.operation)

    def test_returned_result(self):
        """Check the results of the operation."""
        self.assertEqual(self.operation.results, {})

    def test_accumulator_price(self):
        """Check the cost of the option on the accumulator."""
        self.assertEqual(self.accumulator.state['price'], 10)

    def test_accumulator_quantity(self):
        """Check the quantity of the option on the accumulator."""
        self.assertEqual(self.accumulator.state['quantity'], 100)

    def test_accumulator_results(self):
        """Check the results of the option on the accumulator."""
        self.assertEqual(self.accumulator.state['results'], {})
