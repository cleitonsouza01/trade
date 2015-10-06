"""Tests for the prorate_commissions() method of Accumulator."""

from __future__ import absolute_import
import unittest

import trade

ASSET1 = trade.Asset(symbol='GOOGL')
ASSET2 = trade.Asset(symbol='AAPL')
ASSET3 = trade.Asset(symbol='ATVI')


class TestProrateCommissions(unittest.TestCase):

    def setUp(self):
        self.operation = trade.Operation(
            date='2015-09-21',
            asset=ASSET1,
            quantity=-10,
            price=2
        )
        self.discounts = {
            'some discount': 1,
        }

class TestProrateCommissionsByPositionCase01(TestProrateCommissions):
    """Test pro rata of one commission for one operation."""

    def setUp(self):
        super(TestProrateCommissionsByPositionCase01, self).setUp()
        self.container = trade.OperationContainer(
            operations=[self.operation],
            commissions=self.discounts
        )
        self.container.fetch_positions()

    def test_operation_discount(self):
        self.container.prorate_commissions_by_position(self.operation)
        self.assertEqual(self.operation.commissions, {'some discount': 1})


class TestProrateCommissionsByPositionCase02(TestProrateCommissions):
    """Test pro rata of 1 commission for 3 operations."""

    def setUp(self):
        super(TestProrateCommissionsByPositionCase02, self).setUp()
        self.operation2 = trade.Operation(
            date='2015-09-21',
            asset=ASSET2,
            quantity=-10,
            price=2
        )
        self.container = trade.OperationContainer(
            operations=[
                self.operation,
                self.operation2
            ],
            commissions=self.discounts
        )
        self.container.fetch_positions()

    def test_check_trade1_discount(self):
        self.container.prorate_commissions_by_position(self.operation)
        self.assertEqual(self.operation.commissions, {'some discount': 0.5})

    def test_check_trade2_discount(self):
        self.container.prorate_commissions_by_position(self.operation2)
        self.assertEqual(self.operation2.commissions, {'some discount': 0.5})


class TestProrateCommissionsByPositionCase03(TestProrateCommissions):
    """Test pro rata of 1 commission for 2 operations."""

    def setUp(self):
        super(TestProrateCommissionsByPositionCase03, self).setUp()
        self.operation2 = trade.Operation(
            date='2015-09-21',
            asset=ASSET2,
            quantity=-20,
            price=2
        )
        self.container = trade.OperationContainer(
            operations=[
                self.operation,
                self.operation2
            ],
            commissions=self.discounts
        )
        self.container.fetch_positions()

    def test_check_trade1_discount(self):
        self.container.prorate_commissions_by_position(self.operation)
        self.assertEqual(
            round(self.operation.commissions['some discount'], 8),
            0.33333333
        )

    def test_check_trade2_discount(self):
        self.container.prorate_commissions_by_position(self.operation2)
        self.assertEqual(
            round(self.operation2.commissions['some discount'], 8),
            0.66666667
        )


class TestProrateCommissionsByPositionCase04(TestProrateCommissions):
    """Test pro rata of 1 commission for 3 sale operations."""

    def setUp(self):
        super(TestProrateCommissionsByPositionCase04, self).setUp()
        discounts = {
            'some discount': 4,
        }
        self.operation2 = trade.Operation(
            date='2015-09-21',
            asset=ASSET3,
            quantity=-20,
            price=2
        )
        self.operation3 = trade.Operation(
            date='2015-09-21',
            asset=ASSET2,
            quantity=-10,
            price=2
        )
        self.container = trade.OperationContainer(
            operations=[
                self.operation,
                self.operation2,
                self.operation3
            ],
            commissions=discounts
        )
        self.container.fetch_positions()

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
        discounts = {
            'some discount': 2,
            'other discount': 6
        }
        trade1 = trade.Operation(
            date='2015-09-21',
            asset=ASSET1,
            quantity=10,
            price=2
        )
        trade2 = trade.Operation(
            date='2015-09-21',
            asset=ASSET1,
            quantity=-5,
            price=3
        )
        trade3 = trade.Operation(
            date='2015-09-21',
            asset=ASSET2,
            quantity=-5,
            price=7
        )
        self.container = trade.OperationContainer(
            operations=[trade1, trade2, trade3],
            commissions=discounts
        )
        self.container.tasks = [trade.plugins.fetch_daytrades]
        self.container.fetch_positions()

    def test_container_volume(self):
        self.assertEqual(self.container.volume, 70)

    def test_daytrade0_buy_discounts(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET1.symbol]\
                .operations[0].commissions['some discount'], 2),
            0.29
        )
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET1.symbol]\
                .operations[0].commissions['other discount'], 2),
            0.86
        )

    def test_daytrade0_sale_discounts(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET1.symbol]\
                .operations[1].commissions['some discount'], 2),
            0.43
        )
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET1.symbol]\
                .operations[1].commissions['other discount'], 2),
            1.29
        )

    def test_operations0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET1.symbol]\
                .quantity,
            5
        )

    def test_operations0_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET1.symbol].price,
            2
        )

    def test_operations0_volume(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET1.symbol].volume,
            10
        )

    def test_operations0_discounts(self):
        self.assertEqual(
            round(self.container.positions['operations'][ASSET1.symbol]\
                .commissions['some discount'], 2),
            0.29
        )
        self.assertEqual(
            round(self.container.positions['operations'][ASSET1.symbol]\
                .commissions['other discount'], 2),
            0.86
        )

    def test_operations1_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol]\
                .quantity,
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
        expected_discounts = {
            'some discount': 1,
            'other discount': 3
        }
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol]\
                .commissions,
            expected_discounts
        )
