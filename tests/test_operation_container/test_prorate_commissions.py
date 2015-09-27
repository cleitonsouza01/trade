from __future__ import absolute_import
import unittest

import trade as trade_tools


# TODO document this
# TODO more tests


class TestTradeContainer_rate_discounts_by_trade_case_00(unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        asset = trade_tools.Asset('some asset')
        self.trade = trade_tools.Operation(
            date='2015-09-21', asset=asset, quantity=-10, price=2)
        self.trade_container = trade_tools.OperationContainer(
            operations=[self.trade], commissions=discounts)

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade_discount(self):
        expected_discounts = {
            'some discount': 1,
        }
        self.trade_container.prorate_commissions_by_operation(self.trade)
        self.assertEqual(self.trade.commissions, expected_discounts)


class TestTradeContainer_rate_discounts_by_trade_case_01(unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        asset = trade_tools.Asset('some asset')
        self.trade1 = trade_tools.Operation(
            date='2015-09-21', asset=asset, quantity=-10, price=2)
        self.trade2 = trade_tools.Operation(
            date='2015-09-21', asset=asset, quantity=-10, price=2)
        self.trade_container = trade_tools.OperationContainer(
            operations=[self.trade1,self.trade2], commissions=discounts)

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade1_discount(self):
        expected_discounts = {
            'some discount': 0.5,
        }
        self.trade_container.prorate_commissions_by_operation(self.trade1)
        self.assertEqual(self.trade1.commissions, expected_discounts)

    def test_check_trade2_discount(self):
        expected_discounts = {
            'some discount': 0.5,
        }
        self.trade_container.prorate_commissions_by_operation(self.trade2)
        self.assertEqual(self.trade2.commissions, expected_discounts)


class TestTradeContainer_rate_discounts_by_trade_case_02(unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        asset = trade_tools.Asset('some asset')
        self.trade1 = trade_tools.Operation(
            date='2015-09-21', asset=asset, quantity=-10, price=2)
        self.trade2 = trade_tools.Operation(
            date='2015-09-21', asset=asset, quantity=-20, price=2)
        self.trade_container = trade_tools.OperationContainer(
            operations=[self.trade1,self.trade2], commissions=discounts)

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade1_discount(self):
        self.trade_container.prorate_commissions_by_operation(self.trade1)
        self.assertEqual(
            round(self.trade1.commissions['some discount'], 8),
            0.33333333
        )

    def test_check_trade2_discount(self):
        self.trade_container.prorate_commissions_by_operation(self.trade2)
        self.assertEqual(
            round(self.trade2.commissions['some discount'], 8),
            0.66666667
        )


class TestTradeContainer_rate_discounts_by_trade_case_03(unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 4,
        }
        asset1 = trade_tools.Asset('some asset')
        asset2 = trade_tools.Asset('some other asset')
        self.trade1 = trade_tools.Operation(
            date='2015-09-21', asset=asset1, quantity=-10, price=2)
        self.trade2 = trade_tools.Operation(
            date='2015-09-21', asset=asset1, quantity=-20, price=2)
        self.trade3 = trade_tools.Operation(
            date='2015-09-21', asset=asset2, quantity=-10, price=2)
        self.trade_container = trade_tools.OperationContainer(
                            operations=[self.trade1,self.trade2, self.trade3],
                            commissions=discounts
                        )

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade1_discount(self):
        self.trade_container.prorate_commissions_by_operation(self.trade1)
        self.assertEqual(self.trade1.commissions['some discount'], 1)

    def test_check_trade2_discount(self):
        self.trade_container.prorate_commissions_by_operation(self.trade2)
        self.assertEqual(self.trade2.commissions['some discount'], 2)

    def test_check_trade3_discount(self):
        self.trade_container.prorate_commissions_by_operation(self.trade3)
        self.assertEqual(self.trade3.commissions['some discount'], 1)


class TestTradeContainer_prorate_discounts_by_common_trades_and_daytrades(
        unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 1,
            'other discount': 3
        }
        self.asset1 = trade_tools.Asset('some asset')
        self.asset2 = trade_tools.Asset('some other asset')
        trade1 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=10,
                    price=2
                )
        trade2 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=3
                )
        trade3 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=-5,
                    price=7
                )
        self.trade_container = trade_tools.OperationContainer(
                                    operations=[trade1,trade2,trade3],
                                    commissions=discounts
                                )
        self.trade_container.identify_daytrades_and_common_operations()
        self.trade_container\
            .prorate_commissions_by_daytrades_and_common_operations()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade_container_volume(self):
        self.assertEqual(self.trade_container.volume, 70)

    def test_check_daytrade0_buy_discounts(self):
        self.assertEqual(
            round(self.trade_container.daytrades[self.asset1].\
                    purchase.commissions['some discount'], 2),
            0.14
        )
        self.assertEqual(
            round(self.trade_container.daytrades[self.asset1].\
                    purchase.commissions['other discount'], 2),
            0.43
        )

    def test_check_daytrade0_sale_discounts(self):
        self.assertEqual(
            round(self.trade_container.daytrades[self.asset1].\
                    sale.commissions['some discount'], 2),
            0.21
        )
        self.assertEqual(
            round(self.trade_container.daytrades[self.asset1].\
                    sale.commissions['other discount'], 2),
            0.64
        )

    def test_check_common_trades0_asset(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].quantity,
            5
        )

    def test_common_trades0_price_should_be_2(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].price,
            2
        )

    def test_common_trades0_volume_should_be_35(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].volume,
            10
        )

    def test_check_common_trades0_discounts(self):
        self.assertEqual(
            round(self.trade_container.common_operations[self.asset1].\
                    commissions['some discount'],2),
            0.14
        )
        self.assertEqual(
            round(self.trade_container.common_operations[self.asset1].\
                    commissions['other discount'], 2),
            0.43
        )

    def test_check_common_trades1_asset(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset2].asset,
            self.asset2
        )

    def test_common_trades1_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset2].quantity,
            -5
        )

    def test_common_trades1_price_should_be_7(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset2].price,
            7
        )

    def test_common_trades1_volume_should_be_35(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset2].volume,
            35
        )

    def test_check_common_trades1_discounts(self):
        expected_discounts = {
            'some discount': 0.5,
            'other discount': 1.5
        }
        self.assertEqual(
            self.trade_container.common_operations[self.asset2].commissions,
            expected_discounts
        )
