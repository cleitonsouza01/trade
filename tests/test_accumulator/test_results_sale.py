"""Tests the result calc for sale operations."""

from __future__ import absolute_import
import unittest

from trade import Accumulator

from . fixture_operations import (
    ASSET,
    OPERATION9, OPERATION10, OPERATION11, OPERATION12, OPERATION13,
    OPERATION14, OPERATION15, OPERATION16, OPERATION17,
)
from . fixture_logs import (
    EXPECTED_LOG0, EXPECTED_LOG1, EXPECTED_LOG2, EXPECTED_LOG3,
    EXPECTED_LOG4, EXPECTED_LOG5, EXPECTED_LOG6
)


class TestAccumulatorSaleResults(unittest.TestCase):

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION9)
        self.accumulator.accumulate_occurrence(OPERATION10)


class TestAccumulatorResultsSaleCase00(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG0)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {})


class TestAccumulatorResultsSaleCase01(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        super(TestAccumulatorResultsSaleCase01, self).setUp()
        self.accumulator.accumulate_occurrence(OPERATION11)

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG1)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {})


class TestAccumulatorResultsSaleCase02(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        super(TestAccumulatorResultsSaleCase02, self).setUp()
        self.accumulator.accumulate_occurrence(OPERATION11)
        self.accumulator.accumulate_occurrence(OPERATION12)

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG2)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 1000})


class TestAccumulatorResultsSaleCase04(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        super(TestAccumulatorResultsSaleCase04, self).setUp()
        self.accumulator.accumulate_occurrence(OPERATION11)
        self.accumulator.accumulate_occurrence(OPERATION12)
        self.accumulator.accumulate_occurrence(OPERATION13)

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG3)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 1000})


class TestAccumulatorResultsSaleCase05(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        super(TestAccumulatorResultsSaleCase05, self).setUp()
        self.accumulator.accumulate_occurrence(OPERATION11)
        self.accumulator.accumulate_occurrence(OPERATION12)
        self.accumulator.accumulate_occurrence(OPERATION13)
        self.accumulator.accumulate_occurrence(OPERATION14)

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG4)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 3000})


class TestAccumulatorResultsSaleCase06(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        super(TestAccumulatorResultsSaleCase06, self).setUp()

        self.accumulator.accumulate_occurrence(OPERATION11)
        self.accumulator.accumulate_occurrence(OPERATION12)
        self.accumulator.accumulate_occurrence(OPERATION13)
        self.accumulator.accumulate_occurrence(OPERATION15)

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG5)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 2000})


class TestAccumulatorResultsSaleCase07(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION16)
        self.accumulator.accumulate_occurrence(OPERATION17)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG6)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 500})
