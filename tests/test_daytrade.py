"""Tests for the Daytrade class."""

from __future__ import absolute_import
import unittest
import copy

from trade.occurrences import Daytrade
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
        self.daytrade1 = Daytrade(
            copy.deepcopy(OPERATION24), copy.deepcopy(OPERATION25)
        )
        self.daytrade2 = Daytrade(
            copy.deepcopy(OPERATION60), copy.deepcopy(OPERATION39)
        )

    def test_daytrade1_asset(self):
        """Check the daytraded asset."""
        self.assertEqual(self.daytrade1.subject.symbol, ASSET.symbol)

    def test_daytrade1_quantity(self):
        """Check the daytraded quantity."""
        self.assertEqual(self.daytrade1.quantity, 10)

    def test_daytrade1_buy(self):
        """Check the daytrade purchase operation."""
        self.assertTrue(self.daytrade1.operations[0])

    def test_daytrade1_buy_asset(self):
        """Check the asset of the purchase operation."""
        self.assertEqual(
            self.daytrade1.operations[0].subject.symbol,
            self.daytrade1.subject.symbol)

    def test_daytrade1_buy_quantity(self):
        """Check the quantity of the purchase operation."""
        self.assertEqual(self.daytrade1.operations[0].quantity, 10)

    def test_daytrade1_buy_price(self):
        """Check the quantity of the purchase operation."""
        self.assertEqual(self.daytrade1.operations[0].price, 2)

    def test_daytrade1_sale_exists(self):
        """Check the daytrade sale operation."""
        self.assertTrue(self.daytrade1.operations[1])

    def test_daytrade1_sale_asset(self):
        """Check the asset of the sale operation."""
        self.assertEqual(
            self.daytrade1.operations[1].subject.symbol, ASSET.symbol
        )

    def test_daytrade1_sale_quantity(self):
        """Check the quantity of the sale operation."""
        self.assertEqual(self.daytrade1.operations[1].quantity, -10)

    def test_daytrade1_sale_price(self):
        """Check the price of the sale operation."""
        self.assertEqual(self.daytrade1.operations[1].price, 3)

    def test_daytrade1_result(self):
        """Check the results of the daytrade."""
        self.assertEqual(self.daytrade1.results, {'daytrades': 10})

    def test_daytrade2_result(self):
        """Check the results of the daytrade."""
        self.assertEqual(self.daytrade2.results, {'daytrades': -10})
