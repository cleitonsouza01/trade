"""Tests the Portfolio accumulation of underlying assets."""

from __future__ import absolute_import

from tests.fixtures.operations import (
    OPTION_OPERATION1, EXERCISE_OPERATION1, OPERATION46, OPERATION47,
)
from tests.fixtures.assets import (
    ASSET, OPTION1,
)
from .test_portfolio import TestPortfolio


class TestUnderlyingAssetAccumulationCase00(TestPortfolio):
    """Test the accumulation of one operation with underlying assets."""

    operations = [
        OPERATION46,
        OPTION_OPERATION1,
        EXERCISE_OPERATION1
    ]
    state = {
        ASSET.symbol: {
            'quantity': 20,
            'price': 8
        },
        OPTION1.symbol: {
            'quantity': 0,
            'price': 0
        },
    }


class TestUnderlyingAssetAccumulationCase01(TestPortfolio):
    """Test the accumulation of one operation with underlying assets."""

    operations = [
        OPERATION46,
        OPTION_OPERATION1,
        EXERCISE_OPERATION1,
        OPERATION47
    ]
    state = {
        ASSET.symbol: {
            'quantity': 30,
            'price': 7.833333333333333
        },
        OPTION1.symbol: {
            'quantity': 0,
            'price': 0
        },
    }
