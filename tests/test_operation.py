from __future__ import absolute_import
from __future__ import division
import unittest

import trade as trade_tools


class TestTradeCreation(unittest.TestCase):
    """Test the creation of Operation objects."""

    def setUp(self):
        self.asset = trade_tools.Asset(name='some asset')
        self.trade = trade_tools.Operation(
			date='2015-09-18',
			asset=self.asset,
			quantity=20,
			price=10,
			commissions={
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
        self.assertEqual(self.trade.commissions, discounts)


class TestTrade_total_discounts(unittest.TestCase):
    """Test the total_commission property of Operation objects."""

    def setUp(self):
        self.asset = trade_tools.Asset(name='some asset')

    def test_trade_total_discounts_with_one_discount(self):
        trade = trade_tools.Operation(
            quantity=1,
            price=1,
            commissions={
                'some discount': 3
            }
        )
        self.assertEqual(trade.total_commission, 3)

    def test_trade_total_discounts_with_multiple_discounts_case_1(self):
        trade = trade_tools.Operation(
            quantity=1,
            price=1,
            commissions={
                'some discount': 3,
                'other discount': 1
            }
        )
        self.assertEqual(trade.total_commission, 4)

    def test_trade_total_discounts_with_multiple_discounts_case_2(self):
        trade = trade_tools.Operation(
            quantity=1,
            price=1,
            commissions={
                'some discount': 3,
                'other discount': 1,
                'more discounts': 2
            }
        )
        self.assertEqual(trade.total_commission, 6)

    def test_trade_total_discounts_with_multiple_discounts_case_3(self):
        trade = trade_tools.Operation(
            quantity=1,
            price=1,
            commissions={
                'some discount': 3,
                'other discount': 1,
                'negative discount': -1
            }
        )
        self.assertEqual(trade.total_commission, 3)


class TestTrade_real_price(unittest.TestCase):
    """Test the real_price property of Operation objects.

    The real price of an operation (the real unitary price of the
    asset) if the operation's price with all rated commissions
    and taxes.
    """

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
            commissions={
                'some discount': 3
            }
        )
        self.assertEqual(trade.real_price, 10.15)

    def test_trade_real_price_with_multiple_discounts_case_1(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=20,
            commissions={
                'some discount': 3,
                'other discount': 1
            }
        )
        self.assertEqual(trade.real_price, 10.2)

    def test_trade_real_price_with_multiple_discounts_case_2(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=20,
            commissions={
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
            commissions={
                'some discount': 3,
                'other discount': 1,
                'negative discount': -1
            }
        )
        self.assertEqual(trade.real_price, 10.15)


class TestTrade_real_real_value(unittest.TestCase):
    """Test the real_value property of Operation objects.

    The real value of an operation is its value (quantity*price)
    with all commissions and taxes considered.
    """

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
            commissions={
                'some discount': 3
            }
        )
        self.assertEqual(trade.real_value, 203)

    def test_trade_real_value_with_multiple_discounts_case_1(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=20,
            commissions={
                'some discount': 3,
                'other discount': 1
            }
        )
        self.assertEqual(trade.real_value, 204)

    def test_trade_real_value_with_multiple_discounts_case_2(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=20,
            commissions={
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
            commissions={
                'some discount': 3,
                'other discount': 1,
                'negative discount': -1
            }
        )
        self.assertEqual(trade.real_value, 203)


class TestTrade_volume(unittest.TestCase):
    """Test the volume property of Operation objects.

    The volume of the operation is its absolute quantity * its price.
    """

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

    def test_sale_volume_should_be_200_with_commissions_and_taxes(self):
        trade = trade_tools.Operation(
            price=10,
            quantity=-20,
            commissions = {
                'brokerage': 2,
                'some tax': 1.5,
                'other tax': 1,
            },
			taxes={
                'some tax': 0.005,
    			'some other tax': 0.0275
            }
        )
        self.assertEqual(trade.volume, 200)


class TestTrade_total_tax_value_Case_00(unittest.TestCase):
    """Test the total_tax_value property of Operation objects.

    In this TestCase we define multiple taxes.
    """

    def setUp(self):
        self.asset = trade_tools.Asset(name='some asset')
        self.trade = trade_tools.Operation(
			date='2015-09-18',
			asset=self.asset,
			quantity=10,
			price=10,
            commissions = {
                'brokerage': 2,
                'some tax': 1.5,
                'other tax': 1,
            },
			taxes={
                'some tax': 0.005,
    			'some other tax': 0.0275
            }
        )

    def test_trade_exists(self):
        self.assertTrue(self.trade)

    def test_trade_asset(self):
        self.assertEqual(self.trade.asset, self.asset)

    def test_trade_date_should_be_2015_09_18(self):
        self.assertEqual(self.trade.date, '2015-09-18')

    def test_trade_quantity_should_be_20(self):
        self.assertEqual(self.trade.quantity, 10)

    def test_trade_price_should_be_10(self):
        self.assertEqual(self.trade.price, 10)

    def test_trade_commissions_dict(self):
        commissions = {
            'brokerage': 2,
            'some tax': 1.5,
            'other tax': 1,
        }
        self.assertEqual(self.trade.commissions, commissions)

    def test_trade_taxes_dict(self):
        taxes={
            'some tax': 0.005,
            'some other tax': 0.0275
        }
        self.assertEqual(self.trade.taxes, taxes)

    def test_trade_total_tax_value(self):
        self.assertEqual(round(self.trade.total_tax_value, 8), 0.03250000)

    def test_trade_real_price(self):
        self.assertEqual(round(self.trade.real_price, 8), 10.45325000)

    def test_trade_real_value(self):
        self.assertEqual(round(self.trade.real_value, 8), 104.532500)
