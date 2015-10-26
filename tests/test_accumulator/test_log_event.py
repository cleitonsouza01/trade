"""Tests logging of Event objects."""

from __future__ import absolute_import
from __future__ import division

from tests.fixtures.events import (
    EVENT3, EVENT5, EVENT4
)
from tests.fixtures.logs import (
    EXPECTED_LOG17, EXPECTED_LOG18,
    LogTest,
)
from tests.fixtures.accumulator_states import (
    INITIAL_STATE0, EXPECTED_STATE0,
)


class TestLogEvent(LogTest):

    initial_state = INITIAL_STATE0
    occurrences = [EVENT5]
    expected_log = EXPECTED_LOG17
    expected_state = EXPECTED_STATE0


class TestLogEvent01(TestLogEvent):
    """Tests the logging of 2 Event objects."""

    occurrences = [EVENT5, EVENT3]
    expected_log = EXPECTED_LOG18


class TestLogEvent02(TestLogEvent):
    """Tests the logging of multiple Event objects on the same date."""

    occurrences = [EVENT5, EVENT4]
    expected_log = EXPECTED_LOG17
