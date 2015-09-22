from __future__ import absolute_import
import unittest

import trade_tools


# TODO document this


class TestTradeContainerCreation(unittest.TestCase):

    def setUp(self):
        self.trade_container = trade_tools.TradeContainer()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

class TestTradeContainer_total_discount_value_one_discount(
        unittest.TestCase
    ):

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        self.trade_container = trade_tools.TradeContainer(discounts=discounts)

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade_container_raw_discounts(self):
        expected_discounts = {
            'some discount': 1,
        }
        self.assertEqual(self.trade_container.discounts, expected_discounts)

    def test_trade_container_total_discount_value_should_be_one(self):
        self.assertEqual(self.trade_container.total_discount_value, 1)


class TestTradeContainer_total_discount_value_multiple_discounts(
        unittest.TestCase
    ):

    def setUp(self):
        discounts = {
            'some discount': 1,
            'other discount': 3,
        }
        self.trade_container = trade_tools.TradeContainer(discounts=discounts)

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade_container_raw_discounts(self):
        expected_discounts = {
            'some discount': 1,
            'other discount': 3,
        }
        self.assertEqual(self.trade_container.discounts, expected_discounts)

    def test_trade_container_total_discount_value_should_be_4(self):
        self.assertEqual(self.trade_container.total_discount_value, 4)


class TestTradeContainer_volume_one_trade(unittest.TestCase):

    def setUp(self):
        asset = trade_tools.Asset('some asset')
        trade = trade_tools.Trade(
            date='2015-09-21', asset=asset, quantity=10, price=2)
        self.trade_container = trade_tools.TradeContainer(trades=[trade])

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trade_container_trades_should_have_one_trade(self):
        self.assertEqual(len(self.trade_container.trades), 1)

    def test_trade_container_volume_should_be_20(self):
        self.assertEqual(self.trade_container.volume, 20)


class TestTradeContainer_volume_multiple_trades_case_00(unittest.TestCase):

    def setUp(self):
        asset = trade_tools.Asset('some asset')
        trade1 = trade_tools.Trade(
            date='2015-09-21', asset=asset, quantity=10, price=2)
        trade2 = trade_tools.Trade(
            date='2015-09-21', asset=asset, quantity=5, price=1)
        self.trade_container = trade_tools.TradeContainer(
            trades=[trade1,trade2])

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trade_container_trades_should_have_one_trade(self):
        self.assertEqual(len(self.trade_container.trades), 2)

    def test_trade_container_volume_should_be_20(self):
        self.assertEqual(self.trade_container.volume, 25)


class TestTradeContainer_volume_multiple_trades_case_01(unittest.TestCase):

    def setUp(self):
        asset = trade_tools.Asset('some asset')
        trade1 = trade_tools.Trade(
            date='2015-09-21', asset=asset, quantity=-10, price=2)
        trade2 = trade_tools.Trade(
            date='2015-09-21', asset=asset, quantity=5, price=1)
        self.trade_container = trade_tools.TradeContainer(
            trades=[trade1,trade2])

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trade_container_trades_should_have_two_trades(self):
        self.assertEqual(len(self.trade_container.trades), 2)

    def test_trade_container_volume_should_be_20(self):
        self.assertEqual(self.trade_container.volume, 25)


class TestTradeContainer_volume_multiple_trades_case_02(unittest.TestCase):

    def setUp(self):
        asset1 = trade_tools.Asset('some asset')
        asset2 = trade_tools.Asset('some other asset')
        trade1 = trade_tools.Trade(
            date='2015-09-21', asset=asset1, quantity=-10, price=2)
        trade2 = trade_tools.Trade(
            date='2015-09-21', asset=asset1, quantity=5, price=1)
        trade3 = trade_tools.Trade(
            date='2015-09-21', asset=asset2, quantity=20, price=5)
        self.trade_container = trade_tools.TradeContainer(
            trades=[trade1,trade2,trade3])

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trade_container_trades_should_have_three_trades(self):
        self.assertEqual(len(self.trade_container.trades), 3)

    def test_trade_container_volume_should_be_20(self):
        self.assertEqual(self.trade_container.volume, 125)


