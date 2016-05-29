"""Tests for StockSplit events."""

from __future__ import absolute_import

from fixtures.logtest import LogTest
from fixtures.events import EVENT5
from fixtures.accumulator_states import (
    EXPECTED_STATE0, INITIAL_STATE0,
)


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
