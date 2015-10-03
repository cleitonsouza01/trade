from __future__ import absolute_import
import unittest

import trade


class TestTradeContainerCreation_Case_00(unittest.TestCase):

    def setUp(self):
        self.container = trade.OperationContainer()

    def test_container_should_exist(self):
        self.assertTrue(self.container)


class TestTradeContainerCreation_Case_01(unittest.TestCase):

    def setUp(self):
        commissions = {
            'brokerage': 2.3,
            'other': 1
        }
        self.container = trade.OperationContainer(
            commissions=commissions
        )
        self.container.fetch_positions_tasks = [
            trade.plugins.fetch_exercises,
            trade.plugins.fetch_daytrades,
        ]

    def test_container_should_exist(self):
        self.assertTrue(self.container)

    def test_container_commissions(self):
        commissions = {
            'brokerage': 2.3,
            'other': 1
        }
        self.assertEqual(self.container.commissions, commissions)


class TestTradeContainer_add_to_common_operations(unittest.TestCase):

    def setUp(self):
        self.asset = trade.Asset(symbol='some asset')
        operation = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset,
                    quantity=10,
                    price=2
                )
        self.container = trade.OperationContainer(operations=[operation])
        self.container.fetch_positions_tasks = [
            trade.plugins.fetch_exercises,
            trade.plugins.fetch_daytrades,
        ]
        self.container.fetch_positions()
        operation2 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset,
                    quantity=10,
                    price=4
                )
        self.container.add_to_position_operations(operation2)

    def test_common_trades_len_should_be_1(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)

    def test_there_should_be_no_daytrades(self):
        self.assertEqual(len(self.container.positions), 1)

    def test_common_trades0_quantity_should_be_20(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset.symbol].quantity,
            20
        )

    def test_common_trades0_price_should_be_3(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset.symbol].price,
            3
        )
