"""Tests the Portfolio accumulation of underlying assets."""

from __future__ import absolute_import

import copy
import unittest
import accumulator

from fixtures.operation_sequences import OPERATION_SEQUENCE20, OPERATION_SEQUENCE21
from fixtures.assets import ASSET, OPTION1
from fixtures.accumulator_states import (
    STATE06, STATE07, STATE08,
)


class TestPortfolio(unittest.TestCase):
    """Base class for Portfolio tests."""

    initial_state = None
    operations = []
    state = {}

    def setUp(self):
        self.portfolio = accumulator.Portfolio(state=self.initial_state)
        for operation in self.operations:
            self.portfolio.accumulate(copy.deepcopy(operation))

    def test_accumulators_states(self):
        """Test the state of each accumulator."""
        for asset, state in self.state.items():
            for key in state.keys():
                self.assertEqual(
                    self.portfolio.subjects[asset].state[key],
                    state[key]
                )

    def test_keys(self):
        """Test the each accumulator key."""
        self.assertEqual(
            len(self.portfolio.subjects.keys()),
            len(self.state.keys())
        )


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
