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

    def setUp(self):
        self.container = trade.OperationContainer()


class TestContainerPropertiesCase00(TestContainerProperties):
    """Test the volume property of the Container."""

    def setUp(self):
        super(TestContainerPropertiesCase00, self).setUp()
        self.container.operations = [copy.deepcopy(OPERATION39)]
        self.container.fetch_positions()

    def test_volume_00(self):
        self.assertEqual(self.container.volume, 20)


class TestContainerPropertiesCase01(TestContainerProperties):
    """Test the volume property of the Container."""

    def setUp(self):
        super(TestContainerPropertiesCase01, self).setUp()
        self.container.operations = copy.deepcopy(OPERATION_SEQUENCE6)
        self.container.fetch_positions()

    def test_volume_01(self):
        self.assertEqual(self.container.volume, 25)


class TestContainerPropertiesCase02(TestContainerProperties):
    """Test the volume property of the Container."""

    def setUp(self):
        super(TestContainerPropertiesCase02, self).setUp()
        self.container.operations = copy.deepcopy(OPERATION_SEQUENCE7)
        self.container.fetch_positions()

    def test_volume_02(self):
        self.assertEqual(self.container.volume, 125)
