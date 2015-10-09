"""Tests the Portfolio accumulation of assets."""

from __future__ import absolute_import
import unittest
import copy

import trade

from tests.fixtures.operations import (
    ASSET, ASSET2, ASSET3, OPERATION48, OPERATION49, OPERATION50, OPERATION51,
    OPERATION52, OPERATION53,
)
from tests.fixtures.assets import (
    ASSET, ASSET2, ASSET3
)


class TestPortfolioAssetAccumulation(unittest.TestCase):

    def setUp(self):
        self.portfolio = trade.Portfolio()
        self.operation0 = copy.deepcopy(OPERATION48)
        self.operation1 = copy.deepcopy(OPERATION49)
        self.operation2 = copy.deepcopy(OPERATION50)
        self.operation3 = copy.deepcopy(OPERATION51)
        self.operation4 = copy.deepcopy(OPERATION52)
        self.operation5 = copy.deepcopy(OPERATION53)


class TestPortfolioAssetAccumulationCase00(TestPortfolioAssetAccumulation):
    """Test the accumulation of one operation."""

    def setUp(self):
        super(TestPortfolioAssetAccumulationCase00, self).setUp()
        self.portfolio.accumulate(self.operation0)

    def test_portfolio_keys(self):
        self.assertEqual(len(self.portfolio.subjects.keys()), 1)

    def test_accumulator_quantity(self):
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['quantity'], 10)

    def test_accumulator_price(self):
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['price'], 1)


class TestPortfolioAssetAccumulationCase01(TestPortfolioAssetAccumulation):
    """Test the accumulation of two operations with the same asset."""

    def setUp(self):
        super(TestPortfolioAssetAccumulationCase01, self).setUp()
        self.portfolio.accumulate(self.operation0)
        self.portfolio.accumulate(self.operation4)

    def test_portfolio_keys(self):
        self.assertEqual(len(self.portfolio.subjects.keys()), 1)

    def test_accumulator_quantity(self):
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['quantity'], 20)

    def test_accumulator_price(self):
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['price'], 1.5)


class TestPortfolioAssetAccumulationCase02(TestPortfolioAssetAccumulation):
    """Test the accumulation of two operations with different assets."""

    def setUp(self):
        super(TestPortfolioAssetAccumulationCase02, self).setUp()
        self.portfolio.accumulate(self.operation0)
        self.portfolio.accumulate(self.operation5)

    def test_portfolio_keys(self):
        self.assertEqual(len(self.portfolio.subjects.keys()), 2)

    def test_accumulator0_quantity(self):
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['quantity'], 10)

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['price'], 1)

    def test_accumulator1_quantity(self):
        self.assertEqual(self.portfolio.subjects[ASSET3.symbol].data['quantity'], 20)

    def test_accumulator1_price(self):
        self.assertEqual(self.portfolio.subjects[ASSET3.symbol].data['price'], 2)


class TestPortfolioAssetAccumulationCase03(TestPortfolioAssetAccumulation):
    """Accumulation of multiple operations with different assets."""

    def setUp(self):
        super(TestPortfolioAssetAccumulationCase03, self).setUp()
        self.portfolio.accumulate(self.operation0)
        self.portfolio.accumulate(self.operation1)
        self.portfolio.accumulate(self.operation2)

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.subjects.keys()), 2)

    def test_accumulator0_quantity(self):
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['quantity'], 10)

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['price'], 1)

    def test_accumulator1_quantity(self):
        self.assertEqual(self.portfolio.subjects[ASSET2.symbol].data['quantity'], 40)

    def test_accumulator1_price(self):
        self.assertEqual(self.portfolio.subjects[ASSET2.symbol].data['price'], 3)


class TestPortfolioAssetAccumulationCase04(TestPortfolioAssetAccumulation):
    """Accumulation of multiple operations with different assets."""

    def setUp(self):
        super(TestPortfolioAssetAccumulationCase04, self).setUp()
        self.portfolio.accumulate(self.operation0)
        self.portfolio.accumulate(self.operation1)
        self.portfolio.accumulate(self.operation2)
        self.portfolio.accumulate(self.operation3)

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.subjects.keys()), 2)

    def test_accumulator0_asset(self):
        self.assertEqual(
            self.portfolio.subjects[ASSET.symbol].subject.symbol,
            ASSET.symbol
        )

    def test_accumulator0_quantity(self):
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['quantity'], 10)

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['price'], 1)

    def test_accumulator1_quantity(self):
        self.assertEqual(self.portfolio.subjects[ASSET2.symbol].data['quantity'], 60)

    def test_accumulator1_price(self):
        self.assertEqual(self.portfolio.subjects[ASSET2.symbol].data['price'], 3)


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
        self.assertEqual(len(self.portfolio.subjects.keys()), 2)

    def test_accumulator0_quantity(self):
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['quantity'], 20)

    def test_accumulator0_price(self):
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['price'], 1.5)

    def test_accumulator1_quantity(self):
        self.assertEqual(self.portfolio.subjects[ASSET2.symbol].data['quantity'], 60)

    def test_accumulator1_price(self):
        self.assertEqual(self.portfolio.subjects[ASSET2.symbol].data['price'], 3)
