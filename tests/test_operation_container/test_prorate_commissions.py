from __future__ import absolute_import
import unittest

import trade


class TestTradeContainer_rate_discounts_by_trade_case_00(unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        asset = trade.Asset('some asset')
        self.operation = trade.Operation(
                            date='2015-09-21',
                            asset=asset,
                            quantity=-10,
                            price=2
                        )
        self.container = trade.OperationContainer(
                                    operations=[self.operation],
                                    commissions=discounts
                                )

    def test_trade_container_should_exist(self):
        self.assertTrue(self.container)

    def test_check_trade_discount(self):
        expected_discounts = {
            'some discount': 1,
        }
        trade.prorate_commissions_by_operation(self.container, self.operation)
        self.assertEqual(self.operation.commissions, expected_discounts)


class TestTradeContainer_rate_discounts_by_trade_case_01(unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        asset = trade.Asset('some asset')
        self.operation1 = trade.Operation(
                            date='2015-09-21',
                            asset=asset,
                            quantity=-10,
                            price=2
                        )
        self.operation2 = trade.Operation(
                            date='2015-09-21',
                            asset=asset,
                            quantity=-10,
                            price=2
                        )
        self.container = trade.OperationContainer(
                                    operations=[
                                        self.operation1,
                                        self.operation2
                                    ],
                                    commissions=discounts
                                )

    def test_trade_container_should_exist(self):
        self.assertTrue(self.container)

    def test_check_trade1_discount(self):
        expected_discounts = {
            'some discount': 0.5,
        }
        trade.prorate_commissions_by_operation(self.container, self.operation1)
        self.assertEqual(self.operation1.commissions, expected_discounts)

    def test_check_trade2_discount(self):
        expected_discounts = {
            'some discount': 0.5,
        }
        trade.prorate_commissions_by_operation(self.container, self.operation2)
        self.assertEqual(self.operation2.commissions, expected_discounts)


class TestTradeContainer_rate_discounts_by_trade_case_02(unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        asset = trade.Asset('some asset')
        self.operation1 = trade.Operation(
                            date='2015-09-21',
                            asset=asset,
                            quantity=-10,
                            price=2
                        )
        self.operation2 = trade.Operation(
                            date='2015-09-21',
                            asset=asset,
                            quantity=-20,
                            price=2
                        )
        self.container = trade.OperationContainer(
                                    operations=[
                                        self.operation1,
                                        self.operation2
                                    ],
                                    commissions=discounts
                                )

    def test_trade_container_should_exist(self):
        self.assertTrue(self.container)

    def test_check_trade1_discount(self):
        trade.prorate_commissions_by_operation(self.container, self.operation1)
        self.assertEqual(
            round(self.operation1.commissions['some discount'], 8),
            0.33333333
        )

    def test_check_trade2_discount(self):
        trade.prorate_commissions_by_operation(self.container, self.operation2)
        self.assertEqual(
            round(self.operation2.commissions['some discount'], 8),
            0.66666667
        )


class TestTradeContainer_rate_discounts_by_trade_case_03(unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 4,
        }
        asset1 = trade.Asset('some asset')
        asset2 = trade.Asset('some other asset')
        self.operation1 = trade.Operation(
                            date='2015-09-21',
                            asset=asset1,
                            quantity=-10,
                            price=2
                        )
        self.operation2 = trade.Operation(
                            date='2015-09-21',
                            asset=asset1,
                            quantity=-20,
                            price=2
                        )
        self.operation3 = trade.Operation(
                            date='2015-09-21',
                            asset=asset2,
                            quantity=-10,
                            price=2
                        )
        self.container = trade.OperationContainer(
                                    operations=[
                                                self.operation1,
                                                self.operation2,
                                                self.operation3
                                                ],
                                    commissions=discounts
                                )

    def test_trade_container_should_exist(self):
        self.assertTrue(self.container)

    def test_check_trade1_discount(self):
        trade.prorate_commissions_by_operation(self.container, self.operation1)
        self.assertEqual(self.operation1.commissions['some discount'], 1)

    def test_check_trade2_discount(self):
        trade.prorate_commissions_by_operation(self.container, self.operation2)
        self.assertEqual(self.operation2.commissions['some discount'], 2)

    def test_check_trade3_discount(self):
        trade.prorate_commissions_by_operation(self.container, self.operation3)
        self.assertEqual(self.operation3.commissions['some discount'], 1)


class TestTradeContainer_prorate_discounts_by_common_trades_and_daytrades(
        unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 1,
            'other discount': 3
        }
        self.asset1 = trade.Asset('some asset')
        self.asset2 = trade.Asset('some other asset')
        trade1 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=10,
                    price=2
                )
        trade2 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=3
                )
        trade3 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=-5,
                    price=7
                )
        self.container = trade.OperationContainer(
                                    operations=[trade1,trade2,trade3],
                                    commissions=discounts
                                )
        trade.identify_daytrades_and_common_operations(self.container)
        trade.prorate_commissions(self.container)

    def test_trade_container_should_exist(self):
        self.assertTrue(self.container)

    def test_check_trade_container_volume(self):
        self.assertEqual(self.container.volume, 70)

    def test_check_daytrade0_buy_discounts(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][self.asset1].\
                    purchase.commissions['some discount'], 2),
            0.14
        )
        self.assertEqual(
            round(self.container.positions['daytrades'][self.asset1].\
                    purchase.commissions['other discount'], 2),
            0.43
        )

    def test_check_daytrade0_sale_discounts(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][self.asset1].\
                    sale.commissions['some discount'], 2),
            0.21
        )
        self.assertEqual(
            round(self.container.positions['daytrades'][self.asset1].\
                    sale.commissions['other discount'], 2),
            0.64
        )

    def test_check_common_trades0_asset(self):
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_5(self):
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].quantity,
            5
        )

    def test_common_trades0_price_should_be_2(self):
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].price,
            2
        )

    def test_common_trades0_volume_should_be_35(self):
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].volume,
            10
        )

    def test_check_common_trades0_discounts(self):
        self.assertEqual(
            round(self.container.positions['common operations'][self.asset1].\
                    commissions['some discount'],2),
            0.14
        )
        self.assertEqual(
            round(self.container.positions['common operations'][self.asset1].\
                    commissions['other discount'], 2),
            0.43
        )

    def test_check_common_trades1_asset(self):
        self.assertEqual(
            self.container.positions['common operations'][self.asset2].asset,
            self.asset2
        )

    def test_common_trades1_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.container.positions['common operations'][self.asset2].quantity,
            -5
        )

    def test_common_trades1_price_should_be_7(self):
        self.assertEqual(
            self.container.positions['common operations'][self.asset2].price,
            7
        )

    def test_common_trades1_volume_should_be_35(self):
        self.assertEqual(
            self.container.positions['common operations'][self.asset2].volume,
            35
        )

    def test_check_common_trades1_discounts(self):
        expected_discounts = {
            'some discount': 0.5,
            'other discount': 1.5
        }
        self.assertEqual(
            self.container.positions['common operations'][self.asset2].commissions,
            expected_discounts
        )
