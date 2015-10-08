"""Tests for the find_fees_for_positions() method of Accumulator."""

from __future__ import absolute_import
import unittest
from abc import ABCMeta, abstractmethod
import copy

import trade
from trade.plugins import TradingFees, find_trading_fees_for_positions

from tests.fixtures.operations import (
    OPERATION24, OPERATION26, OPERATION27
)
from tests.fixtures.assets import (
    ASSET, ASSET2,
)


class TaxManagerForTests(TradingFees):
    """A TradingFees object for the tests."""

    __metaclass__ = ABCMeta

    @classmethod
    @abstractmethod
    def get_fees(cls, operation=None, operation_type=None):
        if operation_type == 'daytrades':
            return {'rate': 0.005}
        else:
            return {'rate': 1}


class TestFindFeesForPositionsCase00(unittest.TestCase):
    """Test the application of fees to operations in the container."""

    def setUp(self):
        self.container = trade.OperationContainer(
            operations=[
                copy.deepcopy(OPERATION24),
                copy.deepcopy(OPERATION26),
                copy.deepcopy(OPERATION27),
            ]
        )
        self.container.trading_fees = TaxManagerForTests
        self.container.tasks = [
            trade.plugins.fetch_daytrades,
        ]
        self.container.fetch_positions()
        find_trading_fees_for_positions(self.container)

    def test_container_exists(self):
        self.assertTrue(self.container)

    def test_container_volume(self):
        self.assertEqual(self.container.volume, 70)

    def test_daytrade_buy_taxes(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].commissions,
            {'rate': 0.005}
        )

    def test_daytrade_sale_taxes(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].commissions,
            {'rate': 0.005,}
        )

    def test_operations0_taxes(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].commissions,
            {'rate':1}
        )

    def test_operations1_taxes(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol].commissions,
            {'rate':1}
        )
