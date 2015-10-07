"""Tests the logging of Operation and Daytrade objects."""

from __future__ import absolute_import
import unittest

import trade

from tests.fixtures.operations import (
    ASSET, OPERATION1, OPERATION18, DAYTRADE0, DAYTRADE1,
)
from . fixture_logs import (
    EXPECTED_LOG22, EXPECTED_LOG23, EXPECTED_LOG24,
)


class TestLogDaytradesAndOperations(unittest.TestCase):

    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET, logging=True)


class TestLogDaytradesAndOperationsCase00(TestLogDaytradesAndOperations):
    """Tests the logging of Operation and Daytrade objects.

    Try to log a daytrade and a operation on the same date.
    """

    def test_log_occurrences(self):
        self.accumulator.accumulate_occurrence(DAYTRADE0)
        self.accumulator.accumulate_occurrence(OPERATION18)
        self.assertEqual(self.accumulator.log, EXPECTED_LOG22)


class TestLogDaytradesAndOperationsCase01(TestLogDaytradesAndOperations):
    """Tests the logging of Operation and Daytrade objects.

    Logs one daytrade and then one operation on a posterior
    date.
    """

    def test_log_occurrences(self):
        self.accumulator.accumulate_occurrence(DAYTRADE0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.assertEqual(self.accumulator.log, EXPECTED_LOG23)


class TestLogDaytradesAndOperationsCase02(TestLogDaytradesAndOperations):
    """Tests the logging of Operation and Daytrade objects.

    One daytrade first,
    then one operation and one daytrade on a posterior date.
    """

    def test_log_occurrences(self):
        self.accumulator.accumulate_occurrence(DAYTRADE0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(DAYTRADE1)
        self.assertEqual(self.accumulator.log, EXPECTED_LOG24)
