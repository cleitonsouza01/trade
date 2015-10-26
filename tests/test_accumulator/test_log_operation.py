"""Tests the logging of Operation objects."""

from __future__ import absolute_import

from tests.fixtures.operations import OPERATION18
from tests.fixtures.logs import (
    EXPECTED_LOG15,
    LogTest
)
from tests.fixtures.accumulator_states import (
    EXPECTED_STATE9,
)


class TestLogOperation(LogTest):
    """Tests the logging of Operation objects."""

    occurrences = [OPERATION18]
    expected_log = EXPECTED_LOG15
    expected_state = EXPECTED_STATE9