class TestTradeContainer_rate_discounts_by_trade_case_00(unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        asset = trade_tools.Asset('some asset')
        self.trade = trade_tools.Trade(
            date='2015-09-21', asset=asset, quantity=-10, price=2)
        self.trade_container = trade_tools.TradeContainer(
            trades=[self.trade], discounts=discounts)

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade_discount(self):
        expected_discounts = {
            'some discount': 1,
        }
        self.trade_container.rate_discounts_by_trade(self.trade)
        self.assertEqual(self.trade.discounts, expected_discounts)


class TestTradeContainer_rate_discounts_by_trade_case_01(unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        asset = trade_tools.Asset('some asset')
        self.trade1 = trade_tools.Trade(
            date='2015-09-21', asset=asset, quantity=-10, price=2)
        self.trade2 = trade_tools.Trade(
            date='2015-09-21', asset=asset, quantity=-10, price=2)
        self.trade_container = trade_tools.TradeContainer(
            trades=[self.trade1,self.trade2], discounts=discounts)

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade1_discount(self):
        expected_discounts = {
            'some discount': 0.5,
        }
        self.trade_container.rate_discounts_by_trade(self.trade1)
        self.assertEqual(self.trade1.discounts, expected_discounts)

    def test_check_trade2_discount(self):
        expected_discounts = {
            'some discount': 0.5,
        }
        self.trade_container.rate_discounts_by_trade(self.trade2)
        self.assertEqual(self.trade2.discounts, expected_discounts)


class TestTradeContainer_rate_discounts_by_trade_case_02(unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        asset = trade_tools.Asset('some asset')
        self.trade1 = trade_tools.Trade(
            date='2015-09-21', asset=asset, quantity=-10, price=2)
        self.trade2 = trade_tools.Trade(
            date='2015-09-21', asset=asset, quantity=-20, price=2)
        self.trade_container = trade_tools.TradeContainer(
            trades=[self.trade1,self.trade2], discounts=discounts)

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade1_discount(self):
        self.trade_container.rate_discounts_by_trade(self.trade1)
        self.assertEqual(
            round(self.trade1.discounts['some discount'], 8),
            0.33333333
        )

    def test_check_trade2_discount(self):
        self.trade_container.rate_discounts_by_trade(self.trade2)
        self.assertEqual(
            round(self.trade2.discounts['some discount'], 8),
            0.66666667
        )


class TestTradeContainer_rate_discounts_by_trade_case_03(unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 4,
        }
        asset1 = trade_tools.Asset('some asset')
        asset2 = trade_tools.Asset('some other asset')
        self.trade1 = trade_tools.Trade(
            date='2015-09-21', asset=asset1, quantity=-10, price=2)
        self.trade2 = trade_tools.Trade(
            date='2015-09-21', asset=asset1, quantity=-20, price=2)
        self.trade3 = trade_tools.Trade(
            date='2015-09-21', asset=asset2, quantity=-10, price=2)
        self.trade_container = trade_tools.TradeContainer(
            trades=[self.trade1,self.trade2, self.trade3], discounts=discounts)

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade1_discount(self):
        self.trade_container.rate_discounts_by_trade(self.trade1)
        self.assertEqual(self.trade1.discounts['some discount'], 1)

    def test_check_trade2_discount(self):
        self.trade_container.rate_discounts_by_trade(self.trade2)
        self.assertEqual(self.trade2.discounts['some discount'], 2)

    def test_check_trade3_discount(self):
        self.trade_container.rate_discounts_by_trade(self.trade3)
        self.assertEqual(self.trade3.discounts['some discount'], 1)


class TestTradeContainer_identify_daytrades_and_common_trades_case_00(
        unittest.TestCase):

    def setUp(self):
        self.asset = trade_tools.Asset('some asset')
        self.trade1 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset, quantity=10, price=2)
        self.trade2 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset, quantity=-10, price=3)
        self.trade_container = trade_tools.TradeContainer(
            trades=[self.trade1,self.trade2])
        self.trade_container.identify_daytrades_and_common_trades()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_two(self):
        self.assertEqual(len(self.trade_container.trades), 2)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.trades[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.trades[0].price, 2)

    def test_trade_1_quantity_should_be_minus_10(self):
        self.assertEqual(self.trade_container.trades[1].quantity, -10)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.trade_container.trades[1].price, 3)

    def test_common_trades_len_should_be_0(self):
        self.assertEqual(len(self.trade_container.common_trades), 0)

    def test_daytrades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.daytrades), 1)

    def test_check_daytrade_asset(self):
        self.assertEqual(self.trade_container.daytrades[0].asset, self.asset)

    def test_daytrade_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.daytrades[0].quantity, 10)

    def test_daytrade_buy_price_should_be_2(self):
        self.assertEqual(self.trade_container.daytrades[0].buy.price, 2)

    def test_daytrade_buy_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.daytrades[0].buy.quantity, 10)

    def test_daytrade_sale_price_should_be_3(self):
        self.assertEqual(self.trade_container.daytrades[0].sale.price, 3)

    def test_daytrade_sale_quantity_should_be_minus_10(self):
        self.assertEqual(self.trade_container.daytrades[0].sale.quantity, -10)

    def test_daytrade_result_should_be_10(self):
        self.assertEqual(self.trade_container.daytrades[0].result, 10)


