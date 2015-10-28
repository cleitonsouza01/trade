"""Tests for the prorate_commissions() method of Accumulator."""

from __future__ import absolute_import
import unittest
import copy

import trade
from trade.plugins import prorate_commissions, prorate_commissions_by_position
from .container_test_base import TestFetchPositions
from .fixture_positions import (
    POSITION1,
)
from tests.fixtures.operations import (
    OPERATION39, OPERATION42, OPERATION43, OPERATION44,
)
from tests.fixtures.commissions import (
    COMMISSIONS9, COMMISSIONS10, COMMISSIONS11,
)
from tests.fixtures.assets import (
    ASSET, ASSET2,
)
from tests.fixtures.operation_sequences import (
    OPERATION_SEQUENCE2
)


class TestProrateCommissions(unittest.TestCase):
    "Base class to test prorate of commissions."

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


class TestProrateCommissionsByPositionCase05(TestFetchPositions):
    """Test pro rata of 1 commission for daytrades."""

    commissions = COMMISSIONS9
    operations = OPERATION_SEQUENCE2
    positions = POSITION1
    daytrades = {
        ASSET.symbol: {
            'quantity': 5,
            'buy quantity': 5,
            'buy price': 2,
            'sale quantity': -5,
            'sale price': 3,
            'result': {'daytrades': 2.1428571428571423},
            'buy commissions': {
                'some discount': 0.2857142857142857,
                'other discount': 0.8571428571428571
            },
            'sale commissions': {
                'some discount': 0.42857142857142855,
                'other discount': 1.2857142857142856
            }
        }
    }

    def test_container_volume(self):
        self.assertEqual(self.container.volume, 70)

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

    def test_operations1_discounts(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol].commissions,
            {
                'some discount': 1,
                'other discount': 3
            }
        )
