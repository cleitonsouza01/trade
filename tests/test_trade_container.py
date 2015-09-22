from __future__ import absolute_import
import unittest
import decimal
decimal.getcontext().prec = 8

from trade_tools import trade_tools


class TestTradeContainerCreation(unittest.TestCase):

    def setUp(self):
        self.trade_container = trade_tools.TradeContainer()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

class TestTradeContainer_total_discount_value_one_discount(unittest.TestCase):

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


class TestTradeContainer_total_discount_value_multiple_discounts(unittest.TestCase):

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
        trade = trade_tools.Trade(date='2015-09-21', asset=asset, quantity=10, price=2)
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
        trade1 = trade_tools.Trade(date='2015-09-21', asset=asset, quantity=10, price=2)
        trade2 = trade_tools.Trade(date='2015-09-21', asset=asset, quantity=5, price=1)
        self.trade_container = trade_tools.TradeContainer(trades=[trade1,trade2])

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trade_container_trades_should_have_one_trade(self):
        self.assertEqual(len(self.trade_container.trades), 2)

    def test_trade_container_volume_should_be_20(self):
        self.assertEqual(self.trade_container.volume, 25)


class TestTradeContainer_volume_multiple_trades_case_01(unittest.TestCase):

    def setUp(self):
        asset = trade_tools.Asset('some asset')
        trade1 = trade_tools.Trade(date='2015-09-21', asset=asset, quantity=-10, price=2)
        trade2 = trade_tools.Trade(date='2015-09-21', asset=asset, quantity=5, price=1)
        self.trade_container = trade_tools.TradeContainer(trades=[trade1,trade2])

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
        trade1 = trade_tools.Trade(date='2015-09-21', asset=asset1, quantity=-10, price=2)
        trade2 = trade_tools.Trade(date='2015-09-21', asset=asset1, quantity=5, price=1)
        trade3 = trade_tools.Trade(date='2015-09-21', asset=asset2, quantity=20, price=5)
        self.trade_container = trade_tools.TradeContainer(trades=[trade1,trade2,trade3])

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
        self.trade = trade_tools.Trade(date='2015-09-21', asset=asset, quantity=-10, price=2)
        self.trade_container = trade_tools.TradeContainer(trades=[self.trade], discounts=discounts)

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
        self.trade1 = trade_tools.Trade(date='2015-09-21', asset=asset, quantity=-10, price=2)
        self.trade2 = trade_tools.Trade(date='2015-09-21', asset=asset, quantity=-10, price=2)
        self.trade_container = trade_tools.TradeContainer(trades=[self.trade1,self.trade2], discounts=discounts)

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
        self.trade1 = trade_tools.Trade(date='2015-09-21', asset=asset, quantity=-10, price=2)
        self.trade2 = trade_tools.Trade(date='2015-09-21', asset=asset, quantity=-20, price=2)
        self.trade_container = trade_tools.TradeContainer(trades=[self.trade1,self.trade2], discounts=discounts)

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade1_discount(self):
        self.trade_container.rate_discounts_by_trade(self.trade1)
        self.assertEqual(round(self.trade1.discounts['some discount'], 8), 0.33333333)

    def test_check_trade2_discount(self):
        self.trade_container.rate_discounts_by_trade(self.trade2)
        self.assertEqual(round(self.trade2.discounts['some discount'], 8), 0.66666667)


class TestTradeContainer_rate_discounts_by_trade_case_03(unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 4,
        }
        asset1 = trade_tools.Asset('some asset')
        asset2 = trade_tools.Asset('some other asset')
        self.trade1 = trade_tools.Trade(date='2015-09-21', asset=asset1, quantity=-10, price=2)
        self.trade2 = trade_tools.Trade(date='2015-09-21', asset=asset1, quantity=-20, price=2)
        self.trade3 = trade_tools.Trade(date='2015-09-21', asset=asset2, quantity=-10, price=2)
        self.trade_container = trade_tools.TradeContainer(trades=[self.trade1,self.trade2, self.trade3], discounts=discounts)

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
