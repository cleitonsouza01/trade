"""Tests logging of Event objects."""

from __future__ import absolute_import
from __future__ import division

import unittest

from trade import Accumulator

from tests.fixtures.assets import ASSET
from tests.fixtures.events import (
    EVENT3, EVENT5, EVENT4
)
from . fixture_logs import EXPECTED_LOG17, EXPECTED_LOG18


class TestLogEvent(unittest.TestCase):

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.data['quantity'] = 100
        self.accumulator.data['price'] = 10
        self.accumulator.data['results'] = {'trades': 1200}
        self.accumulator.accumulate(EVENT5)


class TestLogEvent00(TestLogEvent):
    """Tests the logging of 1 Event object."""

    def test_check_quantity_after_split(self):
        self.assertEqual(self.accumulator.data['quantity'], 200)

    def test_check_price_after_split(self):
        self.assertEqual(self.accumulator.data['price'], 5)

    def test_check_results_after_split(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 1200})

    def test_check_log_case_00(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG17)


class TestLogEvent01(TestLogEvent):
    """Tests the logging of 2 Event objects."""

    def setUp(self):
        super(TestLogEvent01, self).setUp()
        self.accumulator.accumulate(EVENT3)

    def test_check_log_case_01(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG18)


class TestLogEvent02(TestLogEvent):
    """Tests the logging of multiple Event objects."""

    def setUp(self):
        super(TestLogEvent02, self).setUp()
        self.accumulator.accumulate(EVENT4)

    def test_log_position(self):
        self.assertEqual(
            self.accumulator.log['2015-09-24']['data'],
            {
                'price': 5.0,
                'quantity': 200,
                'results': {'trades': 1200}
            }
        )

    def test_log_occurrences(self):
        self.assertEqual(
            self.accumulator.log['2015-09-24']['occurrences'],
            [EVENT5, EVENT4]
        )
