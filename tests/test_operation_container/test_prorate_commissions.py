"""Tests for the prorate_commissions() method of Accumulator."""

from __future__ import absolute_import
import unittest
import copy

import trade
from trade.plugins import prorate_commissions, prorate_commissions_by_position

from tests.fixtures.operations import (
    OPERATION39, OPERATION42, OPERATION43, OPERATION44,
    OPERATION24, OPERATION26, OPERATION27,
)
from tests.fixtures.commissions import (
    COMMISSIONS9, COMMISSIONS10, COMMISSIONS11,
)
from tests.fixtures.assets import (
    ASSET, ASSET2,
)


class TestProrateCommissions(unittest.TestCase):

    def setUp(self):
        self.operation = copy.deepcopy(OPERATION39)


class TestProrateCommissionsByPositionCase01(TestProrateCommissions):
    """Test pro rata of one commission for one operation."""

    def setUp(self):
        super(TestProrateCommissionsByPositionCase01, self).setUp()
        self.container = trade.OperationContainer(
            operations=[self.operation],
        )
        self.container.fetch_positions()
        self.container.commissions = COMMISSIONS11
        prorate_commissions(self.container)

    def test_operation_discount(self):
        prorate_commissions_by_position(self.container, self.operation)
        self.assertEqual(self.operation.commissions, {'some discount': 1})


class TestProrateCommissionsByPositionCase02(TestProrateCommissions):
    """Test pro rata of 1 commission for 3 operations."""

    def setUp(self):
        super(TestProrateCommissionsByPositionCase02, self).setUp()
        self.operation2 = copy.deepcopy(OPERATION42)
        self.container = trade.OperationContainer(
            operations=[
                self.operation,
                self.operation2
            ],
        )
        self.container.commissions = COMMISSIONS11
        self.container.fetch_positions()
        prorate_commissions(self.container)

    def test_check_trade1_discount(self):
        prorate_commissions_by_position(self.container, self.operation)
        self.assertEqual(self.operation.commissions, {'some discount': 0.5})

    def test_check_trade2_discount(self):
        prorate_commissions_by_position(self.container, self.operation2)
        self.assertEqual(self.operation2.commissions, {'some discount': 0.5})


class TestProrateCommissionsByPositionCase03(TestProrateCommissions):
    """Test pro rata of 1 commission for 2 operations."""

    def setUp(self):
        super(TestProrateCommissionsByPositionCase03, self).setUp()
        self.operation2 = copy.deepcopy(OPERATION43)
        self.container = trade.OperationContainer(
            operations=[
                self.operation,
                self.operation2
            ],
        )
        self.container.commissions = COMMISSIONS11
        self.container.fetch_positions()

    def test_check_trade1_discount(self):
        #self.container.prorate_commissions_by_position(self.operation)
        prorate_commissions_by_position(self.container, self.operation)
        self.assertEqual(
            round(self.operation.commissions['some discount'], 8),
            0.33333333
        )

    def test_check_trade2_discount(self):
        prorate_commissions_by_position(self.container, self.operation2)
        self.assertEqual(
            round(self.operation2.commissions['some discount'], 8),
            0.66666667
        )


class TestProrateCommissionsByPositionCase04(TestProrateCommissions):
    """Test pro rata of 1 commission for 3 sale operations."""

    def setUp(self):
        super(TestProrateCommissionsByPositionCase04, self).setUp()
        self.operation2 = copy.deepcopy(OPERATION44)
        self.operation3 = copy.deepcopy(OPERATION42)
        self.container = trade.OperationContainer(
            operations=[
                self.operation,
                self.operation2,
                self.operation3
            ],
        )
        self.container.commissions = COMMISSIONS10
        self.container.fetch_positions()
        prorate_commissions(self.container)

    def test_check_trade1_discount(self):
        self.assertEqual(self.operation.commissions['some discount'], 1)

    def test_check_trade2_discount(self):
        self.assertEqual(self.operation2.commissions['some discount'], 2)

    def test_check_trade3_discount(self):
        self.assertEqual(self.operation3.commissions['some discount'], 1)


class TestProrateCommissionsByPositionCase05(TestProrateCommissions):
    """Test pro rata of 1 commission for daytrades."""

    def setUp(self):
        super(TestProrateCommissionsByPositionCase05, self).setUp()
        trade1 = copy.deepcopy(OPERATION24)
        trade2 = copy.deepcopy(OPERATION26)
        trade3 = copy.deepcopy(OPERATION27)
        self.container = trade.OperationContainer(
            operations=[trade1, trade2, trade3],
        )
        self.container.commissions = COMMISSIONS9
        self.container.tasks = [trade.plugins.fetch_daytrades]
        self.container.fetch_positions()
        prorate_commissions(self.container)

    def test_container_volume(self):
        self.assertEqual(self.container.volume, 70)

    def test_daytrade0_buy_discounts(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].commissions['some discount'], 2),
            0.29
        )
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].commissions['other discount'], 2),
            0.86
        )

    def test_daytrade0_sale_discounts(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].commissions['some discount'], 2),
            0.43
        )
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].commissions['other discount'], 2),
            1.29
        )

    def test_operations0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].quantity,
            5
        )

    def test_operations0_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].price,
            2
        )

    def test_operations0_volume(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].volume,
            10
        )

    def test_operations0_discounts(self):
        self.assertEqual(
            round(self.container.positions['operations'][ASSET.symbol]\
                .commissions['some discount'], 2),
            0.29
        )
        self.assertEqual(
            round(self.container.positions['operations'][ASSET.symbol]\
                .commissions['other discount'], 2),
            0.86
        )

    def test_operations1_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol].quantity,
            -5
        )

    def test_operations1_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol].price,
            7
        )

    def test_operations1_volume(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol].volume,
            35
        )

    def test_operations1_discounts(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol].commissions,
            {
                'some discount': 1,
                'other discount': 3
            }
        )