class TestTradeContainer_identify_daytrades_and_common_trades_case_01(
        unittest.TestCase):

    def setUp(self):
        self.asset = trade_tools.Asset('some asset')
        self.trade1 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset, quantity=10, price=2)
        self.trade2 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset, quantity=-5, price=3)
        self.trade_container = trade_tools.TradeContainer(
            trades=[self.trade1,self.trade2])
        self.trade_container.identify_daytrades_and_common_trades()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_two(self):
        self.assertEqual(len(self.trade_container.trades), 2)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.trades[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.trades[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.trades[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.trade_container.trades[1].price, 3)

    def test_common_trades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.common_trades), 1)

    def test_check_common_trades0_asset(self):
        self.assertEqual(
            self.trade_container.common_trades[0].asset,
            self.asset
        )

    def test_common_trades1_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.common_trades[0].quantity, 5)

    def test_common_trades1_price_should_be_2(self):
        self.assertEqual(self.trade_container.common_trades[0].price, 2)

    def test_daytrades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.daytrades), 1)

    def test_check_daytrade_asset(self):
        self.assertEqual(self.trade_container.daytrades[0].asset, self.asset)

    def test_daytrade_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[0].quantity, 5)

    def test_daytrade_buy_price_should_be_2(self):
        self.assertEqual(self.trade_container.daytrades[0].buy.price, 2)

    def test_daytrade_buy_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[0].buy.quantity, 5)

    def test_daytrade_sale_price_should_be_3(self):
        self.assertEqual(self.trade_container.daytrades[0].sale.price, 3)

    def test_daytrade_sale_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.daytrades[0].sale.quantity, -5)

    def test_daytrade_result_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[0].result, 5)


