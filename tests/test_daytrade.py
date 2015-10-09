"""Tests for the Daytrade class."""

from __future__ import absolute_import
import unittest
import copy

import trade
from tests.fixtures.assets import ASSET
from tests.fixtures.operations import (
    OPERATION24, OPERATION25, OPERATION60, OPERATION39
)


class TestDaytradeCreation(unittest.TestCase):
    """Tests the creation of daytrade objects.

    Daytrade objects should create two operations, the
    purchase_operation and the sale_operation based on the
    values informed during its cretion.
    """

    def setUp(self):
        operation_a = copy.deepcopy(OPERATION24)
        operation_b = copy.deepcopy(OPERATION25)
        self.daytrade = trade.plugins.Daytrade(operation_a, operation_b)

    def test_daytrade_asset(self):
        self.assertEqual(self.daytrade.subject.symbol, ASSET.symbol)

    def test_daytrade_quantity(self):
        self.assertEqual(self.daytrade.quantity, 10)

    def test_daytrade_buy(self):
        self.assertTrue(self.daytrade.operations[0])

    def test_daytrade_buy_asset(self):
        self.assertEqual(
            self.daytrade.operations[0].subject.symbol,
            self.daytrade.subject.symbol)

    def test_daytrade_buy_quantity(self):
        self.assertEqual(self.daytrade.operations[0].quantity, 10)

    def test_daytrade_buy_price(self):
        self.assertEqual(self.daytrade.operations[0].price, 2)

    def test_daytrade_sale_should_exist(self):
        self.assertTrue(self.daytrade.operations[1])

    def test_daytrade_sale_asset(self):
        self.assertEqual(
            self.daytrade.operations[1].subject.symbol, ASSET.symbol
        )

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
        operation_a = copy.deepcopy(OPERATION60)
        operation_b = copy.deepcopy(OPERATION39)
        self.daytrade = trade.plugins.Daytrade(operation_a, operation_b)

    def test_daytrade_result(self):
        self.assertEqual(self.daytrade.results, {'daytrades': -10})
