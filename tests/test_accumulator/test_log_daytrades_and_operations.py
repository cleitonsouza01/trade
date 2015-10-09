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


class TestLogDaytradesAndOperationsCase00(unittest.TestCase):
    """Tests the logging of Operation and Daytrade objects."""

    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET, logging=True)
        self.accumulator.accumulate(DAYTRADE0)

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