class TestTradeContainer_identify_daytrades_and_common_trades_case_02(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade_tools.Asset('some asset')
        self.asset2 = trade_tools.Asset('some other asset')
        trade1 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset1, quantity=10, price=2)
        trade2 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset1, quantity=-5, price=3)
        trade3 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset2, quantity=-5, price=7)
        self.trade_container = trade_tools.TradeContainer(
            trades=[trade1,trade2,trade3])
        self.trade_container.identify_daytrades_and_common_trades()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_three(self):
        self.assertEqual(len(self.trade_container.trades), 3)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.trades[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.trades[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.trades[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.trade_container.trades[1].price, 3)

    def test_common_trades_len_should_be_2(self):
        self.assertEqual(len(self.trade_container.common_trades), 2)

    def test_check_common_trades0_asset(self):
        self.assertEqual(
            self.trade_container.common_trades[0].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.common_trades[0].quantity, 5)

    def test_common_trades0_price_should_be_2(self):
        self.assertEqual(self.trade_container.common_trades[0].price, 2)

    def test_check_common_trades1_asset(self):
        self.assertEqual(
            self.trade_container.common_trades[1].asset,
            self.asset2
        )

    def test_common_trades1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.common_trades[1].quantity, -5)

    def test_common_trades1_price_should_be_7(self):
        self.assertEqual(self.trade_container.common_trades[1].price, 7)

    def test_daytrades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.daytrades), 1)

    def test_check_daytrade_asset(self):
        self.assertEqual(self.trade_container.daytrades[0].asset, self.asset1)

    def test_daytrade_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[0].quantity, 5)

    def test_daytrade_buy_price_should_be_2(self):
        self.assertEqual(self.trade_container.daytrades[0].buy.price, 2)

    def test_daytrade_buy_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[0].buy.quantity, 5)

    def test_daytrade_sale_price_should_be_3(self):
        self.assertEqual(self.trade_container.daytrades[0].sale.price, 3)

    def test_daytrade_sale_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.daytrades[0].sale.quantity, -5)

    def test_daytrade_result_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[0].result, 5)


class TestTradeContainer_identify_daytrades_and_common_trades_case_03(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade_tools.Asset('some asset')
        self.asset2 = trade_tools.Asset('some other asset')
        trade1 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset1, quantity=10, price=2)
        trade2 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset1, quantity=-5, price=3)
        trade3 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset2, quantity=-5, price=7)
        trade4 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset2, quantity=5, price=10)
        self.trade_container = trade_tools.TradeContainer(
            trades=[trade1,trade2,trade3,trade4])
        self.trade_container.identify_daytrades_and_common_trades()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_four(self):
        self.assertEqual(len(self.trade_container.trades), 4)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.trades[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.trades[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.trades[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.trade_container.trades[1].price, 3)

    def test_common_trades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.common_trades), 1)

    def test_check_common_trades0_asset(self):
        self.assertEqual(
            self.trade_container.common_trades[0].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.common_trades[0].quantity, 5)

    def test_common_trades0_price_should_be_2(self):
        self.assertEqual(self.trade_container.common_trades[0].price, 2)

    def test_daytrades_len_should_be_2(self):
        self.assertEqual(len(self.trade_container.daytrades), 2)

    def test_check_daytrade0_asset(self):
        self.assertEqual(self.trade_container.daytrades[0].asset, self.asset1)

    def test_daytrade0_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[0].quantity, 5)

    def test_daytrade0_buy_price_should_be_2(self):
        self.assertEqual(self.trade_container.daytrades[0].buy.price, 2)

    def test_daytrade0_buy_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[0].buy.quantity, 5)

    def test_daytrade0_sale_price_should_be_3(self):
        self.assertEqual(self.trade_container.daytrades[0].sale.price, 3)

    def test_daytrade0_sale_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.daytrades[0].sale.quantity, -5)

    def test_daytrade0_result_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[0].result, 5)

    def test_check_daytrade1_asset(self):
        self.assertEqual(self.trade_container.daytrades[1].asset, self.asset2)

    def test_daytrade1_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[1].quantity, 5)

    def test_daytrade1_buy_price_should_be_10(self):
        self.assertEqual(self.trade_container.daytrades[1].buy.price, 10)

    def test_daytrade1_buy_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[1].buy.quantity, 5)

    def test_daytrade1_sale_price_should_be_7(self):
        self.assertEqual(self.trade_container.daytrades[1].sale.price, 7)

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.daytrades[1].sale.quantity, -5)

    def test_daytrade1_result_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[1].result, -15)


