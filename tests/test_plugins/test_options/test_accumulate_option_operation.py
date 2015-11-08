"""Test the accumulation of operations with Option objects."""

from __future__ import absolute_import
import unittest
import copy

import trade

from tests.fixtures.assets import OPTION1
from tests.fixtures.operations import OPTION_OPERATION3


class TestAccumulateOption00(unittest.TestCase):
    """Accumulate a Option operation."""

    def setUp(self):
        self.operation = copy.deepcopy(OPTION_OPERATION3)
        self.accumulator = trade.Accumulator(OPTION1)
        self.accumulator.accumulate(self.operation)

    def test_returned_result(self):
        self.assertEqual(self.operation.results, {})

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.state['price'], 10)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.state['quantity'], 100)

    def test_accumulator_results(self):
        self.assertEqual(self.accumulator.state['results'], {})
