from __future__ import absolute_import
import unittest

from trade.utils import (
    average_price, same_sign, daytrade_condition, find_purchase_and_sale
)
from trade import Asset, Operation


# TODO document this
# TODO more tests


class Test_same_sign(unittest.TestCase):

    def setUp(self):
        pass

    def test_same_sign_same_signs(self):
        self.assertTrue(same_sign(-1, -4))

    def test_same_sign_opposite_signs(self):
        self.assertFalse(same_sign(-1, 4))

    def test_same_sign_NaN(self):
        self.assertFalse(same_sign('a', 4))


class Test_average_price(unittest.TestCase):

    def setUp(self):
        pass

    def test_average_price_case_00(self):
        price = average_price(10, 2, 10, 4)
        self.assertEqual(price, 3)

    def test_average_price_case_01(self):
        price = average_price(10, 1, 10, 2)
        self.assertEqual(price, 1.5)

    def test_average_price_case_02(self):
        price = average_price(10, 1, 10, 3)
        self.assertEqual(price, 2)


class Test_daytrade_condition(unittest.TestCase):

    def setUp(self):
        self.asset1 = Asset()
        self.asset2 = Asset()

    def test_daytrade_condition_case_00(self):
        trade1 = Operation(-10, 5, date='2015-09-22',asset=self.asset1)
        trade2 = Operation(10, 5, date='2015-09-22', asset=self.asset1)
        self.assertTrue(daytrade_condition(trade1,trade2))

    def test_daytrade_condition_case_01(self):
        trade1 = Operation(10, 5, date='2015-09-22', asset=self.asset1)
        trade2 = Operation(-10, 5,date='2015-09-22', asset=self.asset1)
        self.assertTrue(daytrade_condition(trade1,trade2))

    def test_daytrade_condition_case_02(self):
        trade1 = Operation(0, 5, date='2015-09-22', asset=self.asset1)
        trade2 = Operation(0, 5, date='2015-09-22', asset=self.asset1)
        self.assertFalse(daytrade_condition(trade1,trade2))

    def test_daytrade_condition_case_03(self):
        trade1 = Operation(0, 5, date='2015-09-22', asset=self.asset1)
        trade2 = Operation(-10, 5, date='2015-09-22', asset=self.asset2)
        self.assertFalse(daytrade_condition(trade1,trade2))

    def test_daytrade_condition_case_04(self):
        trade1 = Operation(0, 5, date='2015-09-22', asset=self.asset1)
        trade2 = Operation(0, 5, date='2015-09-22', asset=self.asset2)
        self.assertFalse(daytrade_condition(trade1,trade2))



class Test_find_purchase_and_sale(unittest.TestCase):

    def setUp(self):
        self.asset = Asset()

    def test_find_purchase_and_sale_case_00(self):
        trade1 = Operation(10, 5, date='2015-09-22',asset=self.asset)
        trade2 = Operation(-10, 5, date='2015-09-22', asset=self.asset)
        result = (trade1, trade2)
        self.assertEqual(find_purchase_and_sale(trade1,trade2), result)

    def test_find_purchase_and_sale_case_01(self):
        trade1 = Operation(-10, 5, date='2015-09-22', asset=self.asset)
        trade2 = Operation(10, 5,date='2015-09-22', asset=self.asset)
        result = (trade2, trade1)
        self.assertEqual(find_purchase_and_sale(trade1,trade2), result)

    def test_find_purchase_and_sale_case_02(self):
        trade1 = Operation(10, 5, date='2015-09-22', asset=self.asset)
        trade2 = Operation(10, 5, date='2015-09-22', asset=self.asset)
        result = None
        self.assertEqual(find_purchase_and_sale(trade1,trade2), result)

    def test_find_purchase_and_sale_case_03(self):
        trade1 = Operation(-10, 5, date='2015-09-22', asset=self.asset)
        trade2 = Operation(-10, 5, date='2015-09-22', asset=self.asset)
        result = None
        self.assertEqual(find_purchase_and_sale(trade1,trade2), result)

    def test_find_purchase_and_sale_case_04(self):
        trade1 = Operation(0, 0, date='2015-09-22', asset=self.asset)
        trade2 = Operation(5, 5, date='2015-09-22', asset=self.asset)
        result = None
        self.assertEqual(find_purchase_and_sale(trade1,trade2), result)

    def test_find_purchase_and_sale_case_05(self):
        trade1 = Operation(0, 0, date='2015-09-22', asset=self.asset)
        trade2 = Operation(-5, 5, date='2015-09-22', asset=self.asset)
        result = None
        self.assertEqual(find_purchase_and_sale(trade1,trade2), result)

    def test_find_purchase_and_sale_case_06(self):
        trade1 = Operation(5, 0, date='2015-09-22', asset=self.asset)
        trade2 = Operation(0, 5, date='2015-09-22', asset=self.asset)
        result = None
        self.assertEqual(find_purchase_and_sale(trade1,trade2), result)

    def test_find_purchase_and_sale_case_07(self):
        trade1 = Operation(-5, 0, date='2015-09-22', asset=self.asset)
        trade2 = Operation(0, 5, date='2015-09-22', asset=self.asset)
        result = None
        self.assertEqual(find_purchase_and_sale(trade1,trade2), result)
