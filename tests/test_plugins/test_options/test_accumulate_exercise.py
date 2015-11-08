"""Test the accumulation of Exercise operations."""

from __future__ import absolute_import
import unittest
import copy

import trade

from tests.fixtures.assets import ASSET, OPTION1
from tests.fixtures.operations import (
    OPTION_OPERATION3, EXERCISE_OPERATION5, OPERATION54,
    EXERCISE_OPERATION5
)


class TestAccumulateExercise(unittest.TestCase):
    """Base class for Exercise accumulation tests."""

    def setUp(self):
        self.option_accumulator = trade.Accumulator(OPTION1)
        self.subject_accumulator = trade.Accumulator(ASSET)
        self.exercise = copy.deepcopy(EXERCISE_OPERATION5)

    def fetch_and_accumulate(self):
        """Accumulate a exercise operation on the asset accumulator.

        and on the option accumulator When accumulating operations,
        the Operation object should be passed to the accumulator
        of all its assets.
        """
        self.exercise.fetch_operations()
        for operation in self.exercise.operations:
            self.subject_accumulator.accumulate(operation)
            self.option_accumulator.accumulate(operation)


class TestAccumulateExercise00(TestAccumulateExercise):
    """Accumulate a Option operation, and then its Exercise operation."""

    def setUp(self):
        super(TestAccumulateExercise00, self).setUp()
        self.option_accumulator.accumulate(
            copy.deepcopy(OPTION_OPERATION3)
        )
        self.fetch_and_accumulate()

    def test_accumulator1_price(self):
        self.assertEqual(self.subject_accumulator.state['price'], 10)

    def test_accumulator1_quantity(self):
        self.assertEqual(self.subject_accumulator.state['quantity'], 100)

    def test_accumulator1_results(self):
        self.assertEqual(self.subject_accumulator.state['results'], {})

    def test_accumulator2_price(self):
        self.assertEqual(self.option_accumulator.state['price'], 0)

    def test_accumulator2_quantity(self):
        self.assertEqual(self.option_accumulator.state['quantity'], 0)

    def test_accumulator2_results(self):
        self.assertEqual(self.option_accumulator.state['results'], {})


class TestAccumulateExercise01(TestAccumulateExercise):
    """Accumulate a operation, an option and then the exericse."""

    def setUp(self):
        super(TestAccumulateExercise01, self).setUp()
        self.operation0 = copy.deepcopy(OPERATION54)
        self.subject_accumulator.accumulate(self.operation0)
        self.operation1 = copy.deepcopy(OPTION_OPERATION3)
        self.option_accumulator.accumulate(self.operation1)
        self.exercise = copy.deepcopy(EXERCISE_OPERATION5)
        self.fetch_and_accumulate()

    def test_accumulator1_price(self):
        self.assertEqual(self.subject_accumulator.state['price'], 7.5)

    def test_accumulator1_quantity(self):
        self.assertEqual(self.subject_accumulator.state['quantity'], 200)

    def test_accumulator1_results(self):
        self.assertEqual(self.subject_accumulator.state['results'], {})

    def test_accumulator2_price(self):
        self.assertEqual(self.option_accumulator.state['price'], 0)

    def test_accumulator2_quantity(self):
        self.assertEqual(self.option_accumulator.state['quantity'], 0)

    def test_accumulator2_results(self):
        self.assertEqual(self.option_accumulator.state['results'], {})
