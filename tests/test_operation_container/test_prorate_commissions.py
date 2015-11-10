"""Tests for the prorate_commissions() method of Accumulator."""

from __future__ import absolute_import

from .fixture_positions import (
    CONTAINER_POSITION0, CONTAINER_POSITION1, CONTAINER_POSITION2,
    CONTAINER_POSITION3, CONTAINER_POSITION4, CONTAINER_DAYTRADE_POSITION0
)
from .container_test_base import TestFetchPositions
from tests.fixtures.operations import OPERATION39
from tests.fixtures.commissions import (
    COMMISSIONS9, COMMISSIONS10, COMMISSIONS11,
)
from tests.fixtures.operation_sequences import (
    OPERATION_SEQUENCE2, OPERATION_SEQUENCE27, OPERATION_SEQUENCE28,
    OPERATION_SEQUENCE29
)


class TestProrateCommissionsByPositionCase01(TestFetchPositions):
    """Test pro rata of one commission for one operation."""

    commissions = COMMISSIONS11
    operations = [OPERATION39]
    positions = CONTAINER_POSITION0


class TestProrateCommissionsByPositionCase02(TestFetchPositions):
    """Test pro rata of 1 commission for 3 operations."""

    commissions = COMMISSIONS11
    operations = OPERATION_SEQUENCE27
    positions = CONTAINER_POSITION1


class TestProrateCommissionsByPositionCase03(TestFetchPositions):
    """Test pro rata of 1 commission for 2 operations."""

    commissions = COMMISSIONS11
    operations = OPERATION_SEQUENCE28
    positions = CONTAINER_POSITION2


class TestProrateCommissionsByPositionCase04(TestFetchPositions):
    """Test pro rata of 1 commission for 3 sale operations."""

    commissions = COMMISSIONS10
    operations = OPERATION_SEQUENCE29
    positions = CONTAINER_POSITION3


class TestProrateCommissionsByPositionCase05(TestFetchPositions):
    """Test pro rata of 1 commission for daytrades."""

    commissions = COMMISSIONS9
    operations = OPERATION_SEQUENCE2
    positions = CONTAINER_POSITION4
    daytrades = CONTAINER_DAYTRADE_POSITION0
