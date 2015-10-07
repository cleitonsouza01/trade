"""Tests the Portfolio accumulation of underlying assets."""

from __future__ import absolute_import
import unittest
import copy

import trade

from tests.fixtures.fixture_operations import (
    ASSET, OPTION1,

    OPTION_OPERATION1, EXERCISE_OPERATION1, OPERATION46, OPERATION47,
)


def get_exercise_no_premium(operation, portfolio):
    if isinstance(operation, trade.plugins.Exercise):
        operation.fetch_operations()


class TestUnderlyingAssetAccumulation(unittest.TestCase):

    def setUp(self):
        self.portfolio = trade.Portfolio()
        self.portfolio.tasks = [get_exercise_no_premium]
        self.portfolio.accumulate(copy.deepcopy(OPERATION46))
        self.portfolio.accumulate(copy.deepcopy(OPTION_OPERATION1))


class TestUnderlyingAssetAccumulationCase00(TestUnderlyingAssetAccumulation):
    """Test the accumulation of one operation with underlying assets."""

    def setUp(self):
        super(TestUnderlyingAssetAccumulationCase00, self).setUp()
        self.portfolio.accumulate(copy.deepcopy(EXERCISE_OPERATION1))

    def test_portfolio_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 2)

    def test_accumulator1_quantity(self):
        self.assertEqual(self.portfolio.assets[ASSET.symbol].quantity, 20)

    def test_accumulator1_price(self):
        self.assertEqual(self.portfolio.assets[ASSET.symbol].price, 7.5)

    def test_accumulator2_quantity(self):
        self.assertEqual(self.portfolio.assets[OPTION1.symbol].quantity, 0)

    def test_accumulator2_price(self):
        self.assertEqual(self.portfolio.assets[OPTION1.symbol].price, 0)


class TestUnderlyingAssetAccumulationCase01(TestUnderlyingAssetAccumulation):
    """Test the accumulation of one operation with underlying assets."""

    def setUp(self):
        super(TestUnderlyingAssetAccumulationCase01, self).setUp()
        self.portfolio.accumulate(copy.deepcopy(EXERCISE_OPERATION1))
        self.portfolio.accumulate(copy.deepcopy(OPERATION47))

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 2)

    def test_asset_accumulator_quantity(self):
        self.assertEqual(self.portfolio.assets[ASSET.symbol].quantity, 30)

    def test_asset_accumulator_price(self):
        self.assertEqual(self.portfolio.assets[ASSET.symbol].price, 7.5)

    def test_option_accumulator_quantity(self):
        self.assertEqual(self.portfolio.assets[OPTION1.symbol].quantity, 0)

    def test_option_accumulator_price(self):
        self.assertEqual(self.portfolio.assets[OPTION1.symbol].price, 0)
