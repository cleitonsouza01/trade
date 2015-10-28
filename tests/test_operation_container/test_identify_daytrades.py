"""Test the identification of Daytrades among Operations."""

from __future__ import absolute_import
import unittest
import copy

import trade

from .container_test_base import TestFetchPositions
from .fixture_positions import POSITION0, POSITION1, POSITION2
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
    trade.plugins.fetch_exercises,
    trade.plugins.fetch_daytrades,
]


class TestIdentifyDaytrades(unittest.TestCase):
    "Base class for daytrade identification tests."
    def setUp(self):
        self.container = trade.OperationContainer()
        self.container.tasks = TASKS


class TestContainerIndentifyDaytradesCase00(TestFetchPositions):
    """Test the identification of daytrade operations."""

    operations = OPERATION_SEQUENCE0
    positions = {}
    daytrades = {
        ASSET.symbol: {
            'quantity': 10,
            'buy quantity': 10,
            'buy price': 2,
            'sale quantity': -10,
            'sale price': 3,
            'result': {'daytrades': 10}
        },
    }


class TestContainerIndentifyDaytradesCase01(TestFetchPositions):
    """Test the identification of daytrade operations."""

    operations = OPERATION_SEQUENCE1
    positions = POSITION0
    daytrades = {
        ASSET.symbol: {
            'quantity': 5,
            'buy quantity': 5,
            'buy price': 2,
            'sale quantity': -5,
            'sale price': 3,
            'result': {'daytrades': 5}
        },
    }


class TestContainerIndentifyDaytradesCase02(TestFetchPositions):
    """Test the identification of daytrade operations."""

    operations = OPERATION_SEQUENCE2
    positions = POSITION1
    daytrades = {
        ASSET.symbol: {
            'quantity': 5,
            'buy quantity': 5,
            'buy price': 2,
            'sale quantity': -5,
            'sale price': 3,
            'result': {'daytrades': 5}
        },
    }


class TestContainerIndentifyDaytradesCase03(TestFetchPositions):
    """Test the identification of daytrade operations."""

    operations = OPERATION_SEQUENCE3
    positions = POSITION0
    daytrades = {
        ASSET.symbol: {
            'quantity': 5,
            'buy quantity': 5,
            'buy price': 2,
            'sale quantity': -5,
            'sale price': 3,
            'result': {'daytrades': 5}
        },
        ASSET2.symbol: {
            'quantity': 5,
            'buy quantity': 5,
            'buy price': 10,
            'sale quantity': -5,
            'sale price': 7,
            'result': {'daytrades': -15}
        },
    }


class TestContainerIndentifyDaytradesCase04(TestFetchPositions):
    """Test the identification of daytrade operations."""

    operations = OPERATION_SEQUENCE3 + [copy.deepcopy(OPERATION26)]
    positions = {}
    daytrades = {
        ASSET.symbol: {
            'quantity': 10,
            'buy quantity': 10,
            'buy price': 2,
            'sale quantity': -10,
            'sale price': 3,
            'result': {'daytrades': 10}
        },
        ASSET2.symbol: {
            'quantity': 5,
            'buy quantity': 5,
            'buy price': 10,
            'sale quantity': -5,
            'sale price': 7,
            'result': {'daytrades': -15}
        },
    }


class TestContainerIndentifyDaytradesCase05(TestFetchPositions):
    """Test the identification of daytrade operations."""

    operations = OPERATION_SEQUENCE4
    positions = {}
    daytrades = {
        ASSET.symbol: {
            'quantity': 10,
            'buy quantity': 10,
            'buy price': 2,
            'sale quantity': -10,
            'sale price': 15,
            'result': {'daytrades': 130}
        },
        ASSET2.symbol: {
            'quantity': 5,
            'buy quantity': 5,
            'buy price': 10,
            'sale quantity': -5,
            'sale price': 7,
            'result': {'daytrades': -15}
        },
    }


class TestContainerIndentifyDaytradesCase06(TestFetchPositions):
    """Test the identification of daytrade operations."""

    operations = OPERATION_SEQUENCE3 + [copy.deepcopy(OPERATION32)]
    positions = POSITION2
    daytrades = {
        ASSET.symbol: {
            'quantity': 5,
            'buy quantity': 5,
            'buy price': 2,
            'sale quantity': -5,
            'sale price': 3,
            'result': {'daytrades': 5}
        },
        ASSET2.symbol: {
            'quantity': 5,
            'buy quantity': 5,
            'buy price': 10,
            'sale quantity': -5,
            'sale price': 7,
            'result': {'daytrades': -15}
        },
    }


class TestContainerIndentifyDaytradesCase07(TestIdentifyDaytrades):
    """Test the identification of daytrade operations."""

    operations = OPERATION_SEQUENCE3 + [copy.deepcopy(OPERATION_SEQUENCE5)]
    positions = POSITION2
    daytrades = {
        ASSET.symbol: {
            'quantity': 5,
            'buy quantity': 5,
            'buy price': 2,
            'sale quantity': -5,
            'sale price': 3,
            'result': {'daytrades': 5}
        },
        ASSET2.symbol: {
            'quantity': 5,
            'buy quantity': 5,
            'buy price': 10,
            'sale quantity': -5,
            'sale price': 7,
            'result': {'daytrades': -15}
        },
        ASSET3.symbol: {
            'quantity': 10,
            'buy quantity':10,
            'buy price': 4,
            'sale quantity': -10,
            'sale price': 3,
            'result': {'daytrades': -10}
        },
    }
