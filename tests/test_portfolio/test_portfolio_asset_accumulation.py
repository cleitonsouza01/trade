"""Tests the Portfolio accumulation of assets."""

from __future__ import absolute_import
import unittest

import trade


class TestPortfolioAssetAccumulation(unittest.TestCase):

    def setUp(self):
        self.portfolio = trade.Portfolio()
        self.asset0 = trade.Asset(symbol='some asset')
        self.asset1 = trade.Asset(symbol='other asset')
        self.asset2 = trade.Asset(symbol='even other asset')
        self.operation0 = trade.Operation(
            asset=self.asset0,
            date='2015-10-01',
            quantity=10,
            price=1
        )
        self.operation1 = trade.Operation(
            asset=self.asset1,
            date='2015-10-01',
            quantity=20,
            price=2
        )
        self.operation2 = trade.Operation(
            asset=self.asset1,
            date='2015-10-01',
            quantity=20,
            price=4
        )
        self.operation3 = trade.Operation(
            asset=self.asset1,
            date='2015-10-02',
            quantity=20,
            price=3
        )
        self.operation4 = trade.Operation(
            asset=self.asset0,
            date='2015-10-06',
            quantity=10,
            price=2
        )
        self.operation5 = trade.Operation(
            asset=self.asset2,
            date='2015-10-01',
            quantity=20,
            price=2
        )


class TestPortfolioAssetAccumulationCase00(TestPortfolioAssetAccumulation):
    """Test the accumulation of one operation."""

    def setUp(self):
        super(TestPortfolioAssetAccumulationCase00, self).setUp()
        self.portfolio.accumulate(self.operation0)

    def test_portfolio_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 1)

    def test_accumulator_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset0.symbol].quantity, 10)

    def test_accumulator_price(self):
        self.assertEqual(self.portfolio.assets[self.asset0.symbol].price, 1)


class TestPortfolioAssetAccumulationCase01(TestPortfolioAssetAccumulation):
    """Test the accumulation of two operations with the same asset."""

    def setUp(self):
        super(TestPortfolioAssetAccumulationCase01, self).setUp()
        self.portfolio.accumulate(self.operation0)
        self.portfolio.accumulate(self.operation4)

    def test_portfolio_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 1)

    def test_accumulator_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset0.symbol].quantity, 20)

    def test_accumulator_price(self):
        self.assertEqual(self.portfolio.assets[self.asset0.symbol].price, 1.5)


class TestPortfolioAssetAccumulationCase02(TestPortfolioAssetAccumulation):
    """Test the accumulation of two operations with different assets."""

    def setUp(self):
        super(TestPortfolioAssetAccumulationCase02, self).setUp()
        self.portfolio.accumulate(self.operation0)
        self.portfolio.accumulate(self.operation5)

    def test_portfolio_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 2)

    def test_accumulator0_asset(self):
        self.assertEqual(
            self.portfolio.assets[self.asset0.symbol].asset.symbol,
            self.asset0.symbol
        )

    def test_accumulator0_quantity(self):
        self.assertEqual(
            self.portfolio.assets[self.asset0.symbol].quantity,
            10
        )

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.assets[self.asset0.symbol].price, 1)

    def test_accumulator1_quantity(self):
        self.assertEqual(
            self.portfolio.assets[self.asset2.symbol].quantity,
            20
        )

    def test_accumulator1_price(self):
        self.assertEqual(self.portfolio.assets[self.asset2.symbol].price, 2)


class TestPortfolioAssetAccumulationCase03(TestPortfolioAssetAccumulation):
    """Accumulation of multiple operations with different assets."""

    def setUp(self):
        super(TestPortfolioAssetAccumulationCase03, self).setUp()
        self.portfolio.accumulate(self.operation0)
        self.portfolio.accumulate(self.operation1)
        self.portfolio.accumulate(self.operation2)

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 2)

    def test_accumulator0_asset(self):
        self.assertEqual(
            self.portfolio.assets[self.asset0.symbol].asset.symbol,
            self.asset0.symbol
        )

    def test_accumulator0_quantity(self):
        self.assertEqual(
            self.portfolio.assets[self.asset0.symbol].quantity,
            10
        )

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.assets[self.asset0.symbol].price, 1)


    def test_accumulator1(self):
        self.assertTrue(
            isinstance(
                self.portfolio.assets[self.asset1.symbol],
                trade.Accumulator
            )
        )

    def test_accumulator1_asset(self):
        self.assertEqual(
            self.portfolio.assets[self.asset1.symbol].asset.symbol,
            self.asset1.symbol
        )

    def test_accumulator1_quantity(self):
        self.assertEqual(
            self.portfolio.assets[self.asset1.symbol].quantity,
            40
        )

    def test_accumulator1_price(self):
        self.assertEqual(self.portfolio.assets[self.asset1.symbol].price, 3)


class TestPortfolioAssetAccumulationCase04(TestPortfolioAssetAccumulation):
    """Accumulation of multiple operations with different assets."""

    def setUp(self):
        super(TestPortfolioAssetAccumulationCase04, self).setUp()
        self.portfolio.accumulate(self.operation0)
        self.portfolio.accumulate(self.operation1)
        self.portfolio.accumulate(self.operation2)
        self.portfolio.accumulate(self.operation3)

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 2)

    def test_accumulator0_asset(self):
        self.assertEqual(
            self.portfolio.assets[self.asset0.symbol].asset.symbol,
            self.asset0.symbol
        )

    def test_accumulator0_quantity(self):
        self.assertEqual(
            self.portfolio.assets[self.asset0.symbol].quantity,
            10
        )

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.assets[self.asset0.symbol].price, 1)


    def test_accumulator1(self):
        self.assertTrue(
            isinstance(
                self.portfolio.assets[self.asset1.symbol],
                trade.Accumulator
            )
        )

    def test_accumulator1_asset(self):
        self.assertEqual(
            self.portfolio.assets[self.asset1.symbol].asset.symbol,
            self.asset1.symbol
        )

    def test_accumulator1_quantity(self):
        self.assertEqual(
            self.portfolio.assets[self.asset1.symbol].quantity,
            60
        )

    def test_accumulator1_price(self):
        self.assertEqual(self.portfolio.assets[self.asset1.symbol].price, 3)



class TestPortfolioAssetAccumulationCase05(TestPortfolioAssetAccumulation):
    """Accumulation of multiple operations with different assets."""

    def setUp(self):
        super(TestPortfolioAssetAccumulationCase05, self).setUp()
        self.portfolio.accumulate(self.operation0)
        self.portfolio.accumulate(self.operation1)
        self.portfolio.accumulate(self.operation2)
        self.portfolio.accumulate(self.operation3)
        self.portfolio.accumulate(self.operation4)

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 2)

    def test_accumulator0_quantity(self):
        self.assertEqual(
            self.portfolio.assets[self.asset0.symbol].quantity,
            20
        )

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.assets[self.asset0.symbol].price, 1.5)


    def test_accumulator1(self):
        self.assertTrue(
            isinstance(
                self.portfolio.assets[self.asset1.symbol],
                trade.Accumulator
            )
        )

    def test_accumulator1_quantity(self):
        self.assertEqual(
            self.portfolio.assets[self.asset1.symbol].quantity,
            60
        )

    def test_accumulator1_price(self):
        self.assertEqual(self.portfolio.assets[self.asset1.symbol].price, 3)
