"""Tests for the utils functions."""

from __future__ import absolute_import
import unittest

from trade import utils
from tests.fixtures.operations import (
    OPERATION46, OPERATION55, OPERATION56, OPERATION57, OPERATION58,
    OPERATION59, OPERATION43
)


class TestSameSign(unittest.TestCase):
    """Test the same_sign() function.

    This function should return True if the two values
    have opposite signs, and False otherwise.
    """

    def test_same_signs(self):
        self.assertTrue(utils.same_sign(-1, -4))

    def test_opposite_signs(self):
        self.assertFalse(utils.same_sign(-1, 4))


class TestAveragePrice(unittest.TestCase):
    """Test the function average_price.

    This function receives two quantity values, both with a
    price associeated to it, and returns the average price.
    """

    def test_case_00(self):
        price = utils.average_price(10, 2, 10, 4)
        self.assertEqual(price, 3)

    def test_case_01(self):
        price = utils.average_price(10, 1, 10, 2)
        self.assertEqual(price, 1.5)

    def test_case_02(self):
        price = utils.average_price(10, 1, 10, 3)
        self.assertEqual(price, 2)


class TestDaytradeCondition(unittest.TestCase):
    """Tests the function daytrade_condition().

    The daytrade_condition function receives two operations and
    shoul return True if the two operations configure a daytrade,
    False otherwise.
    """

    def test_case_00(self):
        self.assertTrue(
            utils.daytrade_condition(OPERATION55, OPERATION46)
        )

    def test_case_01(self):
        self.assertTrue(
            utils.daytrade_condition(OPERATION46, OPERATION55)
        )

    def test_case_02(self):
        self.assertFalse(
            utils.daytrade_condition(OPERATION57, OPERATION57)
        )

    def test_case_04(self):
        self.assertFalse(
            utils.daytrade_condition(OPERATION55, OPERATION59)
        )

    def test_case_06(self):
        self.assertFalse(
            utils.daytrade_condition(OPERATION57, OPERATION46)
        )

    def test_case_09(self):
        self.assertFalse(
            utils.daytrade_condition(OPERATION46, OPERATION46)
        )


class TestFindPurchaseAndSale(unittest.TestCase):
    """Test the find_purchase_and_sale() function.

    This function receives two operations an is expected to
    return a tuple with the two operations: the purchase operation
    first as the first element and the sale operation as the second
    element.
    """

    def test_case_00(self):
        self.assertEqual(
            utils.find_purchase_and_sale(OPERATION46, OPERATION55),
            (OPERATION46, OPERATION55)
        )

    def test_case_01(self):
        self.assertEqual(
            utils.find_purchase_and_sale(OPERATION55, OPERATION46),
            (OPERATION46, OPERATION55)
        )

    def test_case_05(self):
        self.assertEqual(
            utils.find_purchase_and_sale(OPERATION56, OPERATION43),
            (OPERATION56, OPERATION43)
        )

    def test_case_07(self):
        self.assertEqual(
            utils.find_purchase_and_sale(OPERATION58, OPERATION57),
            (OPERATION57, OPERATION58)
        )
