"""Tests the result calc for sale operations."""

from __future__ import absolute_import

from tests.fixtures.logtest import LogTest
from tests.fixtures.operations import (
    OPERATION16, OPERATION17,
)
from tests.fixtures.operation_sequences import (
    OPERATION_SEQUENCE14, OPERATION_SEQUENCE15, OPERATION_SEQUENCE16,
    OPERATION_SEQUENCE17, OPERATION_SEQUENCE18, OPERATION_SEQUENCE19
)
from tests.fixtures.logs import (
    EXPECTED_LOG0, EXPECTED_LOG1, EXPECTED_LOG2, EXPECTED_LOG3,
    EXPECTED_LOG4, EXPECTED_LOG5, EXPECTED_LOG6,
)
from tests.fixtures.accumulator_states import (
    EXPECTED_STATE1, EXPECTED_STATE9, EXPECTED_STATE7, EXPECTED_STATE10,
    EXPECTED_STATE11, EXPECTED_STATE12, EXPECTED_STATE13,
)


class TestAccumulatorResultsSaleCase00(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = OPERATION_SEQUENCE14
    expected_log = EXPECTED_LOG0
    expected_state = EXPECTED_STATE1


class TestAccumulatorResultsSaleCase01(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = OPERATION_SEQUENCE15
    expected_log = EXPECTED_LOG1
    expected_state = EXPECTED_STATE9


class TestAccumulatorResultsSaleCase02(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = OPERATION_SEQUENCE16
    expected_log = EXPECTED_LOG2
    expected_state = EXPECTED_STATE7


class TestAccumulatorResultsSaleCase04(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = OPERATION_SEQUENCE17
    expected_log = EXPECTED_LOG3
    expected_state = EXPECTED_STATE10


class TestAccumulatorResultsSaleCase05(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = OPERATION_SEQUENCE18
    expected_log = EXPECTED_LOG4
    expected_state = EXPECTED_STATE11


class TestAccumulatorResultsSaleCase06(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = OPERATION_SEQUENCE19
    expected_log = EXPECTED_LOG5
    expected_state = EXPECTED_STATE12


class TestAccumulatorResultsSaleCase07(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = [OPERATION16, OPERATION17]
    expected_log = EXPECTED_LOG6
    expected_state = EXPECTED_STATE13
