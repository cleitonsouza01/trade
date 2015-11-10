"""Tests for the prorate_commissions() method of Accumulator."""

from __future__ import absolute_import

from .fixture_positions import (
    POSITION01, POSITION02, POSITION03, POSITION04, POSITION05, POSITION06,
    POSITION07, DT_POSITION10
)
from .container_test_base import TestFetchPositions
from tests.fixtures.operations import OPERATION39
from tests.fixtures.commissions import (
    COMMISSIONS9, COMMISSIONS10, COMMISSIONS11,
)
from tests.fixtures.assets import (
    ASSET, ASSET2, ASSET3
)
from tests.fixtures.operation_sequences import (
    OPERATION_SEQUENCE2, OPERATION_SEQUENCE27, OPERATION_SEQUENCE28,
    OPERATION_SEQUENCE29
)


class TestProrateCommissionsByPositionCase01(TestFetchPositions):
    """Test pro rata of one commission for one operation."""

    commissions = COMMISSIONS11
    operations = [OPERATION39]
    positions = {
        ASSET.symbol: POSITION01,
    }


class TestProrateCommissionsByPositionCase02(TestFetchPositions):
    """Test pro rata of 1 commission for 3 operations."""

    commissions = COMMISSIONS11
    operations = OPERATION_SEQUENCE27
    positions = {
        ASSET.symbol: POSITION02,
        ASSET2.symbol: POSITION02,
    }


class TestProrateCommissionsByPositionCase03(TestFetchPositions):
    """Test pro rata of 1 commission for 2 operations."""

    commissions = COMMISSIONS11
    operations = OPERATION_SEQUENCE28
    positions = {
        ASSET.symbol: POSITION04,
        ASSET2.symbol: POSITION05,
    }


class TestProrateCommissionsByPositionCase04(TestFetchPositions):
    """Test pro rata of 1 commission for 3 sale operations."""

    commissions = COMMISSIONS10
    operations = OPERATION_SEQUENCE29
    positions = {
        ASSET.symbol: POSITION01,
        ASSET2.symbol: POSITION01,
        ASSET3.symbol: POSITION03
    }


class TestProrateCommissionsByPositionCase05(TestFetchPositions):
    """Test pro rata of 1 commission for daytrades."""

    commissions = COMMISSIONS9
    operations = OPERATION_SEQUENCE2
    positions = {
        ASSET.symbol: POSITION06,
        ASSET2.symbol: POSITION07
    }
    daytrades = {
        ASSET.symbol: DT_POSITION10
    }
