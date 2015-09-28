from __future__ import absolute_import
import unittest

import trade as trade_tools


# TODO document this
# TODO more tests


class TaxManagerForTests:
    def get_fees_for_operation(self, operation):
        return {}

    def get_fees_for_daytrade(self, operation):
        return {
            'emoluments': 0.005,
            'liquidation': 0.02,
            'registry': 0,
        }


class TestTradeContainer_fetch_positions_case_00(unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 1,
            'other discount': 3
        }
        self.asset1 = trade_tools.Asset('some asset')
        self.asset2 = trade_tools.Asset('some other asset')
        trade1 = trade_tools.Operation(
                date='2015-09-21', asset=self.asset1, quantity=10, price=2)
        trade2 = trade_tools.Operation(
                date='2015-09-21', asset=self.asset1, quantity=-5, price=3)
        trade3 = trade_tools.Operation(
                date='2015-09-21', asset=self.asset2, quantity=-5, price=7)
        self.trade_container = trade_tools.OperationContainer(
                operations=[trade1,trade2,trade3], fixed_commissions=discounts)
        self.trade_container.fetch_positions()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade_container_volume(self):
        self.assertEqual(self.trade_container.volume, 70)

    def test_check_daytrade0_buy_discounts(self):
        self.assertEqual(
            round(self.trade_container.daytrades[self.asset1].\
                    purchase.fixed_commissions['some discount'], 2),
            0.14
        )
        self.assertEqual(
            round(self.trade_container.daytrades[self.asset1].\
                    purchase.fixed_commissions['other discount'], 2),
            0.43
        )

    def test_check_daytrade0_sale_discounts(self):
        self.assertEqual(
            round(self.trade_container.daytrades[self.asset1].\
                    sale.fixed_commissions['some discount'], 2),
            0.21
        )
        self.assertEqual(
            round(self.trade_container.daytrades[self.asset1].\
                    sale.fixed_commissions['other discount'], 2),
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
                    fixed_commissions['some discount'],2),
            0.14
        )
        self.assertEqual(
            round(self.trade_container.common_operations[self.asset1].\
                    fixed_commissions['other discount'], 2),
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
            self.trade_container.common_operations[self.asset2].fixed_commissions,
            expected_discounts
        )


class TestTradeContainer_fetch_positions_case_01(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade_tools.Asset('some asset')
        self.asset2 = trade_tools.Asset('some other asset')
        self.asset3 = trade_tools.Asset('even other asset')
        trade1 = trade_tools.Operation(
            date='2015-09-21', asset=self.asset1, quantity=10, price=2)
        trade2 = trade_tools.Operation(
            date='2015-09-21', asset=self.asset1, quantity=-5, price=3)
        trade3 = trade_tools.Operation(
            date='2015-09-21', asset=self.asset2, quantity=-5, price=7)
        trade4 = trade_tools.Operation(
            date='2015-09-21', asset=self.asset2, quantity=5, price=10)
        trade5 = trade_tools.Operation(
            date='2015-09-21', asset=self.asset1, quantity=5, price=4)

        trade6 = trade_tools.Operation(
            date='2015-09-21', asset=self.asset3, quantity=5, price=4)
        trade7 = trade_tools.Operation(
            date='2015-09-21', asset=self.asset3, quantity=-5, price=2)

        trade8 = trade_tools.Operation(
            date='2015-09-21', asset=self.asset3, quantity=5, price=4)
        trade9 = trade_tools.Operation(
            date='2015-09-21', asset=self.asset3, quantity=-5, price=4)

        self.trade_container = trade_tools.OperationContainer(
            operations=[
                trade1,trade2,trade3,trade4,trade5,trade6,trade7,trade8,trade9
            ]
        )
        self.trade_container.fetch_positions()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_five(self):
        self.assertEqual(len(self.trade_container.operations), 9)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.trade_container.operations[1].price, 3)

    def test_common_trades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.common_operations.keys()), 1)

    def test_check_common_trades0_asset(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_10(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].quantity,
            10
        )

    def test_common_trades0_price_should_be_3(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].price,
            3
        )

    def test_daytrades_len_should_be_3(self):
        self.assertEqual(
            len(self.trade_container.daytrades.keys()),
            3
        )

    def test_check_daytrade0_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].asset,
            self.asset1
        )

    def test_daytrade0_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].quantity,
            5
        )

    def test_daytrade0_buy_price_should_be_2(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].purchase.price,
            2
        )

    def test_daytrade0_buy_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].purchase.quantity,
            5
        )

    def test_daytrade0_sale_price_should_be_3(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].sale.price,
            3
        )

    def test_daytrade0_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].sale.quantity,
            -5
        )

    def test_daytrade0_result_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].result,
            5
        )

    def test_check_daytrade1_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].asset,
            self.asset2
        )

    def test_daytrade1_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].quantity,
            5
        )

    def test_daytrade1_buy_price_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].purchase.price,
            10
        )

    def test_daytrade1_buy_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].purchase.quantity,
            5
        )

    def test_daytrade1_sale_price_should_be_7(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].sale.price,
            7
        )

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].sale.quantity,
            -5
        )

    def test_daytrade1_result_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].result,
            -15
        )


    def test_check_daytrade2_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset3].asset,
            self.asset3
        )

    def test_daytrade2_quantity_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset3].quantity,
            10
        )

    def test_daytrade2_buy_price_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset3].purchase.price,
            4
        )

    def test_daytrade2_buy_quantity_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset3].purchase.quantity,
            10
        )

    def test_daytrade2_sale_price_should_be_3(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset3].sale.price,
            3
        )

    def test_daytrade2_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset3].sale.quantity,
            -10
        )








