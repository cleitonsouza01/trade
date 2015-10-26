"""Tests the logging of Operation, Daytrade and Event objects."""

from __future__ import absolute_import

from tests.fixtures.operations import (
    OPERATION1, OPERATION18, DAYTRADE2, DAYTRADE3,
)
from tests.fixtures.events import (
    EVENT0, EVENT1, EVENT2,
)
from tests.fixtures.logs import (
    EXPECTED_LOG19, EXPECTED_LOG20, EXPECTED_LOG21,
    LogTest
)
from tests.fixtures.accumulator_states import (
    EXPECTED_STATE23, EXPECTED_STATE24,
)


class TestLogDaytradesOperationsAndEventsCase00(LogTest):
    """Logging events, operations and daytrades on the same date."""

    occurrences = [DAYTRADE2, OPERATION18, EVENT0]
    expected_log = EXPECTED_LOG19
    expected_state = EXPECTED_STATE23


class TestLogDaytradesOperationsAndEventsCase01(LogTest):
    """Logging events, daytrades and operations on different dates."""

    occurrences = [DAYTRADE2, OPERATION1, EVENT1]
    expected_log = EXPECTED_LOG20
    expected_state = EXPECTED_STATE23


class TestLogDaytradesOperationsAndEventsCase02(LogTest):
    """Logging events, operations and daytrades on different dates."""

    occurrences = [DAYTRADE2, OPERATION1, DAYTRADE3, EVENT2]
    expected_log = EXPECTED_LOG21
    expected_state = EXPECTED_STATE24
