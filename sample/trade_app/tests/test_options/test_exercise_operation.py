"""Test Exercise operations.

Exercise operations calls the exercise() method of its
assets to get the underlying operations of the exercise.
"""

from __future__ import absolute_import
import unittest
import copy

from fixtures.operations import (
    EXERCISE_OPERATION5, EXERCISE_OPERATION6
)


class TestExercise(unittest.TestCase):

    length = 0
    option_quantity = 0
    option_price = 0
    asset_quantity = 0
    asset_price = 0
    exercise = None

    def setUp(self):
        super(TestExercise, self).setUp()
        if self.exercise:
            self.exercise = copy.deepcopy(self.exercise)
            self.operations = self.exercise.fetch_operations()

    def test_operations_len(self):
        """Check the len of the operations in the exercise."""
        if self.exercise:
            self.assertEqual(len(self.exercise.operations), self.length)

    def test_option_quantity(self):
        """Check the quantity of the operation consuming the option."""
        if self.exercise:
            self.assertEqual(
                self.exercise.operations[0].quantity,
                self.option_quantity
            )

    def test_option_price(self):
        """Check the price of the operation consuming the option."""
        if self.exercise:
            self.assertEqual(
                self.exercise.operations[0].price,
                self.option_price
            )

    def test_asset_quantity(self):
        """Check the quantity of the operation buying the asset."""
        if self.exercise:
            self.assertEqual(
                self.exercise.operations[1].quantity,
                self.asset_quantity
            )

    def test_asset_price(self):
        """Check the price of the operation buying the asset."""
        if self.exercise:
            self.assertEqual(
                self.exercise.operations[1].price,
                self.asset_price
            )


class TestExerciseCase00(TestExercise):
    """Exercising a call."""

    length = 2
    option_quantity = -100
    option_price = 0
    asset_quantity = 100
    asset_price = 10
    exercise = EXERCISE_OPERATION5


class TestExerciseCase01(TestExercise):
    """Being exercised on a call."""

    length = 2
    option_quantity = -100
    option_price = 0
    asset_quantity = -100
    asset_price = 10
    exercise = EXERCISE_OPERATION6
