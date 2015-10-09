"""Tests the logging of Daytrade objects."""

from __future__ import absolute_import

from tests.fixtures.operations import DAYTRADE0
from tests.fixtures.logs import EXPECTED_LOG16, LogTest


class TestLogDaytrade(LogTest):
    """Test the logging of a Daytrade object."""

    occurrences = [DAYTRADE0]
    expected_log = EXPECTED_LOG16
    expected_quantity = 0
    expected_price = 0
    expected_results = {'daytrades': 1000}

    def test_log_keys(self):
        self.assertEqual(list(self.accumulator.log), ['2015-01-01'])
