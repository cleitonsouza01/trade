"""Test the identification of Daytrades among Operations."""

from __future__ import absolute_import
import unittest
import copy

import trade

from tests.fixtures.operations import (
    OPERATION32, OPERATION26
)
from tests.fixtures.assets import (
    ASSET, ASSET2, ASSET3,
)

from tests.fixtures.operation_sequences import (
    OPERATION_SEQUENCE0, OPERATION_SEQUENCE1, OPERATION_SEQUENCE2,
    OPERATION_SEQUENCE3, OPERATION_SEQUENCE4, OPERATION_SEQUENCE5
)

TASKS = [
    trade.plugins.fetch_exercises,
    trade.plugins.fetch_daytrades,
]


class TestIdentifyDaytrades(unittest.TestCase):
    "Base class for daytrade identification tests."
    def setUp(self):
        self.container = trade.OperationContainer()
        self.container.tasks = TASKS


class TestContainerIndentifyDaytradesCase00(TestIdentifyDaytrades):
    """Test the identification of daytrade operations."""

    def setUp(self):
        super(TestContainerIndentifyDaytradesCase00, self).setUp()
        self.container.operations = copy.deepcopy(OPERATION_SEQUENCE0)
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertTrue('operations' not in self.container.positions)

    def test_daytrades_len(self):
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 1)

    def test_daytrade_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].quantity, 10
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
        self.container.operations = copy.deepcopy(OPERATION_SEQUENCE1)
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)

    def test_operations1_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].quantity, 5
        )

    def test_operations1_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].price, 2
        )

    def test_daytrades_len(self):
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 1)

    def test_daytrade_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].quantity, 5
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
        self.container.operations = copy.deepcopy(OPERATION_SEQUENCE2)
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
            self.container.positions['operations'][ASSET2.symbol].quantity, -5
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
        self.container.operations = copy.deepcopy(OPERATION_SEQUENCE3)
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)

    def test_common_trades0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].quantity, 5
        )

    def test_common_trades0_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].price, 2
        )

    def test_daytrades_len(self):
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 2)

    def test_daytrade0_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].quantity, 5
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
        self.container.operations = copy.deepcopy(OPERATION_SEQUENCE3)
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
            self.container.positions['daytrades'][ASSET.symbol].results,
            {'daytrades': 10}
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


class TestContainerIndentifyDaytradesCase05(TestIdentifyDaytrades):
    """Test the identification of daytrade operations."""

    def setUp(self):
        super(TestContainerIndentifyDaytradesCase05, self).setUp()
        self.container.operations = copy.deepcopy(OPERATION_SEQUENCE4)
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
            self.container.positions['daytrades'][ASSET2.symbol].quantity, 5
        )

    def test_daytrade1_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].price, 10
        )

    def test_daytrade1_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].quantity, 5
        )

    def test_daytrade1_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].price, 7
        )

    def test_daytrade1_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].quantity, -5
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
        self.container.operations = copy.deepcopy(OPERATION_SEQUENCE3)
        self.container.operations.append(copy.deepcopy(OPERATION32))
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)

    def test_common_trades0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].quantity, 10
        )

    def test_common_trades0_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].price, 3
        )

    def test_daytrades_len(self):
        self.assertEqual(
            len(self.container.positions['daytrades'].keys()), 2
        )

    def test_daytrade0_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].quantity, 5
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
                .operations[0].price, 10
        )

    def test_daytrade1_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].quantity, 5
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
        self.container.operations = copy.deepcopy(OPERATION_SEQUENCE3)
        self.container.operations += copy.deepcopy(OPERATION_SEQUENCE5)
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
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 3)

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
