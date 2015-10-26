"""Tests for StockSplit events."""

from __future__ import absolute_import

from tests.fixtures.logs import INITIAL_STATE0, LogTest, EXPECTED_STATE0
from tests.fixtures.events import EVENT5


class TestStockSplitCase00(LogTest):
    """Test a StockSplit effect on the Accumulator."""

    initial_state = INITIAL_STATE0
    occurrences = [EVENT5]
    expected_log = {
        '2015-09-24': {
            'price': 5.0,
            'quantity': 200,
            'results': {'trades': 1200}
        }
    }
    expected_state = EXPECTED_STATE0
