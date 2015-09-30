from __future__ import absolute_import
import unittest

import trade


class TestDaytradeCreation(unittest.TestCase):
    """Tests the creation of daytrade objects.

    Daytrade objects should create two operations, the
    purchase_operation and the sale_operation based on the
    values informed during its cretion.
    """

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
        self.assertTrue(self.daytrade.operations[0])

    def test_check_daytrade_buy_operation_asset(self):
        self.assertEqual(self.daytrade.operations[0].asset, self.asset)

    def test_check_daytrade_buy_operation_quantity(self):
        self.assertEqual(self.daytrade.operations[0].quantity, 10)

    def test_check_daytrade_buy_operation_price(self):
        self.assertEqual(self.daytrade.operations[0].price, 2)

    def test_daytrade_sale_operation_should_exist(self):
        self.assertTrue(self.daytrade.operations[1])

    def test_check_daytrade_sale_operation_asset(self):
        self.assertEqual(self.daytrade.operations[1].asset, self.asset)

    def test_check_daytrade_sale_operation_quantity(self):
        self.assertEqual(self.daytrade.operations[1].quantity, -10)

    def test_check_daytrade_sale_operation_price(self):
        self.assertEqual(self.daytrade.operations[1].price, 3)


class TestDaytradeResult_case_00(unittest.TestCase):
    """Tests the results of a Daytrade operation.

    Daytrade results are based on the prices of the sale
    and purchase operations.
    """

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
    """Tests the results of a Daytrade operation.

    Daytrade results are based on the prices of the sale
    and purchase operations.
    """

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
