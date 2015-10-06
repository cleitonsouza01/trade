"""Tests the Portfolio accumulation of underlying assets."""

from __future__ import absolute_import
import unittest

import trade


def get_exercise_no_premium(operation, portfolio):
    if isinstance(operation, trade.plugins.Exercise):
        operation.fetch_operations()


class TestUnderlyingAssetAccumulation(unittest.TestCase):

    def setUp(self):
        self.portfolio = trade.Portfolio()
        self.portfolio.tasks = [get_exercise_no_premium]

        # Create an asset and a call
        self.asset = trade.Asset(symbol='some asset')
        self.option = trade.plugins.Option(
            symbol='some option',
            underlying_assets=[self.asset]
        )
        # Create an operation buying the asset
        self.operation = trade.Operation(
            asset=self.asset,
            date='2015-10-01',
            quantity=10,
            price=5
        )
        # Create an operation buying the call
        self.option_operation = trade.Operation(
            asset=self.option,
            date='2015-10-02',
            quantity=10,
            price=1
        )
        # Create an operation exercising the call
        self.exercise = trade.plugins.Exercise(
            asset=self.option,
            date='2015-10-04',
            quantity=10,
            price=10
        )
        # Create other operation buying the asset
        self.operation2 = trade.Operation(
            asset=self.asset,
            date='2015-10-05',
            quantity=10,
            price=7.5
        )
        self.portfolio.accumulate(self.operation)
        self.portfolio.accumulate(self.option_operation)


class TestUnderlyingAssetAccumulationCase00(TestUnderlyingAssetAccumulation):
    """Test the accumulation of one operation with underlying assets."""

    def setUp(self):
        super(TestUnderlyingAssetAccumulationCase00, self).setUp()
        self.portfolio.accumulate(self.exercise)

    def test_portfolio_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 2)

    def test_accumulator1_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset.symbol].quantity, 20)

    def test_accumulator1_price(self):
        self.assertEqual(self.portfolio.assets[self.asset.symbol].price, 7.5)

    def test_accumulator2_quantity(self):
        self.assertEqual(self.portfolio.assets[self.option.symbol].quantity, 0)

    def test_accumulator2_price(self):
        self.assertEqual(self.portfolio.assets[self.option.symbol].price, 0)


class TestUnderlyingAssetAccumulationCase01(TestUnderlyingAssetAccumulation):
    """Test the accumulation of one operation with underlying assets."""

    def setUp(self):
        super(TestUnderlyingAssetAccumulationCase01, self).setUp()
        self.portfolio.accumulate(self.exercise)
        self.portfolio.accumulate(self.operation2)

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 2)

    def test_asset_accumulator_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset.symbol].quantity, 30)

    def test_asset_accumulator_price(self):
        self.assertEqual(self.portfolio.assets[self.asset.symbol].price, 7.5)

    def test_option_accumulator_quantity(self):
        self.assertEqual(self.portfolio.assets[self.option.symbol].quantity, 0)

    def test_option_accumulator_price(self):
        self.assertEqual(self.portfolio.assets[self.option.symbol].price, 0)
