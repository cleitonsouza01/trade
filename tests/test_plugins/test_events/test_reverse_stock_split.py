"""Tests for ReverseStockSplit events."""

from __future__ import absolute_import

from tests.fixtures.events import EVENT9
from tests.fixtures.logs import (
    LogTest, INITIAL_STATE0
)


class TestReverseStockSplitCase00(LogTest):
    """Test the accumulation of a ReverseStockSplit event."""

    initial_state = INITIAL_STATE0
    occurrences = [EVENT9]
    expected_quantity = 50
    expected_price = 20
    expected_results = {'trades': 1200}
