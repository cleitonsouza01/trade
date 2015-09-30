from __future__ import absolute_import
import unittest

import trade


class TaxManagerForTests:

    def get_rates_for_operation(self, operation, operation_type):
        if operation_type == 'daytrades':
            return {
                'emoluments': 0.005,
                'liquidation': 0.02,
                'registry': 0,
            }
        return {}


class TestTradeContainer_fetch_positions_case_00(unittest.TestCase):

    def setUp(self):
        discounts = {
            'some discount': 1,
            'other discount': 3
        }
        self.asset1 = trade.Asset('some asset')
        self.asset2 = trade.Asset('some other asset')
        operation1 = trade.Operation(
                        date='2015-09-21',
                        asset=self.asset1,
                        quantity=10,
                        price=2
                    )
        operation2 = trade.Operation(
                        date='2015-09-21',
                        asset=self.asset1,
                        quantity=-5,
                        price=3
                    )
        operation3 = trade.Operation(
                        date='2015-09-21',
                        asset=self.asset2,
                        quantity=-5,
                        price=7
                    )
        self.container = trade.OperationContainer(
                                operations=[operation1,operation2,operation3],
                                commissions=discounts
                            )
        self.container.fetch_positions_tasks = [
            trade.get_operations_from_exercises,
            trade.identify_daytrades_and_common_operations,
            trade.prorate_commissions,
            trade.find_rates_for_positions,
        ]
        self.container.fetch_positions()

    def test_container_should_exist(self):
        self.assertTrue(self.container)

    def test_check_container_volume(self):
        self.assertEqual(self.container.volume, 70)

    def test_check_daytrade0_buy_discounts(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][self.asset1].\
                    operations[0].commissions['some discount'], 2),
            0.14
        )
        self.assertEqual(
            round(self.container.positions['daytrades'][self.asset1].\
                    operations[0].commissions['other discount'], 2),
            0.43
        )

    def test_check_daytrade0_sale_discounts(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][self.asset1].\
                    operations[1].commissions['some discount'], 2),
            0.21
        )
        self.assertEqual(
            round(self.container.positions['daytrades'][self.asset1].\
                    operations[1].commissions['other discount'], 2),
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


class TestTradeContainer_fetch_positions_case_01(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade.Asset('some asset')
        self.asset2 = trade.Asset('some other asset')
        self.asset3 = trade.Asset('even other asset')
        operation1 = trade.Operation(
                        date='2015-09-21',
                        asset=self.asset1,
                        quantity=10,
                        price=2
                    )
        operation2 = trade.Operation(
                        date='2015-09-21',
                        asset=self.asset1,
                        quantity=-5,
                        price=3
                    )
        operation3 = trade.Operation(
                        date='2015-09-21',
                        asset=self.asset2,
                        quantity=-5,
                        price=7
                    )
        operation4 = trade.Operation(
                        date='2015-09-21',
                        asset=self.asset2,
                        quantity=5,
                        price=10
                    )
        operation5 = trade.Operation(
                        date='2015-09-21',
                        asset=self.asset1,
                        quantity=5,
                        price=4
                    )
        operation6 = trade.Operation(
                        date='2015-09-21',
                        asset=self.asset3,
                        quantity=5,
                        price=4
                    )
        operation7 = trade.Operation(
                        date='2015-09-21',
                        asset=self.asset3,
                        quantity=-5,
                        price=2
                    )
        operation8 = trade.Operation(
                        date='2015-09-21',
                        asset=self.asset3,
                        quantity=5,
                        price=4
                    )
        operation9 = trade.Operation(
                        date='2015-09-21',
                        asset=self.asset3,
                        quantity=-5,
                        price=4
                    )

        self.container = trade.OperationContainer(
            operations=[
                operation1,
                operation2,
                operation3,
                operation4,
                operation5,
                operation6,
                operation7,
                operation8,
                operation9
            ]
        )
        self.container.fetch_positions_tasks = [
            trade.get_operations_from_exercises,
            trade.identify_daytrades_and_common_operations,
            trade.prorate_commissions,
            trade.find_rates_for_positions,
        ]
        self.container.fetch_positions()

    def test_container_should_exist(self):
        self.assertTrue(self.container)

    def test_trades_len_should_be_five(self):
        self.assertEqual(len(self.container.operations), 9)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.container.operations[1].price, 3)

    def test_common_trades_len_should_be_1(self):
        self.assertEqual(len(self.container.positions['common operations'].keys()), 1)

    def test_check_common_trades0_asset(self):
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_10(self):
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].quantity,
            10
        )

    def test_common_trades0_price_should_be_3(self):
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].price,
            3
        )

    def test_daytrades_len_should_be_3(self):
        self.assertEqual(
            len(self.container.positions['daytrades'].keys()),
            3
        )

    def test_check_daytrade0_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].asset,
            self.asset1
        )

    def test_daytrade0_quantity_should_be_5(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].quantity,
            5
        )

    def test_daytrade0_buy_price_should_be_2(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity_should_be_5(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[0].quantity,
            5
        )

    def test_daytrade0_sale_price_should_be_3(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[1].price,
            3
        )

    def test_daytrade0_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[1].quantity,
            -5
        )

    def test_daytrade0_result_should_be_5(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].result,
            5
        )

    def test_check_daytrade1_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].asset,
            self.asset2
        )

    def test_daytrade1_quantity_should_be_5(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].quantity,
            5
        )

    def test_daytrade1_buy_price_should_be_10(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity_should_be_5(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price_should_be_7(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[1].quantity,
            -5
        )

    def test_daytrade1_result_should_be_5(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].result,
            -15
        )

    def test_check_daytrade2_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3].asset,
            self.asset3
        )

    def test_daytrade2_quantity_should_be_10(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3].quantity,
            10
        )

    def test_daytrade2_buy_price_should_be_10(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3].operations[0].price,
            4
        )

    def test_daytrade2_buy_quantity_should_be_10(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3].operations[0].quantity,
            10
        )

    def test_daytrade2_sale_price_should_be_3(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3].operations[1].price,
            3
        )

    def test_daytrade2_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3].operations[1].quantity,
            -10
        )


