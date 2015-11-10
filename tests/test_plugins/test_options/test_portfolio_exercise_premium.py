"""Test the function to fetch the exercise premium."""

from __future__ import absolute_import

from tests.fixtures.operation_sequences import (
    OPERATION_SEQUENCE25, OPERATION_SEQUENCE26
)
from tests.fixtures.assets import ASSET, OPTION1
from tests.fixtures.accumulator_states import (
    STATE01, STATE06, STATE09,
)
from tests.test_portfolio.test_portfolio import TestPortfolio


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