class TestTradeContainer_identify_daytrades_and_common_trades_case_04(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade_tools.Asset('some asset')
        self.asset2 = trade_tools.Asset('some other asset')
        trade1 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset1, quantity=10, price=2)
        trade2 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset1, quantity=-5, price=3)
        trade3 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset2, quantity=-5, price=7)
        trade4 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset2, quantity=5, price=10)
        trade5 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset1, quantity=-5, price=3)
        self.trade_container = trade_tools.TradeContainer(
            trades=[trade1,trade2,trade3,trade4,trade5])
        self.trade_container.identify_daytrades_and_common_trades()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_five(self):
        self.assertEqual(len(self.trade_container.trades), 5)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.trades[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.trades[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.trades[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.trade_container.trades[1].price, 3)

    def test_common_trades_len_should_be_0(self):
        self.assertEqual(len(self.trade_container.common_trades), 0)

    def test_daytrades_len_should_be_2(self):
        self.assertEqual(len(self.trade_container.daytrades), 2)

    def test_check_daytrade0_asset(self):
        self.assertEqual(self.trade_container.daytrades[0].asset, self.asset1)

    def test_daytrade0_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[0].quantity, 10)

    def test_daytrade0_buy_price_should_be_2(self):
        self.assertEqual(self.trade_container.daytrades[0].buy.price, 2)

    def test_daytrade0_buy_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.daytrades[0].buy.quantity, 10)

    def test_daytrade0_sale_price_should_be_3(self):
        self.assertEqual(self.trade_container.daytrades[0].sale.price, 3)

    def test_daytrade0_sale_quantity_should_be_minus_10(self):
        self.assertEqual(self.trade_container.daytrades[0].sale.quantity, -10)

    def test_daytrade0_result_should_be_10(self):
        self.assertEqual(self.trade_container.daytrades[0].result, 10)

    def test_check_daytrade1_asset(self):
        self.assertEqual(self.trade_container.daytrades[1].asset, self.asset2)

    def test_daytrade1_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[1].quantity, 5)

    def test_daytrade1_buy_price_should_be_10(self):
        self.assertEqual(self.trade_container.daytrades[1].buy.price, 10)

    def test_daytrade1_buy_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[1].buy.quantity, 5)

    def test_daytrade1_sale_price_should_be_7(self):
        self.assertEqual(self.trade_container.daytrades[1].sale.price, 7)

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.daytrades[1].sale.quantity, -5)

    def test_daytrade1_result_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[1].result, -15)


class TestTradeContainer_identify_daytrades_and_common_trades_case_05(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade_tools.Asset('some asset')
        self.asset2 = trade_tools.Asset('some other asset')
        trade1 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset1, quantity=10, price=2)
        trade2 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset1, quantity=-5, price=10)
        trade3 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset2, quantity=-5, price=7)
        trade4 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset2, quantity=5, price=10)
        trade5 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset1, quantity=-5, price=20)
        self.trade_container = trade_tools.TradeContainer(
            trades=[trade1,trade2,trade3,trade4,trade5])
        self.trade_container.identify_daytrades_and_common_trades()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_five(self):
        self.assertEqual(len(self.trade_container.trades), 5)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.trades[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.trades[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.trades[1].quantity, -5)

    def test_trade_1_price_should_be_10(self):
        self.assertEqual(self.trade_container.trades[1].price, 10)

    def test_common_trades_len_should_be_0(self):
        self.assertEqual(len(self.trade_container.common_trades), 0)

    def test_daytrades_len_should_be_2(self):
        self.assertEqual(len(self.trade_container.daytrades), 2)

    def test_check_daytrade0_asset(self):
        self.assertEqual(self.trade_container.daytrades[0].asset, self.asset1)

    def test_daytrade0_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[0].quantity, 10)

    def test_daytrade0_buy_price_should_be_10(self):
        self.assertEqual(self.trade_container.daytrades[0].buy.price, 2)

    def test_daytrade0_buy_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.daytrades[0].buy.quantity, 10)

    def test_daytrade0_sale_price_should_be_15(self):
        self.assertEqual(self.trade_container.daytrades[0].sale.price, 15)

    def test_daytrade0_sale_quantity_should_be_minus_10(self):
        self.assertEqual(self.trade_container.daytrades[0].sale.quantity, -10)

    def test_daytrade0_result_should_be_130(self):
        self.assertEqual(self.trade_container.daytrades[0].result, 130)

    def test_check_daytrade1_asset(self):
        self.assertEqual(self.trade_container.daytrades[1].asset, self.asset2)

    def test_daytrade1_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[1].quantity, 5)

    def test_daytrade1_buy_price_should_be_10(self):
        self.assertEqual(self.trade_container.daytrades[1].buy.price, 10)

    def test_daytrade1_buy_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[1].buy.quantity, 5)

    def test_daytrade1_sale_price_should_be_7(self):
        self.assertEqual(self.trade_container.daytrades[1].sale.price, 7)

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.daytrades[1].sale.quantity, -5)

    def test_daytrade1_result_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[1].result, -15)