class TestTradeContainer_fetch_positions_case_02(unittest.TestCase):
    """ Daytrades, commissions and taxes."""

    def setUp(self):

        self.containers = []
        self.container_operations = []
        self.asset = trade.Asset('PETR4')

        # NOTA 2
        date='2015-02-03'
        operations = []
        operations.append(
            trade.Operation(
                date=date,
                asset=self.asset,
                quantity=10,
                price=10
            )
        )
        operations.append(
            trade.Operation(
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
        self.container = trade.OperationContainer(
            operations=operations,
            commissions=commissions
        )
        self.container.fetch_positions_tasks = [
            trade.get_operations_from_exercises,
            trade.identify_daytrades_and_common_operations,
            trade.prorate_commissions,
            trade.find_rates_for_positions,
        ]
        self.container.tax_manager = TaxManagerForTests()
        self.container.fetch_positions()

    def test_container_daytrade_buy_operation_discounts(self):
        discounts = {
            'corretagem': 1,
            'iss': 0.75,
            'outros': 0.5,
        }
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].operations[0].commissions,
            discounts
        )

    def test_container_daytrade_buy_sale_operation_discounts(self):
        discounts = {
            'corretagem': 1,
            'iss': 0.75,
            'outros': 0.5,
        }
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].operations[1].commissions,
            discounts
        )

    def test_container_daytrade_buy_operation_taxes(self):
        taxes = {
            'emoluments': 0.005,
            'liquidation': 0.02,
            'registry': 0,
        }
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].operations[0].rates,
            taxes
        )

    def test_container_daytrade_sale_operation_taxes(self):
        taxes = {
            'emoluments': 0.005,
            'liquidation': 0.02,
            'registry': 0,
        }
        self.assertEqual(self.container.positions['daytrades'][self.asset].operations[1].rates, taxes)

    def test_container_daytrade_operation_result(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][self.asset].result,8),
            -4.55000000
        )

    def test_container_daytrade_operation_quantity(self):
        self.assertEqual(self.container.positions['daytrades'][self.asset].quantity, 10)

    def test_container_daytrade_buy_operation_real_price(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][self.asset].operations[0].real_price,8),
            10.22750000
        )

    def test_container_daytrade_sale_operation_real_price(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][self.asset].operations[1].real_price,8),
            9.77250000
        )

    def test_container_daytrade_buy_operation_real_value(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][self.asset].operations[0].real_value,8),
            102.27500000
        )

    def test_container_daytrade_sale_operation_real_value(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][self.asset].operations[1].real_value,8),
            -97.72500000
        )
