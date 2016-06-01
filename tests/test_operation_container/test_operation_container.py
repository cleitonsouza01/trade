"""Test the creation of OperationContainer objects."""

from __future__ import absolute_import
import unittest
import copy

from trade import trade
from trade.container_tasks import (
    fetch_daytrades,
    add_to_position_group, find_volume,
)
from .container_test_base import TestFetchPositions
from tests.fixtures.operations import OPERATION24, OPERATION45
from tests.fixtures.commissions import COMMISSIONS12
from tests.fixtures.assets import ASSET


class TestContainerCreationCase00(unittest.TestCase):
    """Test the creation of a OperationContainer."""

    def setUp(self):
        self.container = trade.OperationContainer(
            operations=[],
            tasks=[find_volume]
        )

    def test_container_exists(self):
        self.assertTrue(self.container)


class TestContainerCreationCase01(unittest.TestCase):
    """Test the creation of a OperationContainer."""

    def setUp(self):
        self.container = trade.OperationContainer(
            operations=[],
            tasks=[find_volume]
        )
        self.container.commissions = COMMISSIONS12
        self.container.fetch_positions_tasks = [fetch_daytrades]
        self.container.fetch_positions()

    def test_container_exists(self):
        self.assertTrue(self.container)

    def test_container_commissions(self):
        self.assertEqual(self.container.commissions, COMMISSIONS12)


class TestContainerAddToPositions(TestFetchPositions):
    """Test add_to_position_operations method."""

    #volume = 20
    operations = [OPERATION24]
    positions = {
        ASSET.symbol: {
            'quantity': 20,
            'price': 3,
            'volume': 60,
            'commissions': {}
        },
    }

    def setUp(self):
        super(TestContainerAddToPositions, self).setUp()
        add_to_position_group(self.container, copy.deepcopy(OPERATION45))
