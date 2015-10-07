"""Tests the logging of Operation, Daytrade and Event objects."""

from __future__ import absolute_import
import unittest
import copy

import trade
import trade.plugins

from . fixture_operations import (
    OPERATION1, OPERATION18, ASSET, DAYTRADE2, EVENT0, EVENT1, EVENT2
)

DAYTRADE3 = copy.deepcopy(DAYTRADE2)
DAYTRADE3.date = '2015-01-02'

EXPECTED_LOG0 = {
    '2015-01-01': {
        'position': {
            'quantity': 100,
            'price': 10
        },
        'occurrences': [DAYTRADE2, OPERATION18, EVENT0]
    }
}

EXPECTED_LOG1 = {
    '2015-01-03': {
        'position': {
            'quantity': 100,
            'price': 10
        },
        'occurrences': [EVENT1]
    },
    '2015-01-02': {
        'position': {
            'quantity': 100,
            'price': 10
        },
        'occurrences': [OPERATION1]
    },
    '2015-01-01': {
        'position': {
            'quantity': 0,
            'price': 0
        },
        'occurrences': [DAYTRADE2]
    }
}

EXPECTED_LOG2 = {
    '2015-01-02': {
        'position': {
            'quantity': 100,
            'price': 10
        },
        'occurrences': [OPERATION1, DAYTRADE3, EVENT2]
    },
    '2015-01-01': {
        'position': {
            'quantity': 0,
            'price': 0
        },
        'occurrences': [DAYTRADE2]
    }
}


class TestLogDaytradesOperationsAndEvents(unittest.TestCase):

    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET, logging=True)


class TestLogDaytradesOperationsAndEventsCase00(
        TestLogDaytradesOperationsAndEvents):
    """Test logging events, operations and daytrades on the same date."""

    def setUp(self):
        super(TestLogDaytradesOperationsAndEventsCase00, self).setUp()
        self.accumulator.accumulate_occurrence(DAYTRADE2)
        self.accumulator.accumulate_occurrence(OPERATION18)
        self.accumulator.accumulate_occurrence(EVENT0)

    def test_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG0)


class TestLogDaytradesOperationsAndEventsCase01(
        TestLogDaytradesOperationsAndEvents):
    """Test logging all objects on the different dates."""

    def setUp(self):
        super(TestLogDaytradesOperationsAndEventsCase01, self).setUp()
        self.accumulator.accumulate_occurrence(DAYTRADE2)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(EVENT1)

    def test_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG1)


class TestLogDaytradesOperationsAndEventsCase02(
        TestLogDaytradesOperationsAndEvents):
    """Test logging objects on different dates."""

    def setUp(self):
        super(TestLogDaytradesOperationsAndEventsCase02, self).setUp()
        self.accumulator.accumulate_occurrence(DAYTRADE2)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(DAYTRADE3)
        self.accumulator.accumulate_occurrence(EVENT2)

    def test_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG2)
