"""Test the identification of Daytrades among Operations."""

from __future__ import absolute_import
import unittest
import copy

import trade

from tests.fixtures.fixture_operations import (
    ASSET, ASSET2, ASSET3,

    OPERATION24, OPERATION25, OPERATION26, OPERATION27, OPERATION28,
    OPERATION29, OPERATION30, OPERATION26, OPERATION32, OPERATION32,
    OPERATION34, OPERATION35, OPERATION34, OPERATION37,
)

TASKS = [
    trade.plugins.fetch_exercises,
    trade.plugins.fetch_daytrades,
]

class TestIdentifyDaytrades(unittest.TestCase):

    def setUp(self):
        self.container = trade.OperationContainer()
        self.container.tasks = TASKS
        self.operation_set1 = [
            copy.deepcopy(OPERATION24),
            copy.deepcopy(OPERATION25)
        ]
        self.operation_set2 = [
            copy.deepcopy(OPERATION24),
            copy.deepcopy(OPERATION26)
        ]
        self.operation_set3 = [
            copy.deepcopy(OPERATION24),
            copy.deepcopy(OPERATION26),
            copy.deepcopy(OPERATION27)
        ]
        self.operation_set4 = [
            copy.deepcopy(OPERATION24),
            copy.deepcopy(OPERATION26),
            copy.deepcopy(OPERATION27),
            copy.deepcopy(OPERATION28)
        ]

class TestContainerIndentifyDaytradesCase00(TestIdentifyDaytrades):
    """Test the identification of daytrade operations."""

    def setUp(self):
        super(TestContainerIndentifyDaytradesCase00, self).setUp()
        self.container.operations = self.operation_set1
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertTrue('operations' not in self.container.positions)

    def test_daytrades_len(self):
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 1)

    def test_daytrade_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].quantity,
            10
        )

    def test_daytrade_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].quantity,
            10
        )

    def test_daytrade_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].quantity,
            -10
        )

    def test_daytrade_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .results,
            {'daytrades': 10}
        )


class TestContainerIndentifyDaytradesCase01(TestIdentifyDaytrades):
    """Test the identification of daytrade operations."""

    def setUp(self):
        super(TestContainerIndentifyDaytradesCase01, self).setUp()
        self.container.operations = self.operation_set2
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)

    def test_operations1_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].quantity,
            5
        )

    def test_operations1_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].price,
            2
        )

    def test_daytrades_len(self):
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 1)

    def test_daytrade_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].quantity,
            5
        )

    def test_daytrade_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].results,
            {'daytrades': 5}
        )


class TestContainerIndentifyDaytradesCase02(TestIdentifyDaytrades):
    """Test the identification of daytrade operations."""

    def setUp(self):
        super(TestContainerIndentifyDaytradesCase02, self).setUp()
        self.container.operations = self.operation_set3
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 2)

    def test_operations0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol]\
                .quantity,
            5
        )

    def test_operations0_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol]\
                .price,
            2
        )

    def test_operations1_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol]\
                .quantity,
            -5
        )

    def test_common_trades1_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol].price,
            7
        )

    def test_daytrades_len(self):
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 1)

    def test_daytrade_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].quantity,
            5
        )

    def test_daytrade_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].results,
            {'daytrades': 5}
        )


class TestContainerIndentifyDaytradesCase03(TestIdentifyDaytrades):
    """Test the identification of daytrade operations."""

    def setUp(self):
        super(TestContainerIndentifyDaytradesCase03, self).setUp()
        self.container.operations = self.operation_set4
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)

    def test_common_trades0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol]\
                .quantity,
            5
        )

    def test_common_trades0_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].price,
            2
        )

    def test_daytrades_len(self):
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 2)

    def test_daytrade0_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .quantity,
            5
        )

    def test_daytrade0_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade0_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade0_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade0_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].results,
            {'daytrades': 5}
        )

    def test_daytrade1_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol].quantity,
            5
        )

    def test_daytrade1_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade1_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol].results,
            {'daytrades': -15}
        )


