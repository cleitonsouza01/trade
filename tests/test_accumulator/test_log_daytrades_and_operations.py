"""Tests the logging of Operation and Daytrade objects."""

from __future__ import absolute_import

from tests.fixtures.operations import (
    OPERATION1, OPERATION18, DAYTRADE0, DAYTRADE1,
)
from tests.fixtures.logs import (
    EXPECTED_LOG22, EXPECTED_LOG23, EXPECTED_LOG24,
    LogTest
)


class TestLogDaytradesAndOperationsCase00(LogTest):
    """Tests the logging of Operation and Daytrade objects.

    This test creates a position.
    """

    occurrences = [DAYTRADE0, OPERATION18]
    expected_log = EXPECTED_LOG22
    expected_quantity = 100
    expected_price = 10
    expected_results = {'daytrades': 1000}


class TestLogDaytradesAndOperationsCase01(LogTest):
    """Tests the logging of Operation and Daytrade objects."""

    occurrences = [DAYTRADE0, OPERATION1, DAYTRADE1]
    expected_log = EXPECTED_LOG24
    expected_quantity = 100
    expected_price = 10
    expected_results = {'daytrades': 2000}


class TestLogDaytradesAndOperationsCase02(LogTest):
    """Tests the logging of Operation and Daytrade objects."""

    occurrences = [DAYTRADE0, OPERATION1]
    expected_log = EXPECTED_LOG23
    expected_quantity = 100
    expected_price = 10
    expected_results = {'daytrades': 1000}
