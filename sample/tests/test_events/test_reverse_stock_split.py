"""Tests for ReverseStockSplit events."""

from __future__ import absolute_import

from fixtures.events import EVENT9
from fixtures.logtest import LogTest
from fixtures.accumulator_states import (
    INITIAL_STATE0, EXPECTED_STATE20
)


class TestReverseStockSplitCase00(LogTest):
    """Test the accumulation of a ReverseStockSplit event."""

    initial_state = INITIAL_STATE0
    occurrences = [EVENT9]
    expected_state = EXPECTED_STATE20
