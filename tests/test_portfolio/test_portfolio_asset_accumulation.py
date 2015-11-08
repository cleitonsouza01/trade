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
from tests.fixtures.accumulator_states import (
    STATE01, STATE02, STATE03, STATE04, STATE05
)
from .test_portfolio import TestPortfolio


class TestPortfolioAssetAccumulationCase00(TestPortfolio):
    """Test the accumulation of one operation."""

    operations = [OPERATION48]
    state = {
        ASSET.symbol: STATE01
    }


class TestPortfolioAssetAccumulationCase01(TestPortfolio):
    """Test the accumulation of two operations with the same asset."""

    operations = [OPERATION48, OPERATION52]
    state = {
        ASSET.symbol: STATE02
    }


class TestPortfolioAssetAccumulationCase02(TestPortfolio):
    """Test the accumulation of two operations with different assets."""

    operations = [OPERATION48, OPERATION53]
    state = {
        ASSET.symbol: STATE01,
        ASSET3.symbol: STATE03,
    }


class TestPortfolioAssetAccumulationCase03(TestPortfolio):
    """Accumulation of multiple operations with different assets."""

    operations = [
        OPERATION48,
        OPERATION49,
        OPERATION50,
    ]
    state = {
        ASSET.symbol: STATE01,
        ASSET2.symbol: STATE04,
    }


class TestPortfolioAssetAccumulationCase04(TestPortfolio):
    """Accumulation of multiple operations with different assets."""

    operations = OPERATION_SEQUENCE22
    state = {
        ASSET.symbol: STATE01,
        ASSET2.symbol: STATE05,
    }


class TestPortfolioAssetAccumulationCase05(TestPortfolio):
    """Accumulation of multiple operations with different assets."""

    operations = OPERATION_SEQUENCE23
    state = {
        ASSET.symbol: STATE02,
        ASSET2.symbol: STATE05,
    }
