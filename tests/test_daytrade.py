"""Tests for the Daytrade class."""

from __future__ import absolute_import
import unittest

import trade


class TestDaytradeCreation(unittest.TestCase):
    """Tests the creation of daytrade objects.

    Daytrade objects should create two operations, the
    purchase_operation and the sale_operation based on the
    values informed during its cretion.
    """

    def setUp(self):
        self.asset = trade.Asset(name='some stock')
        asset = trade.Asset()
        operation_a = trade.Operation(
            asset=asset,
            quantity=10,
            price=2,
            date='2015-09-20'
        )
        operation_b = trade.Operation(
            asset=asset,
            quantity=-10,
            price=3,
            date='2015-09-20'
        )
        self.daytrade = trade.plugins.Daytrade(operation_a, operation_b)

    def test_daytrade_asset(self):
        self.assertEqual(self.daytrade.asset.symbol, self.asset.symbol)

    def test_daytrade_quantity(self):
        self.assertEqual(self.daytrade.quantity, 10)

    def test_daytrade_buy(self):
        self.assertTrue(self.daytrade.operations[0])

    def test_daytrade_buy_asset(self):
        self.assertEqual(
            self.daytrade.operations[0].asset.symbol,
            self.daytrade.asset.symbol)

    def test_daytrade_buy_quantity(self):
        self.assertEqual(self.daytrade.operations[0].quantity, 10)

    def test_daytrade_buy_price(self):
        self.assertEqual(self.daytrade.operations[0].price, 2)

    def test_daytrade_sale_should_exist(self):
        self.assertTrue(self.daytrade.operations[1])

    def test_daytrade_sale_asset(self):
        self.assertEqual(
            self.daytrade.operations[1].asset.symbol,
            self.asset.symbol)

    def test_daytrade_sale_quantity(self):
        self.assertEqual(self.daytrade.operations[1].quantity, -10)

    def test_daytrade_sale_price(self):
        self.assertEqual(self.daytrade.operations[1].price, 3)

    def test_daytrade_result(self):
        self.assertEqual(self.daytrade.results, {'daytrades': 10})


class TestDaytradeResultCase01(unittest.TestCase):
    """Tests the results of a Daytrade operation.

    Daytrade results are based on the prices of the sale
    and purchase operations.
    """

    def setUp(self):
        asset = trade.Asset()
        operation_a = trade.Operation(
            asset=asset,
            quantity=10,
            price=3,
            date='2015-09-20'
        )
        operation_b = trade.Operation(
            asset=asset,
            quantity=-10,
            price=2,
            date='2015-09-20'
        )
        self.daytrade = trade.plugins.Daytrade(operation_a, operation_b)

    def test_daytrade_result(self):
        self.assertEqual(self.daytrade.results, {'daytrades': -10})
