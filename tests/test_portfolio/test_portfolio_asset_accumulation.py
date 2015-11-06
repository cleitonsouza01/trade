"""Tests the Portfolio accumulation of assets."""

from __future__ import absolute_import

from tests.fixtures.operations import (
    ASSET, ASSET2, ASSET3, OPERATION48, OPERATION49, OPERATION50,
    OPERATION52, OPERATION53,
)
from tests.fixtures.operation_sequences import (
    OPERATION_SEQUENCE22, OPERATION_SEQUENCE23,
)
from tests.fixtures.assets import (
    ASSET, ASSET2, ASSET3
)
from .test_portfolio import TestPortfolio


class TestPortfolioAssetAccumulationCase00(TestPortfolio):
    """Test the accumulation of one operation."""

    operations = [OPERATION48]
    state = {
        ASSET.symbol: {
            'quantity': 10,
            'price': 1
        }
    }


class TestPortfolioAssetAccumulationCase01(TestPortfolio):
    """Test the accumulation of two operations with the same asset."""

    operations = [OPERATION48, OPERATION52]
    state = {
        ASSET.symbol: {
            'quantity': 20,
            'price': 1.5
        }
    }


class TestPortfolioAssetAccumulationCase02(TestPortfolio):
    """Test the accumulation of two operations with different assets."""

    operations = [OPERATION48, OPERATION53]
    state = {
        ASSET.symbol: {
            'quantity': 10,
            'price': 1
        },
        ASSET3.symbol: {
            'quantity': 20,
            'price': 2
        },
    }


class TestPortfolioAssetAccumulationCase03(TestPortfolio):
    """Accumulation of multiple operations with different assets."""

    operations = [
        OPERATION48,
        OPERATION49,
        OPERATION50,
    ]

    state = {
        ASSET.symbol: {
            'quantity': 10,
            'price': 1
        },
        ASSET2.symbol: {
            'quantity': 40,
            'price': 3
        },
    }


class TestPortfolioAssetAccumulationCase04(TestPortfolio):
    """Accumulation of multiple operations with different assets."""

    operations = OPERATION_SEQUENCE22
    state = {
        ASSET.symbol: {
            'quantity': 10,
            'price': 1
        },
        ASSET2.symbol: {
            'quantity': 60,
            'price': 3
        },
    }


class TestPortfolioAssetAccumulationCase05(TestPortfolio):
    """Accumulation of multiple operations with different assets."""

    operations = OPERATION_SEQUENCE23
    state = {
        ASSET.symbol: {
            'quantity': 20,
            'price': 1.5
        },
        ASSET2.symbol: {
            'quantity': 60,
            'price': 3
        },
    }
