"""Test Exercise operations.

Exercise operations calls the exercise() method of its
assets to get the underlying operations of the exercise.
"""

from __future__ import absolute_import
import unittest
import copy

from tests.fixtures.operations import (
    EXERCISE_OPERATION5, EXERCISE_OPERATION6
)


class TestExerciseCase00(unittest.TestCase):
    """Exercising a call."""

    def setUp(self):
        super(TestExerciseCase00, self).setUp()
        self.exercise = copy.deepcopy(EXERCISE_OPERATION5)
        self.operations = self.exercise.fetch_operations()

    def test_operations_len(self):
        self.assertEqual(len(self.exercise.operations), 2)

    def test_option_consuming_quantity(self):
        self.assertEqual(self.exercise.operations[0].quantity, -100)

    def test_option_consuming_price(self):
        self.assertEqual(self.exercise.operations[0].price, 0)

    def test_asset_purchase_quantity(self):
        self.assertEqual(self.exercise.operations[1].quantity, 100)

    def test_asset_purchase_price(self):
        self.assertEqual(self.exercise.operations[1].price, 10)


class TestExerciseCase01(unittest.TestCase):
    """Being exercised on a call."""

    def setUp(self):
        super(TestExerciseCase01, self).setUp()
        self.exercise = copy.deepcopy(EXERCISE_OPERATION6)
        self.exercise.fetch_operations()

    def test_operations_len(self):
        self.assertEqual(len(self.exercise.operations), 2)

    def test_option_consuming_quantity(self):
        self.assertEqual(self.exercise.operations[0].quantity, -100)

    def test_option_consuming_price(self):
        self.assertEqual(self.exercise.operations[0].price, 0)

    def test_asset_purchase_quantity(self):
        self.assertEqual(self.exercise.operations[1].quantity, -100)

    def test_asset_purchase_price(self):
        self.assertEqual(self.exercise.operations[1].price, 10)
