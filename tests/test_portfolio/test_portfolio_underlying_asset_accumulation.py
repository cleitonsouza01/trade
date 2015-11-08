"""Tests the Portfolio accumulation of underlying assets."""

from __future__ import absolute_import

from tests.fixtures.operation_sequences import (
    OPERATION_SEQUENCE20, OPERATION_SEQUENCE21,
)
from tests.fixtures.assets import (
    ASSET, OPTION1,
)
from tests.fixtures.accumulator_states import (
    STATE06, STATE07, STATE08,
)
from .test_portfolio import TestPortfolio


class TestUnderlyingAssetAccumulationCase00(TestPortfolio):
    """Test the accumulation of one operation with underlying assets."""

    operations = OPERATION_SEQUENCE20
    state = {
        ASSET.symbol: STATE07,
        OPTION1.symbol: STATE06,
    }


class TestUnderlyingAssetAccumulationCase01(TestPortfolio):
    """Test the accumulation of one operation with underlying assets."""

    operations = OPERATION_SEQUENCE21
    state = {
        ASSET.symbol: STATE08,
        OPTION1.symbol: STATE06,
    }
