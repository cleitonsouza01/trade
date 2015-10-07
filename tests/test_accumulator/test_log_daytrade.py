"""Tests the logging of Daytrade objects."""

from __future__ import absolute_import
import unittest

import trade
from . fixture_operations import ASSET, DAYTRADE0
from . fixture_logs import EXPECTED_LOG16


class TestLogDaytrade(unittest.TestCase):
    """Test the logging of a Daytrade object."""

    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(DAYTRADE0)

    def test_log_first_operation(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG16)

    def test_log_keys(self):
        self.assertEqual(list(self.accumulator.log), ['2015-01-01'])

    def test_returned_result(self):
        self.assertEqual(DAYTRADE0.results, {'daytrades':1000})
