"""Test the function to fetch the exercise premium."""

from __future__ import absolute_import

from tests.fixtures.operations import  (
    OPERATION46,
    EXERCISE_OPERATION4,
    OPTION_OPERATION1, OPTION_OPERATION2
)
from tests.fixtures.assets import ASSET, OPTION1
from tests.fixtures.accumulator_states import (
    STATE01, STATE06, STATE09,
)
from tests.test_portfolio.test_portfolio import TestPortfolio


class TestExercisePremiumCase00(TestPortfolio):
    """Test the accumulation of one operation with underlying assets."""

    operations = [
        OPERATION46,
        OPTION_OPERATION1,
        EXERCISE_OPERATION4
    ]
    state = {
        ASSET.symbol: STATE09,
        OPTION1.symbol: STATE06
    }


class TestExercisePremiumCase01(TestPortfolio):
    """Test the accumulation of one operation with underlying assets."""

    operations = [
        OPERATION46,
        OPTION_OPERATION2,
        EXERCISE_OPERATION4
    ]
    state = {
        ASSET.symbol: STATE09,
        OPTION1.symbol: STATE01
    }
