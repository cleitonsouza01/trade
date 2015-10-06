"""Tests for the prorate_commissions() method of Accumulator."""

from __future__ import absolute_import
import unittest

import trade

ASSET1 = trade.Asset(symbol='GOOGL')
ASSET2 = trade.Asset(symbol='AAPL')
OPERATION = trade.Operation(
    date='2015-09-21',
    asset=ASSET1,
    quantity=-10,
    price=2
)

class TestProrateCommissionsByPositionCase01(unittest.TestCase):
    """Test pro rata of one commission for one operation."""

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        self.container = trade.OperationContainer(
            operations=[OPERATION],
            commissions=discounts
        )

    def test_operation_discount(self):
        self.container.prorate_commissions_by_position(OPERATION)
        self.assertEqual(OPERATION.commissions, {'some discount': 1})


class TestProrateCommissionsByPositionCase02(unittest.TestCase):
    """Test pro rata of 1 commission for 3 operations."""

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        self.operation2 = trade.Operation(
            date='2015-09-21',
            asset=ASSET1,
            quantity=-10,
            price=2
        )
        self.container = trade.OperationContainer(
            operations=[
                OPERATION,
                self.operation2
            ],
            commissions=discounts
        )

    def test_check_trade1_discount(self):
        self.container.prorate_commissions_by_position(OPERATION)
        self.assertEqual(OPERATION.commissions, {'some discount': 0.5})

    def test_check_trade2_discount(self):
        self.container.prorate_commissions_by_position(self.operation2)
        self.assertEqual(self.operation2.commissions, {'some discount': 0.5})


class TestProrateCommissionsByPositionCase03(unittest.TestCase):
    """Test pro rata of 1 commission for 2 operations."""

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        self.operation2 = trade.Operation(
            date='2015-09-21',
            asset=ASSET1,
            quantity=-20,
            price=2
        )
        self.container = trade.OperationContainer(
            operations=[
                OPERATION,
                self.operation2
            ],
            commissions=discounts
        )

    def test_check_trade1_discount(self):
        self.container.prorate_commissions_by_position(OPERATION)
        self.assertEqual(
            round(OPERATION.commissions['some discount'], 8),
            0.33333333
        )

    def test_check_trade2_discount(self):
        self.container.prorate_commissions_by_position(self.operation2)
        self.assertEqual(
            round(self.operation2.commissions['some discount'], 8),
            0.66666667
        )


class TestProrateCommissionsByPositionCase04(unittest.TestCase):
    """Test pro rata of 1 commission for 3 sale operations."""

    def setUp(self):
        discounts = {
            'some discount': 4,
        }
        self.operation2 = trade.Operation(
            date='2015-09-21',
            asset=ASSET1,
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
                OPERATION,
                self.operation2,
                self.operation3
            ],
            commissions=discounts
        )

    def test_check_trade1_discount(self):
        self.container.prorate_commissions_by_position(OPERATION)
        self.assertEqual(OPERATION.commissions['some discount'], 1)

    def test_check_trade2_discount(self):
        self.container.prorate_commissions_by_position(self.operation2)
        self.assertEqual(self.operation2.commissions['some discount'], 2)

    def test_check_trade3_discount(self):
        self.container.prorate_commissions_by_position(self.operation3)
        self.assertEqual(self.operation3.commissions['some discount'], 1)


class TestProrateCommissionsByPositionCase05(unittest.TestCase):
    """Test pro rata of 1 commission for daytrades."""

    def setUp(self):
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
        trade.plugins.fetch_daytrades(self.container)
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

    def test_operations0_asset(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET1.symbol].asset,
            ASSET1
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

    def test_operations1_asset(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol].asset,
            ASSET2
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
