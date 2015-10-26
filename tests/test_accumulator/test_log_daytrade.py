"""Tests the logging of Daytrade objects."""

from __future__ import absolute_import

from tests.fixtures.operations import DAYTRADE0
from tests.fixtures.logs import (
    EXPECTED_LOG16, LogTest,
)
from tests.fixtures.accumulator_states import (
    EXPECTED_STATE25
)


class TestLogDaytrade(LogTest):
    """Test the logging of a Daytrade object."""

    occurrences = [DAYTRADE0]
    expected_log = EXPECTED_LOG16
    expected_state = EXPECTED_STATE25

    def test_log_keys(self):
        self.assertEqual(list(self.accumulator.log), ['2015-01-01'])