class TestTradeContainer_identify_daytrades_and_common_trades_case_06(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade_tools.Asset('some asset')
        self.asset2 = trade_tools.Asset('some other asset')
        trade1 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset1, quantity=10, price=2)
        trade2 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset1, quantity=-5, price=3)
        trade3 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset2, quantity=-5, price=7)
        trade4 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset2, quantity=5, price=10)
        trade5 = trade_tools.Trade(
            date='2015-09-21', asset=self.asset1, quantity=5, price=4)
        self.trade_container = trade_tools.TradeContainer(
            trades=[trade1,trade2,trade3,trade4,trade5])
        self.trade_container.identify_daytrades_and_common_trades()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_five(self):
        self.assertEqual(len(self.trade_container.trades), 5)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.trades[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.trades[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.trades[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.trade_container.trades[1].price, 3)

    def test_common_trades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.common_trades), 1)

    def test_check_common_trades0_asset(self):
        self.assertEqual(
            self.trade_container.common_trades[0].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.common_trades[0].quantity, 10)

    def test_common_trades0_price_should_be_3(self):
        self.assertEqual(self.trade_container.common_trades[0].price, 3)

    def test_daytrades_len_should_be_2(self):
        self.assertEqual(len(self.trade_container.daytrades), 2)

    def test_check_daytrade0_asset(self):
        self.assertEqual(self.trade_container.daytrades[0].asset, self.asset1)

    def test_daytrade0_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[0].quantity, 5)

    def test_daytrade0_buy_price_should_be_2(self):
        self.assertEqual(self.trade_container.daytrades[0].buy.price, 2)

    def test_daytrade0_buy_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[0].buy.quantity, 5)

    def test_daytrade0_sale_price_should_be_3(self):
        self.assertEqual(self.trade_container.daytrades[0].sale.price, 3)

    def test_daytrade0_sale_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.daytrades[0].sale.quantity, -5)

    def test_daytrade0_result_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[0].result, 5)

    def test_check_daytrade1_asset(self):
        self.assertEqual(self.trade_container.daytrades[1].asset, self.asset2)

    def test_daytrade1_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[1].quantity, 5)

    def test_daytrade1_buy_price_should_be_10(self):
        self.assertEqual(self.trade_container.daytrades[1].buy.price, 10)

    def test_daytrade1_buy_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[1].buy.quantity, 5)

    def test_daytrade1_sale_price_should_be_7(self):
        self.assertEqual(self.trade_container.daytrades[1].sale.price, 7)

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.daytrades[1].sale.quantity, -5)

    def test_daytrade1_result_should_be_5(self):
        self.assertEqual(self.trade_container.daytrades[1].result, -15)


