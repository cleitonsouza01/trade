"""Tests logging of Event objects."""

from __future__ import absolute_import
from __future__ import division

import unittest

from trade import Accumulator

from . fixture_operations import ASSET, EVENT3, EVENT4, EVENT5


EXPECTED_LOG0 = {
    '2015-09-24': {
        'position': {
            'price': 5.0,
            'quantity': 200
        },
        'occurrences': [EVENT5]
    }
}

EXPECTED_LOG1 = {
    '2015-09-25': {
        'position': {
            'price': 5.0,
            'quantity': 200
        },
        'occurrences': [EVENT3]
    },
    '2015-09-24': {
        'position': {
            'price': 5.0,
            'quantity': 200
        },
        'occurrences': [EVENT5]
    }
}


class TestLogEvent(unittest.TestCase):

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}
        self.accumulator.accumulate_occurrence(EVENT5)


class TestLogEvent00(TestLogEvent):
    """Tests the logging of 1 Event object."""

    def test_check_quantity_after_split(self):
        self.assertEqual(self.accumulator.quantity, 200)

    def test_check_price_after_split(self):
        self.assertEqual(self.accumulator.price, 5)

    def test_check_results_after_split(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})

    def test_check_log_case_00(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG0)


class TestLogEvent01(TestLogEvent):
    """Tests the logging of 2 Event objects."""

    def setUp(self):
        super(TestLogEvent01, self).setUp()
        self.accumulator.accumulate_occurrence(EVENT3)

    def test_check_log_case_01(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG1)


class TestLogEvent02(TestLogEvent):
    """Tests the logging of multiple Event objects."""

    def setUp(self):
        super(TestLogEvent02, self).setUp()
        self.accumulator.accumulate_occurrence(EVENT4)

    def test_log_position(self):
        self.assertEqual(
            self.accumulator.log['2015-09-24']['position'],
            {
                'price': 5.0,
                'quantity': 200
            }
        )

    def test_log_occurrences(self):
        self.assertEqual(
            self.accumulator.log['2015-09-24']['occurrences'],
            [EVENT5, EVENT4]
        )
