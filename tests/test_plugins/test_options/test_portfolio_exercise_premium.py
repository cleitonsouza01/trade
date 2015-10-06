"""Test the function to fetch the exercise premium."""

from __future__ import absolute_import
import unittest

import trade


class TestExercisePremium(unittest.TestCase):

    def setUp(self):
        self.portfolio = trade.Portfolio()
        self.portfolio.tasks = [trade.plugins.get_exercise_premium]

        # Create an asset and a call
        self.asset = trade.Asset(symbol='some asset')
        self.option = trade.plugins.Option(
            symbol='GOOG151002C00540000',
            underlying_assets={self.asset: 1},
            expiration_date='2015-10-02'
        )

        # Buy the asset
        self.operation = trade.Operation(
            asset=self.asset,
            date='2015-10-01',
            quantity=10,
            price=5
        )
        self.portfolio.accumulate(self.operation)

        # Exercise the call
        self.exercise = trade.plugins.Exercise(
            asset=self.option,
            date='2015-10-04',
            quantity=10,
            price=5
        )

        # other operation with the option
        self.option_operation = trade.Operation(
            asset=self.option,
            date='2015-10-02',
            quantity=10,
            price=1
        )
        self.option_operation2 = trade.Operation(
            asset=self.option,
            date='2015-10-02',
            quantity=20,
            price=1
        )


class TestExercisePremiumCase00(TestExercisePremium):
    """Test the accumulation of one operation with underlying assets."""

    def setUp(self):
        super(TestExercisePremiumCase00, self).setUp()
        self.portfolio.accumulate(self.option_operation)
        self.portfolio.accumulate(self.exercise)

    def test_option_name(self):
        self.assertEqual(self.option.symbol, 'GOOG151002C00540000')

    def test_option_expiration_date(self):
        self.assertEqual(self.option.expiration_date, '2015-10-02')

    def test_underlying_assets(self):
        self.assertEqual(self.option.underlying_assets, {self.asset: 1})

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 2)

    def test_asset_accumulator_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset.symbol].quantity, 20)

    def test_asset_accumulator_price(self):
        """Should have the premium included on the price"""
        self.assertEqual(self.portfolio.assets[self.asset.symbol].price, 5.5)

    def test_option_accumulator_quantity(self):
        self.assertEqual(self.portfolio.assets[self.option.symbol].quantity, 0)

    def test_option_accumulator_price(self):
        self.assertEqual(self.portfolio.assets[self.option.symbol].price, 0)


class TestExercisePremiumCase01(TestExercisePremium):
    """Test the accumulation of one operation with underlying assets."""

    def setUp(self):
        super(TestExercisePremiumCase01, self).setUp()
        self.portfolio.accumulate(self.option_operation2)
        self.portfolio.accumulate(self.exercise)

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 2)

    def test_asset_accumulator_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset.symbol].quantity, 20)

    def test_asset_accumulator_price(self):
        """Should have the premium included on the price"""
        self.assertEqual(self.portfolio.assets[self.asset.symbol].price, 5.5)

    def test_option_accumulator_quantity(self):
        self.assertEqual(
            self.portfolio.assets[self.option.symbol].quantity,
            10
        )

    def test_option_accumulator_price(self):
        self.assertEqual(self.portfolio.assets[self.option.symbol].price, 1)