class TestContainerIndentifyDaytradesCase04(TestIdentifyDaytrades):
    """Test the identification of daytrade operations."""

    def setUp(self):
        super(TestContainerIndentifyDaytradesCase04, self).setUp()
        self.container.operations = self.operation_set4
        self.container.operations.append(copy.deepcopy(OPERATION26))
        self.container.fetch_positions()

    def test_for_no_common_trades(self):
        self.assertTrue('operations' not in self.container.positions)

    def test_daytrades_len(self):
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 2)

    def test_daytrade0_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].quantity,
            10
        )

    def test_daytrade0_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].quantity,
            10
        )

    def test_daytrade0_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade0_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].quantity,
            -10
        )

    def test_daytrade0_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .results,
            {'daytrades': 10}
        )

    def test_daytrade1_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .quantity,
            5
        )

    def test_daytrade1_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade1_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .results,
            {'daytrades': -15}
        )


class TestContainerIndentifyDaytradesCase05(TestIdentifyDaytrades):
    """Test the identification of daytrade operations."""

    def setUp(self):
        super(TestContainerIndentifyDaytradesCase05, self).setUp()

        self.container.operations = [
            copy.deepcopy(OPERATION24),
            copy.deepcopy(OPERATION29),
            copy.deepcopy(OPERATION27),
            copy.deepcopy(OPERATION28),
            copy.deepcopy(OPERATION30)
        ]
        self.container.fetch_positions()

    def test_for_no_common_trades(self):
        self.assertTrue('operations' not in self.container.positions)

    def test_daytrades_len(self):
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 2)

    def test_daytrade0_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].quantity,
            10
        )

    def test_daytrade0_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].quantity,
            10
        )

    def test_daytrade0_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].price,
            15
        )

    def test_daytrade0_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].quantity,
            -10
        )

    def test_daytrade0_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].results,
            {'daytrades': 130}
        )

    def test_daytrade1_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol].quantity,
            5
        )

    def test_daytrade1_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade1_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol].results,
            {'daytrades': -15}
        )


class TestContainerIndentifyDaytradesCase06(TestIdentifyDaytrades):
    """Test the identification of daytrade operations."""

    def setUp(self):
        super(TestContainerIndentifyDaytradesCase06, self).setUp()
        self.container.operations = self.operation_set4
        self.container.operations.append(copy.deepcopy(OPERATION32))
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)

    def test_common_trades0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol]\
                .quantity,
            10
        )

    def test_common_trades0_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].price,
            3
        )

    def test_daytrades_len(self):
        self.assertEqual(
            len(self.container.positions['daytrades'].keys()),
            2
        )

    def test_daytrade0_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].quantity,
            5
        )

    def test_daytrade0_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade0_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade0_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade0_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].results,
            {'daytrades': 5}
        )

    def test_daytrade1_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol].quantity,
            5
        )

    def test_daytrade1_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade1_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol].results,
            {'daytrades': -15}
        )


class TestContainerIndentifyDaytradesCase07(TestIdentifyDaytrades):
    """Test the identification of daytrade operations."""

    def setUp(self):
        super(TestContainerIndentifyDaytradesCase07, self).setUp()
        self.container.operations = self.operation_set4
        self.container.operations += [
            copy.deepcopy(OPERATION32),
            copy.deepcopy(OPERATION34),
            copy.deepcopy(OPERATION35),
            copy.deepcopy(OPERATION34),
            copy.deepcopy(OPERATION37)
        ]
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)

    def test_operations0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].quantity,
            10
        )

    def test_operations0_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].price,
            3
        )

    def test_daytrades_len(self):
        self.assertEqual(
            len(self.container.positions['daytrades'].keys()),
            3
        )

    def test_daytrade0_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].quantity,
            5
        )

    def test_daytrade0_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade0_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade0_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade0_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].results,
            {'daytrades': 5}
        )

    def test_daytrade1_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol].quantity,
            5
        )

    def test_daytrade1_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade1_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol].results,
            {'daytrades': -15}
        )

    def test_daytrade2_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET3.symbol].quantity,
            10
        )

    def test_daytrade2_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET3.symbol]\
                .operations[0].price,
            4
        )

    def test_daytrade2_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET3.symbol]\
                .operations[0].quantity,
            10
        )

    def test_daytrade2_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET3.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade2_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET3.symbol]\
                .operations[1].quantity,
            -10
        )
