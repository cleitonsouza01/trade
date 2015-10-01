from __future__ import absolute_import
import unittest

import trade


class TestPortfolioUnderlyingAssetAccumulation_Case_00(unittest.TestCase):
    """Test the accumulation of one operation with underlying assets."""

    def setUp(self):
        self.portfolio = trade.Portfolio()

        # Create an asset and a call
        self.asset = trade.Asset(name='some asset')
        self.option = trade.Option(name='some option', underlying_assets=[self.asset])

        # Buy the asset
        self.operation = trade.Operation(
                            asset=self.asset,
                            date='2015-10-01',
                            quantity=10,
                            price=5
                        )
        self.portfolio.accumulate(self.operation)

        # Buy the call
        self.option_operation = trade.Operation(
                            asset=self.option,
                            date='2015-10-02',
                            quantity=10,
                            price=1
                        )
        self.portfolio.accumulate(self.option_operation)

        # Exercise the call
        self.exercise = trade.Exercise(
                            asset=self.option,
                            date='2015-10-04',
                            quantity=10,
                            price=10
                        )
        self.portfolio.accumulate(self.exercise)

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 2)

    def test_asset_accumulator(self):
        self.assertTrue(isinstance(self.portfolio.assets[self.asset], trade.Accumulator))

    def test_asset_accumulator_asset(self):
        self.assertEqual(self.portfolio.assets[self.asset].asset, self.asset)

    def test_asset_accumulator_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset].quantity, 20)

    def test_asset_accumulator_price(self):
        self.assertEqual(self.portfolio.assets[self.asset].price, 7.5)


    def test_option_accumulator(self):
        self.assertTrue(isinstance(self.portfolio.assets[self.option], trade.Accumulator))

    def test_option_accumulator_asset(self):
        self.assertEqual(self.portfolio.assets[self.option].asset, self.option)

    def test_option_accumulator_quantity(self):
        self.assertEqual(self.portfolio.assets[self.option].quantity, 0)

    def test_option_accumulator_price(self):
        self.assertEqual(self.portfolio.assets[self.option].price, 0)
