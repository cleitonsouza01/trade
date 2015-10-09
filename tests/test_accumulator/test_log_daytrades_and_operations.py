"""Tests the logging of Operation and Daytrade objects."""

from __future__ import absolute_import

from tests.fixtures.operations import (
    OPERATION1, OPERATION18, DAYTRADE0, DAYTRADE1,
)
from . fixture_logs import (
    EXPECTED_LOG22, EXPECTED_LOG23, EXPECTED_LOG24, LogTest
)


class TestLogDaytradesAndOperationsCase00(LogTest):
    """Tests the logging of Operation and Daytrade objects."""

    occurrences = [DAYTRADE0]

    def test_log_case_00(self):
        self.accumulator.accumulate(OPERATION18)
        self.assertEqual(self.accumulator.log, EXPECTED_LOG22)

    def test_log_case_01(self):
        self.accumulator.accumulate(OPERATION1)
        self.accumulator.accumulate(DAYTRADE1)
        self.assertEqual(self.accumulator.log, EXPECTED_LOG24)

    def test_log_case_02(self):
        self.accumulator.accumulate(OPERATION1)
        self.assertEqual(self.accumulator.log, EXPECTED_LOG23)
