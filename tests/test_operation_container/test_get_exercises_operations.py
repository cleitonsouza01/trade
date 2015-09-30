from __future__ import absolute_import
import unittest

import trade


class Test_get_exercises_operations_Case_00(unittest.TestCase):

    def setUp(self):
        self.asset = trade.Asset(symbol='GOOGL')
        self.option = trade.Option(
                        name='GOOG151002C00540000',
                        expiration_date='2015-10-02',
                        underlying_assets=[self.asset]
                    )
        self.exercise = trade.Exercise(
            			date='2015-09-18',
            			asset=self.option,
            			quantity=100,
            			price=10
                    )
        container.container_tasks = trade.OperationContainer(
                                        exercises=[self.exercise]
                                    )
        container.container_tasks.fetch_positions_tasks = [
            trade.container_tasks.get_operations_from_exercises,
            trade.container_tasks.identify_daytrades_and_common_operations,
            trade.container_tasks.prorate_commissions,
            trade.container_tasks.find_rates_for_positions,
        ]

    def test_operation_container_should_exist(self):
        self.assertTrue(self.container)

    def test_container_exercise_operations_len(self):
        self.container.fetch_positions()
        self.assertEqual(
            len(self.container.positions['exercises'].values()),
            2
        )

    def test_option_consuming_operation_quantity(self):
        self.assertEqual(
            self.container.positions['exercises'][self.option].quantity,
            -100
        )

    def test_option_consuming_operation_price(self):
        self.assertEqual(
            self.container.positions['exercises'][self.option].price,
            0
        )

    def test_asset_purchase_operation_quantity(self):
        self.assertEqual(
            self.container.positions['exercises'][self.asset].quantity,
            100
        )

    # FIXME premium!
    def test_asset_purchase_operation_price(self):
        self.assertEqual(
            self.container.positions['exercises'][self.asset].price,
            10
        )


class Test_get_exercises_operations_Case_00(unittest.TestCase):

    def setUp(self):
        self.asset = trade.Asset(symbol='GOOGL')
        self.option = trade.Option(
                            name='GOOG151002C00540000',
                            expiration_date='2015-10-02',
                            underlying_assets=[self.asset]
                        )
        self.exercise0 = trade.Exercise(
                			date='2015-09-18',
                			asset=self.option,
                			quantity=100,
                			price=1
                        )
        self.exercise1 = trade.Exercise(
                			date='2015-09-18',
                			asset=self.option,
                			quantity=100,
                			price=3
                        )
        self.container = trade.OperationContainer(
                                exercises=[self.exercise0, self.exercise1]
                            )
        self.container.fetch_positions_tasks = [
            trade.get_operations_from_exercises,
            trade.identify_daytrades_and_common_operations,
            trade.prorate_commissions,
            trade.find_rates_for_positions,
        ]

    def test_operation_container_should_exist(self):
        self.assertTrue(self.container)

    def test_container_exercise_operations_len(self):
        self.container.fetch_positions()
        self.assertEqual(
            len(self.container.positions['exercises'].values()),
            2
        )

    def test_option_consuming_operation_quantity(self):
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['exercises'][self.option].quantity,
            -200
        )

    def test_option_consuming_operation_price(self):
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['exercises'][self.option].price,
            0
        )

    def test_asset_purchase_operation_quantity(self):
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['exercises'][self.asset].quantity,
            200
        )

    # FIXME premium!
    def test_asset_purchase_operation_price(self):
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['exercises'][self.asset].price,
            2
        )
