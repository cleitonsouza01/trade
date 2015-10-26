"""Tests the result calc for purchase operations."""

from __future__ import absolute_import

from tests.fixtures.operations import (
    OPERATION0, OPERATION1, OPERATION2, OPERATION3, OPERATION4, OPERATION5,
    OPERATION6, OPERATION7, OPERATION8,
)
from tests.fixtures.logs import (
    EXPECTED_LOG7, EXPECTED_LOG8, EXPECTED_LOG9, EXPECTED_LOG10,
    EXPECTED_LOG11, EXPECTED_LOG12, EXPECTED_LOG13, EXPECTED_LOG14,
    EXPECTED_STATE1, EXPECTED_STATE2, EXPECTED_STATE3, EXPECTED_STATE4,
    EXPECTED_STATE5, EXPECTED_STATE6, EXPECTED_STATE7, EXPECTED_STATE8,
    LogTest
)


class TestAccumulatorResultsPurchaseCase00(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [OPERATION0, OPERATION1]
    expected_log = EXPECTED_LOG7
    expected_state = EXPECTED_STATE1


class TestAccumulatorResultsPurchaseCase01(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [OPERATION0, OPERATION1, OPERATION2]
    expected_log = EXPECTED_LOG8
    expected_state = EXPECTED_STATE2


class TestAccumulatorResultsPurchaseCase02(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [OPERATION0, OPERATION1, OPERATION2, OPERATION3]
    expected_log = EXPECTED_LOG11
    expected_state = EXPECTED_STATE3


class TestAccumulatorResultsPurchaseCase03(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [
        OPERATION0, OPERATION1, OPERATION2, OPERATION3, OPERATION4
    ]
    expected_log = EXPECTED_LOG9
    expected_state = EXPECTED_STATE4


class TestAccumulatorResultsPurchaseCase04(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [
        OPERATION0, OPERATION1, OPERATION2, OPERATION3, OPERATION4,
        OPERATION5
    ]
    expected_log = EXPECTED_LOG10
    expected_state = EXPECTED_STATE5


class TestAccumulatorResultsPurchaseCase05(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [
        OPERATION0, OPERATION1, OPERATION2, OPERATION3, OPERATION4,
        OPERATION6
    ]
    expected_log = EXPECTED_LOG12
    expected_state = EXPECTED_STATE6


class TestAccumulatorResultsPurchaseCase06(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [OPERATION7, OPERATION1]
    expected_log = EXPECTED_LOG14
    expected_state = EXPECTED_STATE7


class TestAccumulatorResultsPurchaseCase07(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [OPERATION8, OPERATION1]
    expected_log = EXPECTED_LOG13
    expected_state = EXPECTED_STATE8
