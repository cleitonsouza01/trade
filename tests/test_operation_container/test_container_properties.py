from __future__ import absolute_import
import unittest

import trade as trade_tools


# TODO document this
# TODO more tests


class TestTradeContainer_total_discount_value_one_discount(
        unittest.TestCase
    ):

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        self.trade_container = trade_tools.OperationContainer(
            fixed_commissions=discounts
        )

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade_container_raw_discounts(self):
        expected_discounts = {
            'some discount': 1,
        }
        self.assertEqual(self.trade_container.fixed_commissions, expected_discounts)

    def test_trade_container_total_discount_value_should_be_one(self):
        self.assertEqual(self.trade_container.total_commission_value, 1)


class TestTradeContainer_total_discount_value_multiple_discounts(
        unittest.TestCase
    ):

    def setUp(self):
        discounts = {
            'some discount': 1,
            'other discount': 3,
        }
        self.trade_container = trade_tools.OperationContainer(
            fixed_commissions=discounts
        )

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade_container_raw_discounts(self):
        expected_discounts = {
            'some discount': 1,
            'other discount': 3,
        }
        self.assertEqual(self.trade_container.fixed_commissions, expected_discounts)

    def test_trade_container_total_discount_value_should_be_4(self):
        self.assertEqual(self.trade_container.total_commission_value, 4)


class TestTradeContainer_volume_one_trade(unittest.TestCase):

    def setUp(self):
        asset = trade_tools.Asset('some asset')
        trade = trade_tools.Operation(
            date='2015-09-21', asset=asset, quantity=10, price=2)
        self.trade_container = trade_tools.OperationContainer(
            operations=[trade]
        )

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trade_container_trades_should_have_one_trade(self):
        self.assertEqual(len(self.trade_container.operations), 1)

    def test_trade_container_volume_should_be_20(self):
        self.assertEqual(self.trade_container.volume, 20)


class TestTradeContainer_volume_multiple_trades_case_00(unittest.TestCase):

    def setUp(self):
        asset = trade_tools.Asset('some asset')
        trade1 = trade_tools.Operation(
            date='2015-09-21', asset=asset, quantity=10, price=2)
        trade2 = trade_tools.Operation(
            date='2015-09-21', asset=asset, quantity=5, price=1)
        self.trade_container = trade_tools.OperationContainer(
            operations=[trade1,trade2])

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trade_container_trades_should_have_one_trade(self):
        self.assertEqual(len(self.trade_container.operations), 2)

    def test_trade_container_volume_should_be_20(self):
        self.assertEqual(self.trade_container.volume, 25)


class TestTradeContainer_volume_multiple_trades_case_01(unittest.TestCase):

    def setUp(self):
        asset = trade_tools.Asset('some asset')
        trade1 = trade_tools.Operation(
            date='2015-09-21', asset=asset, quantity=-10, price=2)
        trade2 = trade_tools.Operation(
            date='2015-09-21', asset=asset, quantity=5, price=1)
        self.trade_container = trade_tools.OperationContainer(
            operations=[trade1,trade2])

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trade_container_trades_should_have_two_trades(self):
        self.assertEqual(len(self.trade_container.operations), 2)

    def test_trade_container_volume_should_be_20(self):
        self.assertEqual(self.trade_container.volume, 25)


class TestTradeContainer_volume_multiple_trades_case_02(unittest.TestCase):

    def setUp(self):
        asset1 = trade_tools.Asset('some asset')
        asset2 = trade_tools.Asset('some other asset')
        trade1 = trade_tools.Operation(
            date='2015-09-21', asset=asset1, quantity=-10, price=2)
        trade2 = trade_tools.Operation(
            date='2015-09-21', asset=asset1, quantity=5, price=1)
        trade3 = trade_tools.Operation(
            date='2015-09-21', asset=asset2, quantity=20, price=5)
        self.trade_container = trade_tools.OperationContainer(
            operations=[trade1,trade2,trade3])

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trade_container_trades_should_have_three_trades(self):
        self.assertEqual(len(self.trade_container.operations), 3)

    def test_trade_container_volume_should_be_20(self):
        self.assertEqual(self.trade_container.volume, 125)
