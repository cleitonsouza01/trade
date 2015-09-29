from __future__ import absolute_import
import unittest

import trade


class TestDaytradeCreation(unittest.TestCase):

    def setUp(self):
        self.asset = trade.Asset(name='some stock')
        self.daytrade = trade.Daytrade(
                            date='2015-09-20',
                            asset=self.asset,
                            quantity=10,
                            purchase_price=2,
                            sale_price=3
                        )

    def test_daytrade_should_exist(self):
        self.assertTrue(self.daytrade)

    def test_check_daytrade_asset(self):
        self.assertEqual(self.daytrade.asset, self.asset)

    def test_check_daytrade_quantity(self):
        self.assertEqual(self.daytrade.quantity, 10)

    def test_daytrade_buy_operation_should_exist(self):
        self.assertTrue(self.daytrade.purchase)

    def test_check_daytrade_buy_operation_asset(self):
        self.assertEqual(self.daytrade.purchase.asset, self.asset)

    def test_check_daytrade_buy_operation_quantity(self):
        self.assertEqual(self.daytrade.purchase.quantity, 10)

    def test_check_daytrade_buy_operation_price(self):
        self.assertEqual(self.daytrade.purchase.price, 2)

    def test_daytrade_sale_operation_should_exist(self):
        self.assertTrue(self.daytrade.sale)

    def test_check_daytrade_sale_operation_asset(self):
        self.assertEqual(self.daytrade.sale.asset, self.asset)

    def test_check_daytrade_sale_operation_quantity(self):
        self.assertEqual(self.daytrade.sale.quantity, -10)

    def test_check_daytrade_sale_operation_price(self):
        self.assertEqual(self.daytrade.sale.price, 3)


class TestDaytradeResult_case_00(unittest.TestCase):

    def setUp(self):
        self.daytrade = trade.Daytrade(
                            date='2015-09-20',
                            asset=trade.Asset(),
                            quantity=10,
                            purchase_price=2,
                            sale_price=3
                        )

    def test_daytrade_should_exist(self):
        self.assertTrue(self.daytrade)

    def test_daytrade_result_should_be_1(self):
        self.assertEqual(self.daytrade.result, 10)


class TestDaytradeResult_case_01(unittest.TestCase):

    def setUp(self):
        self.daytrade = trade.Daytrade(
                            date='2015-09-20',
                            asset=trade.Asset(),
                            quantity=10,
                            purchase_price=3,
                            sale_price=2
                        )

    def test_daytrade_should_exist(self):
        self.assertTrue(self.daytrade)

    def test_daytrade_result_should_be_1(self):
        self.assertEqual(self.daytrade.result, -10)
