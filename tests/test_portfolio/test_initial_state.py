"""Tests the creation of Portfolio objects with a initial state."""

from __future__ import absolute_import

from .test_portfolio import TestPortfolio
from tests.fixtures.assets import ASSET, ASSET2
from tests.fixtures.accumulator_states import EXPECTED_STATE0, EXPECTED_STATE2


class TestPortfolioInitialStateCase00(TestPortfolio):
    """Test the creation of a Portfolio object with a initial state."""

    initial_state = {
        ASSET: EXPECTED_STATE0
    }
    state = {
        ASSET.symbol: EXPECTED_STATE0
    }


class TestPortfolioInitialStateCase01(TestPortfolio):
    """Test the creation of a Portfolio object with a initial state."""

    initial_state = {
        ASSET: EXPECTED_STATE0,
        ASSET2: EXPECTED_STATE2
    }
    state = {
        ASSET.symbol: EXPECTED_STATE0,
        ASSET2.symbol: EXPECTED_STATE2
    }
