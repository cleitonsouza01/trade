"""Test the accumulation of Exercise operations."""

from __future__ import absolute_import
import unittest
import copy

import trade

from tests.fixtures.assets import ASSET, OPTION1
from tests.fixtures.operations import (
    OPTION_OPERATION3, EXERCISE_OPERATION5, OPERATION54
)


class TestAccumulateExercise00(unittest.TestCase):
    """Accumulate a Option operation, and then its Exercise operation."""

    def setUp(self):
        # create a accumultor for the options, a accumulator for the asset
        self.option_accumulator = trade.Accumulator(OPTION1)
        self.asset_accumulator = trade.Accumulator(ASSET)
        self.option_accumulator.accumulate_occurrence(
            copy.deepcopy(OPTION_OPERATION3)
        )

        # Accumulate a exercise operation on the asset accumulator
        # and on the option accumulator
        # When accumulating operations, the Operation object should
        # be passed to the accumulator of all its assets
        self.exercise = copy.deepcopy(EXERCISE_OPERATION5)
        self.exercise.fetch_operations()
        self.asset_accumulator.accumulate_occurrence(self.exercise)
        self.option_accumulator.accumulate_occurrence(self.exercise)

    def test_accumulator1_price(self):
        self.assertEqual(self.asset_accumulator.price, 10)

    def test_accumulator1_quantity(self):
        self.assertEqual(self.asset_accumulator.quantity, 100)

    def test_accumulator1_results(self):
        self.assertEqual(self.asset_accumulator.results, {})

    def test_accumulator2_price(self):
        self.assertEqual(self.option_accumulator.price, 0)

    def test_accumulator2_quantity(self):
        self.assertEqual(self.option_accumulator.quantity, 0)

    def test_accumulator2_results(self):
        self.assertEqual(self.option_accumulator.results, {})


class TestAccumulateExercise01(unittest.TestCase):
    """Accumulate a operation, an option and then the exericse."""

    def setUp(self):

        # create a accumultor for the options, a accumulator for the asset
        self.option_accumulator = trade.Accumulator(OPTION1)
        self.asset_accumulator = trade.Accumulator(ASSET)

        # create and accumulate a operation
        # with the Asset
        self.operation0 = copy.deepcopy(OPERATION54)
        self.asset_accumulator.accumulate_occurrence(self.operation0)

        # Accumulate and accumulate an operation
        # with the Option
        self.operation1 = copy.deepcopy(OPTION_OPERATION3)
        self.option_accumulator.accumulate_occurrence(self.operation1)

        # Accumulate a exercise operation on the asset accumulator
        # and on the option accumulator
        # When accumulating operations, the Operation object should
        # be passed to the accumulator of all its assets
        self.exercise = trade.plugins.Exercise(
            quantity=100,
            price=10,
            asset=OPTION1,
            date='2015-01-01'
        )
        self.exercise.fetch_operations()
        self.asset_accumulator.accumulate_occurrence(self.exercise)
        self.option_accumulator.accumulate_occurrence(self.exercise)

    def test_accumulator1_price(self):
        self.assertEqual(self.asset_accumulator.price, 7.5)

    def test_accumulator1_quantity(self):
        self.assertEqual(self.asset_accumulator.quantity, 200)

    def test_accumulator1_results(self):
        self.assertEqual(self.asset_accumulator.results, {})

    def test_accumulator2_price(self):
        self.assertEqual(self.option_accumulator.price, 0)

    def test_accumulator2_quantity(self):
        self.assertEqual(self.option_accumulator.quantity, 0)

    def test_accumulator2_results(self):
        self.assertEqual(self.option_accumulator.results, {})
