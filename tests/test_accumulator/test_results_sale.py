"""Tests the result calc for sale operations."""

from __future__ import absolute_import
import unittest

from trade import Accumulator

from tests.fixtures.operations import (
    OPERATION9, OPERATION10, OPERATION11, OPERATION12, OPERATION13,
    OPERATION14, OPERATION15, OPERATION16, OPERATION17,
)
from tests.fixtures.assets import (
    ASSET
)
from . fixture_logs import (
    EXPECTED_LOG0, EXPECTED_LOG1, EXPECTED_LOG2, EXPECTED_LOG3,
    EXPECTED_LOG4, EXPECTED_LOG5, EXPECTED_LOG6
)


class TestAccumulatorSaleResults(unittest.TestCase):

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate(OPERATION9)
        self.accumulator.accumulate(OPERATION10)


class TestAccumulatorResultsSaleCase00(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG0)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {})


class TestAccumulatorResultsSaleCase01(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        super(TestAccumulatorResultsSaleCase01, self).setUp()
        self.accumulator.accumulate(OPERATION11)

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG1)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {})


class TestAccumulatorResultsSaleCase02(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        super(TestAccumulatorResultsSaleCase02, self).setUp()
        self.accumulator.accumulate(OPERATION11)
        self.accumulator.accumulate(OPERATION12)

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG2)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 1000})


class TestAccumulatorResultsSaleCase04(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        super(TestAccumulatorResultsSaleCase04, self).setUp()
        self.accumulator.accumulate(OPERATION11)
        self.accumulator.accumulate(OPERATION12)
        self.accumulator.accumulate(OPERATION13)

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG3)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 1000})


class TestAccumulatorResultsSaleCase05(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        super(TestAccumulatorResultsSaleCase05, self).setUp()
        self.accumulator.accumulate(OPERATION11)
        self.accumulator.accumulate(OPERATION12)
        self.accumulator.accumulate(OPERATION13)
        self.accumulator.accumulate(OPERATION14)

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG4)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 3000})


class TestAccumulatorResultsSaleCase06(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        super(TestAccumulatorResultsSaleCase06, self).setUp()

        self.accumulator.accumulate(OPERATION11)
        self.accumulator.accumulate(OPERATION12)
        self.accumulator.accumulate(OPERATION13)
        self.accumulator.accumulate(OPERATION15)

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG5)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 2000})


class TestAccumulatorResultsSaleCase07(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate(OPERATION16)
        self.accumulator.accumulate(OPERATION17)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG6)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 500})
