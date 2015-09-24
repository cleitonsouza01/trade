from __future__ import absolute_import
import unittest

import trade as trade_tools


# TODO document this


class TestTradeCreation(unittest.TestCase):

    def setUp(self):
        self.asset = trade_tools.Asset(name='some asset')
        self.trade = trade_tools.Operation(
			date='2015-09-18',
			asset=self.asset,
			quantity=20,
			price=10,
			comissions={
                'some discount': 3
            }
        )

    def test_trade_exists(self):
        self.assertTrue(self.trade)

    def test_trade_asset(self):
        self.assertEqual(self.trade.asset, self.asset)

    def test_trade_date_should_be_2015_09_18(self):
        self.assertEqual(self.trade.date, '2015-09-18')

    def test_trade_quantity_should_be_20(self):
        self.assertEqual(self.trade.quantity, 20)

    def test_trade_price_should_be_10(self):
        self.assertEqual(self.trade.price, 10)

    def test_trade_discounts_dict(self):
        discounts={
            'some discount': 3
        }
        self.assertEqual(self.trade.comissions, discounts)


class TestTrade_total_discounts(unittest.TestCase):

    def setUp(self):
        self.asset = trade_tools.Asset(name='some asset')

    def test_trade_total_discounts_with_one_discount(self):
        trade = trade_tools.Operation(
            quantity=1,
            price=1,
            comissions={
                'some discount': 3
            }
        )
        self.assertEqual(trade.total_comission, 3)

    def test_trade_total_discounts_with_multiple_discounts_case_1(self):
        trade = trade_tools.Operation(
            quantity=1,
            price=1,
            comissions={
                'some discount': 3,
                'other discount': 1
            }
        )
        self.assertEqual(trade.total_comission, 4)

    def test_trade_total_discounts_with_multiple_discounts_case_2(self):
        trade = trade_tools.Operation(
            quantity=1,
            price=1,
            comissions={
                'some discount': 3,
                'other discount': 1,
                'more discounts': 2
            }
        )
        self.assertEqual(trade.total_comission, 6)

    def test_trade_total_discounts_with_multiple_discounts_case_3(self):
        trade = trade_tools.Operation(
            quantity=1,
            price=1,
            comissions={
                'some discount': 3,
                'other discount': 1,
                'negative discount': -1
            }
        )
        self.assertEqual(trade.total_comission, 3)


class TestTrade_real_price(unittest.TestCase):

    def setUp(self):
        self.asset = trade_tools.Asset(name='some asset')

    def test_real_price_with_no_discount(self):
        trade = trade_tools.Operation(
			price=10,
            quantity=20
        )
        self.assertEqual(trade.real_price, 10)

    def test_real_price_with_one_discount(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=20,
            comissions={
                'some discount': 3
            }
        )
        self.assertEqual(trade.real_price, 10.15)

    def test_trade_real_price_with_multiple_discounts_case_1(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=20,
            comissions={
                'some discount': 3,
                'other discount': 1
            }
        )
        self.assertEqual(trade.real_price, 10.2)

    def test_trade_real_price_with_multiple_discounts_case_2(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=20,
            comissions={
                'some discount': 3,
                'other discount': 1,
                'more discounts': 2
            }
        )
        self.assertEqual(trade.real_price, 10.3)

    def test_trade_real_price_with_multiple_discounts_case_3(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=20,
            comissions={
                'some discount': 3,
                'other discount': 1,
                'negative discount': -1
            }
        )
        self.assertEqual(trade.real_price, 10.15)


class TestTrade_real_real_value(unittest.TestCase):

    def setUp(self):
        self.asset = trade_tools.Asset(name='some asset')

    def test_real_price_with_no_discount(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=20
        )
        self.assertEqual(trade.real_value, 200)

    def test_real_value_with_one_discount(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=20,
            comissions={
                'some discount': 3
            }
        )
        self.assertEqual(trade.real_value, 203)

    def test_trade_real_value_with_multiple_discounts_case_1(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=20,
            comissions={
                'some discount': 3,
                'other discount': 1
            }
        )
        self.assertEqual(trade.real_value, 204)

    def test_trade_real_value_with_multiple_discounts_case_2(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=20,
            comissions={
                'some discount': 3,
                'other discount': 1,
                'more discounts': 2
            }
        )
        self.assertEqual(trade.real_value, 206)

    def test_trade_real_value_with_multiple_discounts_case_3(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=20,
            comissions={
                'some discount': 3,
                'other discount': 1,
                'negative discount': -1
            }
        )
        self.assertEqual(trade.real_value, 203)


class TestTrade_volume(unittest.TestCase):

    def test_volume_should_be_100(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=10
        )
        self.assertEqual(trade.volume, 100)

    def test_purchase_volume_should_be_200(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=20
        )
        self.assertEqual(trade.volume, 200)

    def test_sale_volume_should_be_200(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=-20
        )
        self.assertEqual(trade.volume, 200)
