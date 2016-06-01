"""Test the function to fetch the exercise premium."""

from __future__ import absolute_import

from fixtures.operation_sequences import (
    OPERATION_SEQUENCE25, OPERATION_SEQUENCE26
)
from fixtures.assets import OPTION1, ASSET
from fixtures.accumulator_states import (
    STATE01, STATE06, STATE09,
)
from test_options.test_portfolio_underlying_asset_accumulation import (
    TestPortfolio
)


class TestExercisePremiumCase00(TestPortfolio):
    """Test the accumulation of one operation with underlying assets."""

    operations = OPERATION_SEQUENCE25
    state = {
        ASSET.symbol: STATE09,
        OPTION1.symbol: STATE06
    }


class TestExercisePremiumCase01(TestPortfolio):
    """Test the accumulation of one operation with underlying assets."""

    operations = OPERATION_SEQUENCE26
    state = {
        ASSET.symbol: STATE09,
        OPTION1.symbol: STATE01
    }
