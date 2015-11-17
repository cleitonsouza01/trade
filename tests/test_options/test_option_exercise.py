"""Test the exercise() method of Option objects."""

from __future__ import absolute_import
import unittest

from tests.fixtures.assets import OPTION1


class TestOptionExerciseCase00(unittest.TestCase):
    """Test the exercises of a call and a put."""

    def setUp(self):
        self.option = OPTION1
        self.exercise_op_1 = self.option.exercise(quantity=100, price=10)

    def test_len(self):
        self.assertEqual(len(self.exercise_op_1), 2)

    def test_consuming_quantity(self):
        self.assertEqual(self.exercise_op_1[0].quantity, -100)

    def test_consuming_price(self):
        self.assertEqual(self.exercise_op_1[0].price, 0)

    def test_purchase_quantity(self):
        self.assertEqual(self.exercise_op_1[1].quantity, 100)

    def test_purchase_price(self):
        self.assertEqual(self.exercise_op_1[1].price, 10)


class TestOptionExerciseCase01(unittest.TestCase):
    """Test the exercises of a call and a put."""

    def setUp(self):
        self.option = OPTION1
        self.exercise_op_2 = self.option.exercise(quantity=-100, price=10)

    def test_len(self):
        self.assertEqual(len(self.exercise_op_2), 2)

    def test_consuming_quantity(self):
        self.assertEqual(self.exercise_op_2[0].quantity, -100)

    def test_consuming_price(self):
        self.assertEqual(self.exercise_op_2[0].price, 0)

    def test_purchase_quantity(self):
        self.assertEqual(self.exercise_op_2[1].quantity, -100)

    def test_purchase_price(self):
        self.assertEqual(self.exercise_op_2[1].price, 10)
