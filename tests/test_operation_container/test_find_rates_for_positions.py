"""Tests for the find_fees_for_positions() method of Accumulator."""

from __future__ import absolute_import
import unittest
from abc import ABCMeta, abstractmethod

import trade


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
        self.asset1 = trade.Asset(symbol='some asset')
        self.asset2 = trade.Asset(symbol='some other asset')
        operation1 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=10,
            price=2
        )
        operation2 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=-5,
            price=3
        )
        operation3 = trade.Operation(
            date='2015-09-21',
            asset=self.asset2,
            quantity=-5,
            price=7
        )
        self.container = trade.OperationContainer(
            operations=[
                operation1,
                operation2,
                operation3
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
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[0].fees,
            taxes
        )

    def test_daytrade_sale_taxes(self):
        taxes = {
            'rate': 0.005,
        }
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[0].fees,
            taxes
        )

    def test_operations0_taxes(self):
        taxes = {'rate':1}
        self.assertEqual(
            self.container.positions['operations'][self.asset1.symbol].fees,
            taxes
        )

    def test_operations1_taxes(self):
        taxes = {'rate':1}
        self.assertEqual(
            self.container.positions['operations'][self.asset2.symbol].fees,
            taxes
        )
