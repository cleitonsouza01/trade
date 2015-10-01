from __future__ import absolute_import
import unittest

import trade


class TestPortfolioAssetAccumulation_Case_00(unittest.TestCase):
    """Test the accumulation of one operation."""

    def setUp(self):
        self.portfolio = trade.Portfolio()
        self.asset = trade.Asset(name='some asset')
        self.operation = trade.Operation(
                            asset=self.asset,
                            date='2015-10-01',
                            quantity=10,
                            price=1
                        )
        self.portfolio.accumulate(self.operation)

    #def test_portfolio_asset_keys(self):
    #    self.assertEqual(self.portfolio.assets.keys(), [self.asset])

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 1)

    def test_portfolio_asset_accumulator(self):
        self.assertTrue(isinstance(self.portfolio.assets[self.asset], trade.Accumulator))

    def test_portfolio_asset_accumulator_asset(self):
        self.assertEqual(self.portfolio.assets[self.asset].asset, self.asset)

    def test_accumulator_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset].quantity, 10)

    def test_accumulator_price(self):
        self.assertEqual(self.portfolio.assets[self.asset].price, 1)


class TestPortfolioAssetAccumulation_Case_01(unittest.TestCase):
    """Test the accumulation of two operations with the same asset."""

    def setUp(self):
        self.portfolio = trade.Portfolio()
        self.asset = trade.Asset(name='some asset')
        self.operation0 = trade.Operation(
                            asset=self.asset,
                            date='2015-10-01',
                            quantity=10,
                            price=1
                        )
        self.operation1 = trade.Operation(
                            asset=self.asset,
                            date='2015-10-01',
                            quantity=10,
                            price=2
                        )
        self.portfolio.accumulate(self.operation0)
        self.portfolio.accumulate(self.operation1)

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 1)

    def test_portfolio_asset_accumulator(self):
        self.assertTrue(isinstance(self.portfolio.assets[self.asset], trade.Accumulator))

    def test_portfolio_asset_accumulator_asset(self):
        self.assertEqual(self.portfolio.assets[self.asset].asset, self.asset)

    def test_accumulator_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset].quantity, 20)

    def test_accumulator_price(self):
        self.assertEqual(self.portfolio.assets[self.asset].price, 1.5)


class TestPortfolioAssetAccumulation_Case_02(unittest.TestCase):
    """Test the accumulation of two operations with different assets."""

    def setUp(self):
        self.portfolio = trade.Portfolio()
        self.asset0 = trade.Asset(name='some asset')
        self.asset1 = trade.Asset(name='other asset')
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
        self.portfolio.accumulate(self.operation0)
        self.portfolio.accumulate(self.operation1)

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 2)

    def test_accumulator0(self):
        self.assertTrue(isinstance(self.portfolio.assets[self.asset0], trade.Accumulator))

    def test_accumulator0_asset(self):
        self.assertEqual(self.portfolio.assets[self.asset0].asset, self.asset0)

    def test_accumulator0_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset0].quantity, 10)

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.assets[self.asset0].price, 1)


    def test_accumulator0(self):
        self.assertTrue(isinstance(self.portfolio.assets[self.asset1], trade.Accumulator))

    def test_accumulator0_asset(self):
        self.assertEqual(self.portfolio.assets[self.asset1].asset, self.asset1)

    def test_accumulator0_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset1].quantity, 20)

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.assets[self.asset1].price, 2)


class TestPortfolioAssetAccumulation_Case_03(unittest.TestCase):
    """Accumulation of multiple operations with different assets."""

    def setUp(self):
        self.portfolio = trade.Portfolio()
        self.asset0 = trade.Asset(name='some asset')
        self.asset1 = trade.Asset(name='other asset')
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
        self.portfolio.accumulate(self.operation0)
        self.portfolio.accumulate(self.operation1)
        self.portfolio.accumulate(self.operation2)

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 2)

    def test_accumulator0(self):
        self.assertTrue(isinstance(self.portfolio.assets[self.asset0], trade.Accumulator))

    def test_accumulator0_asset(self):
        self.assertEqual(self.portfolio.assets[self.asset0].asset, self.asset0)

    def test_accumulator0_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset0].quantity, 10)

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.assets[self.asset0].price, 1)


    def test_accumulator0(self):
        self.assertTrue(isinstance(self.portfolio.assets[self.asset1], trade.Accumulator))

    def test_accumulator0_asset(self):
        self.assertEqual(self.portfolio.assets[self.asset1].asset, self.asset1)

    def test_accumulator0_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset1].quantity, 40)

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.assets[self.asset1].price, 3)




class TestPortfolioAssetAccumulation_Case_04(unittest.TestCase):
    """Accumulation of multiple operations with different assets."""

    def setUp(self):
        self.portfolio = trade.Portfolio()
        self.asset0 = trade.Asset(name='some asset')
        self.asset1 = trade.Asset(name='other asset')
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
        self.portfolio.accumulate(self.operation0)
        self.portfolio.accumulate(self.operation1)
        self.portfolio.accumulate(self.operation2)
        self.portfolio.accumulate(self.operation3)

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 2)

    def test_accumulator0(self):
        self.assertTrue(isinstance(self.portfolio.assets[self.asset0], trade.Accumulator))

    def test_accumulator0_asset(self):
        self.assertEqual(self.portfolio.assets[self.asset0].asset, self.asset0)

    def test_accumulator0_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset0].quantity, 10)

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.assets[self.asset0].price, 1)


    def test_accumulator0(self):
        self.assertTrue(isinstance(self.portfolio.assets[self.asset1], trade.Accumulator))

    def test_accumulator0_asset(self):
        self.assertEqual(self.portfolio.assets[self.asset1].asset, self.asset1)

    def test_accumulator0_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset1].quantity, 60)

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.assets[self.asset1].price, 3)



class TestPortfolioAssetAccumulation_Case_05(unittest.TestCase):
    """Accumulation of multiple operations with different assets."""

    def setUp(self):
        self.portfolio = trade.Portfolio()
        self.asset0 = trade.Asset(name='some asset')
        self.asset1 = trade.Asset(name='other asset')
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
        self.portfolio.accumulate(self.operation0)
        self.portfolio.accumulate(self.operation1)
        self.portfolio.accumulate(self.operation2)
        self.portfolio.accumulate(self.operation3)
        self.portfolio.accumulate(self.operation4)

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.assets.keys()), 2)

    def test_accumulator0(self):
        self.assertTrue(isinstance(self.portfolio.assets[self.asset0], trade.Accumulator))

    def test_accumulator0_asset(self):
        self.assertEqual(self.portfolio.assets[self.asset0].asset, self.asset0)

    def test_accumulator0_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset0].quantity, 20)

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.assets[self.asset0].price, 1.5)


    def test_accumulator0(self):
        self.assertTrue(isinstance(self.portfolio.assets[self.asset1], trade.Accumulator))

    def test_accumulator0_asset(self):
        self.assertEqual(self.portfolio.assets[self.asset1].asset, self.asset1)

    def test_accumulator0_quantity(self):
        self.assertEqual(self.portfolio.assets[self.asset1].quantity, 60)

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.assets[self.asset1].price, 3)
