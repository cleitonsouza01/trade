"""Tests for StockSplit events."""

from __future__ import absolute_import

from tests.fixtures.logs import (
    EVENT5, INITIAL_STATE0, LogTest,
)


class TestStockSplitCase00(LogTest):
    """Test a StockSplit effect on the Accumulator."""

    initial_state = INITIAL_STATE0
    occurrences = [EVENT5]
    expected_quantity = 200
    expected_price = 5
    expected_results = {'trades': 1200}
    expected_log = {
        '2015-09-24': {
            'data': {
                'price': 5.0,
                'quantity': 200,
                'results': {'trades': 1200}
            },
            'occurrences': [EVENT5]
        }
    }
