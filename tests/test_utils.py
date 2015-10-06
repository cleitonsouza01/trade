"""Tests for the utils functions."""

from __future__ import absolute_import
import unittest

import trade


class TestOperationUtils(unittest.TestCase):

    def setUp(self):
        self.asset1 = trade.Asset()
        self.asset2 = trade.Asset()
        self.operation1 = trade.Operation(
            quantity=-10,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        self.operation2 = trade.Operation(
            quantity=10,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        self.operation3 = trade.Operation(
            quantity=0,
            price=0,
            date='2015-09-22',
            asset=self.asset1
        )
        self.operation4 = trade.Operation(
            quantity=0,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        self.operation5 = trade.Operation(
            quantity=-5,
            price=0,
            date='2015-09-22',
            asset=self.asset1
        )


class TestSameSign(unittest.TestCase):
    """Test the same_sign() function.

    This function should return True if the two values
    have opposite signs, and False otherwise.
    """

    def test_same_signs(self):
        self.assertTrue(trade.same_sign(-1, -4))

    def test_opposite_signs(self):
        self.assertFalse(trade.same_sign(-1, 4))


class TestAveragePrice(unittest.TestCase):
    """Test the function average_price.

    This function receives two quantity values, both with a
    price associeated to it, and returns the average price.
    """

    def test_case_00(self):
        price = trade.average_price(10, 2, 10, 4)
        self.assertEqual(price, 3)

    def test_case_01(self):
        price = trade.average_price(10, 1, 10, 2)
        self.assertEqual(price, 1.5)

    def test_case_02(self):
        price = trade.average_price(10, 1, 10, 3)
        self.assertEqual(price, 2)


class TestDaytradeCondition(TestOperationUtils):
    """Tests the function daytrade_condition().

    The daytrade_condition function receives two operations and
    shoul return True if the two operations configure a daytrade,
    False otherwise.
    """

    def test_case_00(self):
        self.assertTrue(
            trade.plugins.daytrade_condition(self.operation1, self.operation2)
        )

    def test_case_01(self):
        self.assertTrue(
            trade.plugins.daytrade_condition(self.operation2, self.operation1)
        )

    def test_case_02(self):
        self.assertFalse(
            trade.plugins.daytrade_condition(self.operation4, self.operation4)
        )

    def test_case_03(self):
        self.assertFalse(
            trade.plugins.daytrade_condition(self.operation4, self.operation1)
        )

    def test_case_04(self):
        operation2 = trade.Operation(
            quantity=0,
            price=5,
            date='2015-09-22',
            asset=self.asset2
        )
        self.assertFalse(
            trade.plugins.daytrade_condition(self.operation1, operation2)
        )

    def test_case_05(self):
        self.assertFalse(
            trade.plugins.daytrade_condition(self.operation1, self.operation4)
        )

    def test_case_06(self):
        operation2 = trade.Operation(
            quantity=10,
            price=5,
            date='2015-09-22',
            asset=self.asset2
        )
        self.assertFalse(
            trade.plugins.daytrade_condition(self.operation4, operation2)
        )

    def test_case_07(self):
        operation1 = trade.Operation(
            quantity=-10,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        operation2 = trade.Operation(
            quantity=-10,
            price=5,
            date='2015-09-22',
            asset=self.asset2
        )
        self.assertFalse(
            trade.plugins.daytrade_condition(operation1, operation2)
        )

    def test_case_08(self):
        self.assertFalse(
            trade.plugins.daytrade_condition(self.operation2, self.operation2)
        )


class TestFindPurchaseAndSale(TestOperationUtils):
    """Test the find_purchase_and_sale() function.

    This function receives two operations an is expected to
    return a tuple with the two operations: the purchase operation
    first as the first element and the sale operation as the second
    element.
    """

    def test_case_00(self):
        result = (self.operation2, self.operation1)
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(
                self.operation2, self.operation1
            ),
            result
        )

    def test_case_01(self):
        result = (self.operation2, self.operation1)
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(self.operation1, self.operation2),
            result
        )

    def test_case_02(self):
        result = None, None
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(
                self.operation2, self.operation2
            ),
            result
        )

    def test_case_03(self):
        result = None, None
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(
                self.operation1, self.operation1
            ),
            result
        )

    def test_case_04(self):
        operation2 = trade.Operation(
            quantity=5,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        result = None, None
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(self.operation2, operation2),
            result
        )

    def test_case_05(self):
        operation2 = trade.Operation(
            quantity=-5,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        result = (self.operation3, operation2)
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(self.operation3, operation2),
            result
        )

    def test_case_06(self):
        operation1 = trade.Operation(
            quantity=5,
            price=0,
            date='2015-09-22',
            asset=self.asset1
        )
        result = None, None
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(operation1, self.operation4),
            result
        )

    def test_case_07(self):

        result = (self.operation4, self.operation5)
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(
                self.operation5, self.operation4
            ),
            result
        )
