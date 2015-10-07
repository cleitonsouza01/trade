"""Tests the method accumulate_occurrence() of the Accumulator."""

from __future__ import absolute_import
import unittest
import copy

import trade
from tests.fixtures.operations import (
    ASSET, OPERATION18, OPERATION19, OPERATION20, OPERATION21, OPERATION22,
    OPERATION23
)
from tests.fixtures.commissions import (
    COMMISSIONS13
)

class TestAccumulateOperation(unittest.TestCase):

    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET)


class TestAccumulateOperationCase00(TestAccumulateOperation):
    """Test the accumulation of 1 operation."""

    def setUp(self):
        super(TestAccumulateOperationCase00, self).setUp()
        self.operation = copy.deepcopy(OPERATION18)
        self.accumulator.accumulate_occurrence(self.operation)

    def test_returned_result(self):
        self.assertEqual(self.operation.results, {})

    def test_accumulator_price(self):
        self.assertEqual(self.operation.price, 10)

    def test_accumulator_quantity(self):
        self.assertEqual(self.operation.quantity, 100)

    def test_accumulator_results(self):
        self.assertEqual(self.operation.results, {})


class TestAccumulateOperationCase01(TestAccumulateOperation):
    """Attempt to accumulate a Operation with a different asset.

    The Accumulator should only accumulate operations from assets
    with the same code from self.asset.
    """

    def setUp(self):
        super(TestAccumulateOperationCase01, self).setUp()
        self.operation = copy.deepcopy(OPERATION18)
        self.accumulator = trade.Accumulator(trade.Asset(symbol='other'))
        self.accumulator.accumulate_occurrence(self.operation)

    def test_returned_result(self):
        self.assertEqual(self.operation.results, {})

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.price, 0)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 0)

    def test_accumulator_results(self):
        self.assertEqual(self.accumulator.results, {})


class TestAccumulateOperationCase02(TestAccumulateOperation):
    """Test the accumulation of 1 operation with commissions."""

    def setUp(self):
        super(TestAccumulateOperationCase02, self).setUp()
        container = trade.OperationContainer(
            operations=[copy.deepcopy(OPERATION19)],
            commissions=COMMISSIONS13
        )
        container.fetch_positions()
        operation = container.positions['operations'][ASSET.symbol]
        self.accumulator.accumulate_occurrence(operation)

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.price, 10.2)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 20)

    def test_accumulator_results(self):
        self.assertEqual(self.accumulator.results, {})


class TestAccumulateOperationCase03(TestAccumulateOperation):
    """Test the accumulation of 1 operation with zero price."""

    def setUp(self):
        super(TestAccumulateOperationCase03, self).setUp()
        container = trade.OperationContainer(
            operations=[copy.deepcopy(OPERATION20)]
        )
        container.fetch_positions()
        operation = container.positions['operations'][ASSET.symbol]
        self.accumulator.accumulate_occurrence(operation)

    def test_accumulator_average_price(self):
        self.assertEqual(self.accumulator.price, 0)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 20)

    def test_accumulator_results(self):
        self.assertEqual(self.accumulator.results, {})


class TestAccumulateOperationCase04(TestAccumulateOperation):
    """Test the accumulation of 2 operations in consecutive dates."""

    def setUp(self):
        super(TestAccumulateOperationCase04, self).setUp()
        container = trade.OperationContainer(
            operations=[copy.deepcopy(OPERATION19)]
        )
        container.fetch_positions()
        self.accumulator.accumulate_occurrence(
            container.positions['operations'][ASSET.symbol]
        )
        self.accumulator.accumulate_occurrence(copy.deepcopy(OPERATION21))

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.price, 0)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 0)

    def test_accumulator_results(self):
        self.assertEqual(self.accumulator.results, {'trades': -200})


class TestAccumulateOperationCase05(TestAccumulateOperation):
    """Test the accumulation of empty operations."""

    def setUp(self):
        super(TestAccumulateOperationCase05, self).setUp()
        self.accumulator.accumulate_occurrence(OPERATION22)
        operation2 = copy.deepcopy(OPERATION23)
        operation2.raw_results = {
            'some result': 1000
        }
        self.accumulator.accumulate_occurrence(operation2)

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.price, 0)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 0)

    def test_accumulator_results(self):
        self.assertEqual(self.accumulator.results['some result'], 1000)
