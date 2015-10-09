"""Tests the result calc for sale operations."""

from __future__ import absolute_import

from tests.fixtures.operations import (
    OPERATION9, OPERATION10, OPERATION11, OPERATION12, OPERATION13,
    OPERATION14, OPERATION15, OPERATION16, OPERATION17,
)
from . fixture_logs import (
    EXPECTED_LOG0, EXPECTED_LOG1, EXPECTED_LOG2, EXPECTED_LOG3,
    EXPECTED_LOG4, EXPECTED_LOG5, EXPECTED_LOG6,
    LogTest
)


class TestAccumulatorResultsSaleCase00(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = [
        OPERATION9, OPERATION10
    ]

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG0)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {})


class TestAccumulatorResultsSaleCase01(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = [
        OPERATION9, OPERATION10, OPERATION11
    ]

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG1)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {})


class TestAccumulatorResultsSaleCase02(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = [
        OPERATION9, OPERATION10, OPERATION11, OPERATION12
    ]

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG2)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 1000})


class TestAccumulatorResultsSaleCase04(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = [
        OPERATION9, OPERATION10, OPERATION11, OPERATION12, OPERATION13
    ]

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG3)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 1000})


class TestAccumulatorResultsSaleCase05(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = [
        OPERATION9, OPERATION10, OPERATION11, OPERATION12, OPERATION13,
        OPERATION14
    ]

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG4)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 3000})


class TestAccumulatorResultsSaleCase06(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = [
        OPERATION9, OPERATION10, OPERATION11, OPERATION12, OPERATION13,
        OPERATION15
    ]

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG5)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 2000})


class TestAccumulatorResultsSaleCase07(LogTest):
    """Test profits or losses originating from sale operations."""

    occurrences = [
        OPERATION16, OPERATION17
    ]

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG6)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 500})
