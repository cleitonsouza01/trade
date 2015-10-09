"""Tests the result calc for purchase operations."""

from __future__ import absolute_import

from tests.fixtures.operations import (
    OPERATION0, OPERATION1, OPERATION2, OPERATION3, OPERATION4, OPERATION5,
    OPERATION6, OPERATION7, OPERATION8,
)
from . fixture_logs import (
    EXPECTED_LOG7, EXPECTED_LOG8, EXPECTED_LOG9, EXPECTED_LOG10,
    EXPECTED_LOG11, EXPECTED_LOG12, EXPECTED_LOG13, EXPECTED_LOG14,
    LogTest
)


class TestAccumulatorResultsPurchaseCase00(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [OPERATION0, OPERATION1]

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG7)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {})


class TestAccumulatorResultsPurchaseCase01(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [OPERATION0, OPERATION1, OPERATION2]

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG8)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {})

    def test_current_quantity(self):
        self.assertEqual(self.accumulator.data['quantity'], -100)

    def test_current_price(self):
        self.assertEqual(self.accumulator.data['price'], 10)


class TestAccumulatorResultsPurchaseCase02(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [OPERATION0, OPERATION1, OPERATION2, OPERATION3]

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG11)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': -1000})


class TestAccumulatorResultsPurchaseCase03(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [
        OPERATION0, OPERATION1, OPERATION2, OPERATION3, OPERATION4
    ]

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG9)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': -1000})


class TestAccumulatorResultsPurchaseCase04(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [
        OPERATION0, OPERATION1, OPERATION2, OPERATION3, OPERATION4,
        OPERATION5
    ]

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG10)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': -3000})


class TestAccumulatorResultsPurchaseCase05(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [
        OPERATION0, OPERATION1, OPERATION2, OPERATION3, OPERATION4,
        OPERATION6
    ]

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG12)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': -2000})


class TestAccumulatorResultsPurchaseCase06(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [OPERATION7, OPERATION1]

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG14)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 1000})


class TestAccumulatorResultsPurchaseCase07(LogTest):
    """Test profits or losses originating from purchase operations."""

    occurrences = [OPERATION8, OPERATION1]

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG13)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 500})
