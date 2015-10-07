"""Tests for the find_fees_for_positions() method of Accumulator."""

from __future__ import absolute_import
import unittest
from abc import ABCMeta, abstractmethod
import copy

import trade

from tests.fixtures.fixture_operations import (
    ASSET, ASSET2,

    OPERATION24, OPERATION26, OPERATION27
)


class TaxManagerForTests(trade.TradingFees):
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

    def test_container_exists(self):
        self.assertTrue(self.container)

    def test_container_volume(self):
        self.assertEqual(self.container.volume, 70)

    def test_daytrade_buy_taxes(self):
        taxes = {
            'rate': 0.005,
        }
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].fees,
            taxes
        )

    def test_daytrade_sale_taxes(self):
        taxes = {
            'rate': 0.005,
        }
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].fees,
            taxes
        )

    def test_operations0_taxes(self):
        taxes = {'rate':1}
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].fees,
            taxes
        )

    def test_operations1_taxes(self):
        taxes = {'rate':1}
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol].fees,
            taxes
        )
