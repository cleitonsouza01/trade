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

    def setUp(self):
        self.container = trade.OperationContainer(
            operations=copy.deepcopy(self.operations)
        )
        self.container.fetch_positions()


class TestContainerPropertiesCase00(TestContainerProperties):
    """Test the volume property of the Container."""

    operations = [OPERATION39]

    def test_volume_00(self):
        self.assertEqual(self.container.volume, 20)


class TestContainerPropertiesCase01(TestContainerProperties):
    """Test the volume property of the Container."""

    operations = OPERATION_SEQUENCE6

    def test_volume_01(self):
        self.assertEqual(self.container.volume, 25)


class TestContainerPropertiesCase02(TestContainerProperties):
    """Test the volume property of the Container."""

    operations = OPERATION_SEQUENCE7

    def test_volume_02(self):
        self.assertEqual(self.container.volume, 125)
