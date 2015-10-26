"""Tests the result calc for sale operations."""

from __future__ import absolute_import

from tests.fixtures.operations import (
    OPERATION9, OPERATION10, OPERATION11, OPERATION12, OPERATION13,
    OPERATION14, OPERATION15, OPERATION16, OPERATION17,
)
from tests.fixtures.logs import (
    EXPECTED_LOG0, EXPECTED_LOG1, EXPECTED_LOG2, EXPECTED_LOG3,
    EXPECTED_LOG4, EXPECTED_LOG5, EXPECTED_LOG6,
    EXPECTED_STATE1, EXPECTED_STATE9, EXPECTED_STATE7, EXPECTED_STATE10,
    EXPECTED_STATE11, EXPECTED_STATE12, EXPECTED_STATE13,
    LogTest
)


class TestAccumulatorResultsSaleCase00(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = [
        OPERATION9, OPERATION10
    ]
    expected_log = EXPECTED_LOG0
    expected_state = EXPECTED_STATE1


class TestAccumulatorResultsSaleCase01(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = [
        OPERATION9, OPERATION10, OPERATION11
    ]
    expected_log = EXPECTED_LOG1
    expected_state = EXPECTED_STATE9


class TestAccumulatorResultsSaleCase02(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = [
        OPERATION9, OPERATION10, OPERATION11, OPERATION12
    ]
    expected_log = EXPECTED_LOG2
    expected_state = EXPECTED_STATE7


class TestAccumulatorResultsSaleCase04(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = [
        OPERATION9, OPERATION10, OPERATION11, OPERATION12, OPERATION13
    ]
    expected_log = EXPECTED_LOG3
    expected_state = EXPECTED_STATE10


class TestAccumulatorResultsSaleCase05(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = [
        OPERATION9, OPERATION10, OPERATION11, OPERATION12, OPERATION13,
        OPERATION14
    ]
    expected_log = EXPECTED_LOG4
    expected_state = EXPECTED_STATE11


class TestAccumulatorResultsSaleCase06(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = [
        OPERATION9, OPERATION10, OPERATION11, OPERATION12, OPERATION13,
        OPERATION15
    ]
    expected_log = EXPECTED_LOG5
    expected_state = EXPECTED_STATE12


class TestAccumulatorResultsSaleCase07(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = [
        OPERATION16, OPERATION17
    ]
    expected_log = EXPECTED_LOG6
    expected_state = EXPECTED_STATE13