class TestTradeContainer_add_to_existing_common_trade(unittest.TestCase):

    def setUp(self):
        asset = trade_tools.Asset('some asset')
        trade = trade_tools.Trade(
                    date='2015-09-21', asset=asset, quantity=10, price=2)
        self.trade_container = trade_tools.TradeContainer(trades=[trade])
        self.trade_container.identify_daytrades_and_common_trades()
        trade = trade_tools.Trade(
                    date='2015-09-21', asset=asset, quantity=10, price=4)
        self.trade_container.add_to_existing_common_trade(trade)

    def test_common_trades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.common_trades), 1)

    def test_daytrades_len_should_be_zero(self):
        self.assertEqual(len(self.trade_container.daytrades), 0)

    def test_common_trades0_quantity_should_be_20(self):
        self.assertEqual(self.trade_container.common_trades[0].quantity, 20)

    def test_common_trades0_price_should_be_3(self):
        self.assertEqual(self.trade_container.common_trades[0].price, 3)


class TestTradeContainer_rate_discounts_by_common_trades_and_daytrades(
        unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 1,
            'other discount': 3
        }
        self.asset1 = trade_tools.Asset('some asset')
        self.asset2 = trade_tools.Asset('some other asset')
        trade1 = trade_tools.Trade(
                date='2015-09-21', asset=self.asset1, quantity=10, price=2)
        trade2 = trade_tools.Trade(
                date='2015-09-21', asset=self.asset1, quantity=-5, price=3)
        trade3 = trade_tools.Trade(
                date='2015-09-21', asset=self.asset2, quantity=-5, price=7)
        self.trade_container = trade_tools.TradeContainer(
                trades=[trade1,trade2,trade3], discounts=discounts)
        self.trade_container.identify_daytrades_and_common_trades()
        self.trade_container.rate_discounts_by_common_trades_and_daytrades()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade_container_volume(self):
        self.assertEqual(self.trade_container.volume, 70)

    def test_check_daytrade0_buy_discounts(self):
        self.assertEqual(
            round(self.trade_container.daytrades[0].\
                    buy.discounts['some discount'], 2),
            0.14
        )
        self.assertEqual(
            round(self.trade_container.daytrades[0].\
                    buy.discounts['other discount'], 2),
            0.43
        )

    def test_check_daytrade0_sale_discounts(self):
        self.assertEqual(
            round(self.trade_container.daytrades[0].\
                    sale.discounts['some discount'], 2),
            0.21
        )
        self.assertEqual(
            round(self.trade_container.daytrades[0].\
                    sale.discounts['other discount'], 2),
            0.64
        )

    def test_check_common_trades0_asset(self):
        self.assertEqual(
            self.trade_container.common_trades[0].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_5(self):
        self.assertEqual(self.trade_container.common_trades[0].quantity, 5)

    def test_common_trades0_price_should_be_2(self):
        self.assertEqual(self.trade_container.common_trades[0].price, 2)

    def test_common_trades0_volume_should_be_35(self):
        self.assertEqual(self.trade_container.common_trades[0].volume, 10)

    def test_check_common_trades0_discounts(self):
        self.assertEqual(
            round(self.trade_container.common_trades[0].\
                    discounts['some discount'],2),
            0.14
        )
        self.assertEqual(
            round(self.trade_container.common_trades[0].\
                    discounts['other discount'], 2),
            0.43
        )

    def test_check_common_trades1_asset(self):
        self.assertEqual(
            self.trade_container.common_trades[1].asset,
            self.asset2
        )

    def test_common_trades1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.common_trades[1].quantity, -5)

    def test_common_trades1_price_should_be_7(self):
        self.assertEqual(self.trade_container.common_trades[1].price, 7)

    def test_common_trades1_volume_should_be_35(self):
        self.assertEqual(self.trade_container.common_trades[1].volume, 35)

    def test_check_common_trades1_discounts(self):
        expected_discounts = {
            'some discount': 0.5,
            'other discount': 1.5
        }
        self.assertEqual(
            self.trade_container.common_trades[1].discounts,
            expected_discounts
        )
