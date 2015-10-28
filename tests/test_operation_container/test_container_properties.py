"""Test the properties of the Accumulator."""

from __future__ import absolute_import
import unittest
import copy

import trade

from tests.fixtures.operations import OPERATION39
from tests.fixtures.operation_sequences import (
    OPERATION_SEQUENCE6, OPERATION_SEQUENCE7
)


class TestContainerProperties(unittest.TestCase):
    """A base class with all operations used in the test cases."""

    operations = []
    volume = 0

    def setUp(self):
        self.container = trade.OperationContainer(
            operations=copy.deepcopy(self.operations)
        )
        self.container.fetch_positions()

    def test_volume_00(self):
        self.assertEqual(self.container.volume, self.volume)


class TestContainerPropertiesCase00(TestContainerProperties):
    """Test the volume property of the Container."""

    volume = 20
    operations = [OPERATION39]


class TestContainerPropertiesCase01(TestContainerProperties):
    """Test the volume property of the Container."""

    volume = 25
    operations = OPERATION_SEQUENCE6


class TestContainerPropertiesCase02(TestContainerProperties):
    """Test the volume property of the Container."""

    volume = 125
    operations = OPERATION_SEQUENCE7
