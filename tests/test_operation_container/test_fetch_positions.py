"""Tests for the fetch_positions() method of OperationContainer."""

from __future__ import absolute_import
import unittest
from abc import ABCMeta

import trade
from .container_test_base import TestFetchPositions
from .fixture_positions import (
    DT_POSITION0, DT_POSITION1, DT_POSITION2, POSITION4, POSITION2,
    DT_POSITION6,
)
from trade.plugins import (
    prorate_commissions,
)
from .fixture_tasks import find_trading_fees_for_positions

from tests.fixtures.assets import (
    ASSET, ASSET2, ASSET3,
)
from tests.fixtures.commissions import (
    COMMISSIONS13, COMMISSIONS8
)
from tests.fixtures.operation_sequences import (
    OPERATION_SEQUENCE2, OPERATION_SEQUENCE8
)


class TaxManagerForTests(object):
    """A TradingFees class for the tests."""

    __metaclass__ = ABCMeta

    @classmethod
    def get_fees(cls, operation=None, operation_type=None):
        """A sample implementation of get_fees()."""
        if operation_type == 'daytrades':
            return cls.get_fees_for_daytrades(operation)
        return {}

    @classmethod
    def get_fees_for_daytrades(cls, operation):
        """Get the fees for a daytrade operation."""
        return {
            'emoluments': operation.volume * 0.005 / 100,
            'liquidation': operation.volume * 0.02 / 100,
            'registry': 0,
        }

class TestContainerFetchPositionsCase00(TestFetchPositions):
    """Test the fetch_positions() method of Accumulator."""

    commissions = COMMISSIONS13
    operations = OPERATION_SEQUENCE2
    positions = POSITION4
    daytrades = {
        ASSET.symbol: DT_POSITION6
    }


class TestContainerFetchPositionsCase01(TestFetchPositions):
    """Test the fetch_positions() method of Accumulator."""

    operations = OPERATION_SEQUENCE8
    positions = POSITION2
    daytrades = {
        ASSET.symbol: DT_POSITION0,
        ASSET2.symbol: DT_POSITION1,
        ASSET3.symbol: DT_POSITION2
    }


class TestContainerFetchPositionsCase02(unittest.TestCase):
    """Daytrades, commissions and taxes."""

    def setUp(self):
        date = '2015-02-03'
        operations = []
        operations.append(
            trade.Operation(
                date=date, subject=ASSET, quantity=10, price=10
            )
        )
        operations.append(
            trade.Operation(
                date=date, subject=ASSET, quantity=-10, price=10
            )
        )
        self.container = trade.OperationContainer(
            operations=operations,
        )
        self.container.commissions = COMMISSIONS8
        self.container.tasks = [
            trade.plugins.fetch_exercises,
            trade.plugins.fetch_daytrades,
        ]
        self.container.trading_fees = TaxManagerForTests
        self.container.fetch_positions()
        find_trading_fees_for_positions(self.container)
        prorate_commissions(self.container)

    def test_daytrade_buy_discounts(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].commissions,
            {
                'some': 1,
                'other': 0.75,
                'and other': 0.5,
                'emoluments': 0.005,
                'liquidation': 0.02,
                'registry': 0,
            }
        )

    def test_daytrade_sale_discounts(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].commissions,
            {
                'some': 1,
                'other': 0.75,
                'and other': 0.5,
                'emoluments': 0.005,
                'liquidation': 0.02,
                'registry': 0,
            }
        )

    def test_daytrade_result(self):
        self.assertEqual(
            round(
                self.container.positions['daytrades'][ASSET.symbol]\
                    .results['daytrades'], 8
            ), -4.55000000
        )

    def test_daytrade_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].quantity, 10
        )

    def test_daytrade_buy_real_price(self):
        self.assertEqual(
            round(
                self.container.positions['daytrades'][ASSET.symbol]\
                    .operations[0].real_price, 8
            ), 10.22750000
        )

    def test_daytrade_sale_real_price(self):
        self.assertEqual(
            round(
                self.container.positions['daytrades'][ASSET.symbol]\
                    .operations[1].real_price, 8
            ), 9.77250000
        )

    def test_daytrade_buy_real_value(self):
        self.assertEqual(
            round(
                self.container.positions['daytrades'][ASSET.symbol].\
                    operations[0].real_value, 8
            ), 102.27500000
        )

    def test_daytrade_sale_real_value(self):
        self.assertEqual(
            round(
                self.container.positions['daytrades'][ASSET.symbol]\
                    .operations[1].real_value, 8
            ), -97.72500000
        )
