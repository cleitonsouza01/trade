"""Tests the result calc for purchase operations."""

from __future__ import absolute_import
import unittest

from trade import Accumulator

from tests.fixtures.operations import (
    OPERATION0, OPERATION1, OPERATION2, OPERATION3, OPERATION4, OPERATION5,
    OPERATION6, OPERATION7, OPERATION8,
)
from tests.fixtures.assets import (
    ASSET,
)
from . fixture_logs import (
    EXPECTED_LOG7, EXPECTED_LOG8, EXPECTED_LOG9, EXPECTED_LOG10,
    EXPECTED_LOG11, EXPECTED_LOG12, EXPECTED_LOG13, EXPECTED_LOG14
)


class TestAccumulatorResultsPurchaseCase00(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG7)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {})


class TestAccumulatorResultsPurchaseCase01(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(OPERATION2)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG8)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {})

    def test_current_quantity(self):
        self.assertEqual(self.accumulator.quantity, -100)

    def test_current_price(self):
        self.assertEqual(self.accumulator.price, 10)


class TestAccumulatorResultsPurchaseCase02(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(OPERATION2)
        self.accumulator.accumulate_occurrence(OPERATION3)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG11)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': -1000})


class TestAccumulatorResultsPurchaseCase03(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(OPERATION2)
        self.accumulator.accumulate_occurrence(OPERATION3)
        self.accumulator.accumulate_occurrence(OPERATION4)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG9)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': -1000})


class TestAccumulatorResultsPurchaseCase04(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(OPERATION2)
        self.accumulator.accumulate_occurrence(OPERATION3)
        self.accumulator.accumulate_occurrence(OPERATION4)
        self.accumulator.accumulate_occurrence(OPERATION5)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG10)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': -3000})


class TestAccumulatorResultsPurchaseCase05(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(OPERATION2)
        self.accumulator.accumulate_occurrence(OPERATION3)
        self.accumulator.accumulate_occurrence(OPERATION4)
        self.accumulator.accumulate_occurrence(OPERATION6)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG12)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': -2000})


class TestAccumulatorResultsPurchaseCase06(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION7)
        self.accumulator.accumulate_occurrence(OPERATION1)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG14)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 1000})


class TestAccumulatorResultsPurchaseCase07(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION8)
        self.accumulator.accumulate_occurrence(OPERATION1)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG13)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 500})
