"""Test the identification of Daytrades among Operations."""

from __future__ import absolute_import
import copy

from trade.trade import fetch_daytrades

from .container_test_base import TestFetchPositions
from .fixture_positions import (
    POSITION0, POSITION1, POSITION2,
    DT_POSITION0, DT_POSITION1, DT_POSITION2, DT_POSITION4,
    DT_POSITION5
)
from tests.fixtures.operations import (
    OPERATION32, OPERATION26
)
from tests.fixtures.assets import (
    ASSET, ASSET2, ASSET3,
)

from tests.fixtures.operation_sequences import (
    OPERATION_SEQUENCE0, OPERATION_SEQUENCE1, OPERATION_SEQUENCE2,
    OPERATION_SEQUENCE3, OPERATION_SEQUENCE4, OPERATION_SEQUENCE5
)

TASKS = [
    fetch_daytrades,
]


class TestContainerIndentifyDaytradesCase00(TestFetchPositions):
    """Test the identification of daytrade operations."""

    #volume = 50
    operations = OPERATION_SEQUENCE0
    daytrades = {
        ASSET.symbol: DT_POSITION4,
    }


class TestContainerIndentifyDaytradesCase01(TestFetchPositions):
    """Test the identification of daytrade operations."""

    #volume = 35
    operations = OPERATION_SEQUENCE1
    positions = POSITION0
    daytrades = {
        ASSET.symbol: DT_POSITION0,
    }


class TestContainerIndentifyDaytradesCase02(TestFetchPositions):
    """Test the identification of daytrade operations."""

    #volume = 70
    operations = OPERATION_SEQUENCE2
    positions = POSITION1
    daytrades = {
        ASSET.symbol: DT_POSITION0,
    }


class TestContainerIndentifyDaytradesCase03(TestFetchPositions):
    """Test the identification of daytrade operations."""

    #volume = 120
    operations = OPERATION_SEQUENCE3
    positions = POSITION0
    daytrades = {
        ASSET.symbol: DT_POSITION0,
        ASSET2.symbol: DT_POSITION1,
    }


class TestContainerIndentifyDaytradesCase04(TestFetchPositions):
    """Test the identification of daytrade operations."""

    #volume = 135
    operations = OPERATION_SEQUENCE3 + [copy.deepcopy(OPERATION26)]
    daytrades = {
        ASSET.symbol: DT_POSITION4,
        ASSET2.symbol: DT_POSITION1,
    }


class TestContainerIndentifyDaytradesCase05(TestFetchPositions):
    """Test the identification of daytrade operations."""

    #volume = 255
    operations = OPERATION_SEQUENCE4
    daytrades = {
        ASSET.symbol: DT_POSITION5,
        ASSET2.symbol: DT_POSITION1,
    }


class TestContainerIndentifyDaytradesCase06(TestFetchPositions):
    """Test the identification of daytrade operations."""

    #volume = 140
    operations = OPERATION_SEQUENCE3 + [copy.deepcopy(OPERATION32)]
    positions = POSITION2
    daytrades = {
        ASSET.symbol: DT_POSITION0,
        ASSET2.symbol: DT_POSITION1,
    }


class TestContainerIndentifyDaytradesCase07(TestFetchPositions):
    """Test the identification of daytrade operations."""

    #volume = 210
    operations = OPERATION_SEQUENCE3 + copy.deepcopy(OPERATION_SEQUENCE5)
    positions = POSITION2
    daytrades = {
        ASSET.symbol: DT_POSITION0,
        ASSET2.symbol: DT_POSITION1,
        ASSET3.symbol: DT_POSITION2,
    }
