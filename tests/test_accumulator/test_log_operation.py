"""Tests the logging of Operation objects."""

from __future__ import absolute_import
import unittest

import trade


from . fixture_operations import ASSET, OPERATION18


class TestLogOperation(unittest.TestCase):
    """Tests the logging of Operation objects."""

    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION18)

    def test_log_first_operation(self):
        expected_log = {
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [OPERATION18]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_log_keys(self):
        self.assertEqual(list(self.accumulator.log), ['2015-01-01'])

    def test_returned_result(self):
        self.assertEqual(OPERATION18.results, {})