class TestTradeContainer_fetch_positions_case_02(unittest.TestCase):
    """ Daytrades, commissions and taxes."""

    def setUp(self):

        containers = []
        container_operations = []
        self.asset = trade_tools.Asset('PETR4')

        # NOTA 2
        date='2015-02-03'
        operations = []
        operations.append(
            trade_tools.Operation(
                date=date,
                asset=self.asset,
                quantity=10,
                price=10
            )
        )
        operations.append(
            trade_tools.Operation(
                date=date,
                asset=self.asset,
                quantity=-10,
                price=10
            )
        )
        commissions = {
            'corretagem': 2,
            'iss': 1.5,
            'outros': 1,
        }
        self.container = trade_tools.OperationContainer(
            operations=operations,
            fixed_commissions=commissions
        )
        self.container.tax_manager = TaxManagerForTests()
        self.container.fetch_positions()

    def test_container_daytrade_buy_operation_discounts(self):
        discounts = {
            'corretagem': 1,
            'iss': 0.75,
            'outros': 0.5,
        }
        self.assertEqual(
            self.container.daytrades[self.asset].purchase.fixed_commissions,
            discounts
        )

    def test_container_daytrade_buy_sale_operation_discounts(self):
        discounts = {
            'corretagem': 1,
            'iss': 0.75,
            'outros': 0.5,
        }
        self.assertEqual(
            self.container.daytrades[self.asset].sale.fixed_commissions,
            discounts
        )

    def test_container_daytrade_buy_operation_taxes(self):
        taxes = {
            'emoluments': 0.005,
            'liquidation': 0.02,
            'registry': 0,
        }
        self.assertEqual(
            self.container.daytrades[self.asset].purchase.taxes,
            taxes
        )

    def test_container_daytrade_sale_operation_taxes(self):
        taxes = {
            'emoluments': 0.005,
            'liquidation': 0.02,
            'registry': 0,
        }
        self.assertEqual(self.container.daytrades[self.asset].sale.taxes, taxes)

    def test_container_daytrade_operation_result(self):
        self.assertEqual(
            round(self.container.daytrades[self.asset].result,8),
            -4.55000000
        )

    def test_container_daytrade_operation_quantity(self):
        self.assertEqual(self.container.daytrades[self.asset].quantity, 10)

    def test_container_daytrade_buy_operation_real_price(self):
        self.assertEqual(
            round(self.container.daytrades[self.asset].purchase.real_price,8),
            10.22750000
        )

    def test_container_daytrade_sale_operation_real_price(self):
        self.assertEqual(
            round(self.container.daytrades[self.asset].sale.real_price,8),
            9.77250000
        )

    def test_container_daytrade_buy_operation_real_value(self):
        self.assertEqual(
            round(self.container.daytrades[self.asset].purchase.real_value,8),
            102.27500000
        )

    def test_container_daytrade_sale_operation_real_value(self):
        self.assertEqual(
            round(self.container.daytrades[self.asset].sale.real_value,8),
            -97.72500000
        )
