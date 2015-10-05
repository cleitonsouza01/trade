"""Tests the method accumulate_operation() of the Accumulator."""

from __future__ import absolute_import
import unittest

import trade


class TestAccumulateOperationCase00(unittest.TestCase):
    """Test the accumulation of 1 operation."""

    def setUp(self):
        self.asset = trade.Asset()
        self.operation = trade.Operation(
            quantity=100,
            price=10,
            asset=self.asset,
            date='2015-01-01'
        )
        self.accumulator = trade.Accumulator(self.asset)
        self.result = self.accumulator.accumulate_operation(self.operation)

    def test_returned_result(self):
        self.assertEqual(self.result, {})

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.price, 10)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 100)

    def test_accumulator_results(self):
        self.assertEqual(self.accumulator.results, {})


class TestAccumulateOperationCase01(unittest.TestCase):
    """Attempt to accumulate a Operation with a different asset.

    The Accumulator should only accumulate operations from assets
    with the same code from self.asset.
    """

    def setUp(self):
        self.asset0 = trade.Asset()
        self.asset1 = trade.Asset(symbol='other')
        self.operation = trade.Operation(
            quantity=-100,
            price=10,
            asset=self.asset0,
            date='2015-01-01'
        )
        self.accumulator = trade.Accumulator(self.asset1)
        self.result = self.accumulator.accumulate_operation(self.operation)

    def test_returned_result(self):
        self.assertEqual(self.result, {})

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.price, 0)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 0)

    def test_accumulator_results(self):
        self.assertEqual(self.accumulator.results, {})


class TestAccumulateOperationCase02(unittest.TestCase):
    """Test the accumulation of 1 operation with commissions."""

    def setUp(self):
        asset = trade.Asset(symbol='some asset')
        operation = trade.Operation(
            date='2015-09-18',
            asset=asset,
            quantity=20,
            price=10
        )
        comissions = {
            'some comission': 1,
            'other comission': 3,
        }
        container = trade.OperationContainer(
            operations=[operation],
            commissions=comissions
        )
        container.tasks = [
            trade.plugins.fetch_exercises,
            trade.plugins.fetch_daytrades,
        ]
        container.fetch_positions()
        self.accumulator = trade.Accumulator(asset)
        operation = container.positions['operations'][asset.symbol]
        self.accumulator.accumulate_operation(operation)

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.price, 10.2)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 20)

    def test_accumulator_results(self):
        self.assertEqual(self.accumulator.results, {})


class TestAccumulateOperationCase03(unittest.TestCase):
    """Test the accumulation of 1 operation with zero price."""

    def setUp(self):
        asset = trade.Asset(symbol='some asset')
        operation = trade.Operation(
            date='2015-09-18',
            asset=asset,
            quantity=20,
            price=0
        )
        container = trade.OperationContainer(
            operations=[operation]
        )
        container.tasks = [
            trade.plugins.fetch_exercises,
            trade.plugins.fetch_daytrades,
        ]
        container.fetch_positions()
        self.accumulator = trade.Accumulator(asset)
        operation = container.positions['operations'][asset.symbol]
        self.accumulator.accumulate_operation(operation)

    def test_accumulator_average_price(self):
        self.assertEqual(self.accumulator.price, 0)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 20)

    def test_accumulator_results(self):
        self.assertEqual(self.accumulator.results, {})


class TestAccumulateOperationCase04(unittest.TestCase):
    """Test the accumulation of 2 operations in consecutive dates."""

    def setUp(self):
        asset = trade.Asset(symbol='some asset')
        operation = trade.Operation(
            date='2015-09-18',
            asset=asset,
            quantity=20,
            price=10
        )
        container = trade.OperationContainer(
            operations=[operation]
        )
        container.tasks = [
            trade.plugins.fetch_exercises,
            trade.plugins.fetch_daytrades,
        ]
        container.fetch_positions()
        self.accumulator = trade.Accumulator(asset)

        self.accumulator.accumulate_operation(
            container.positions['operations'][asset.symbol]
        )

        operation2 = trade.Operation(
            date='2015-09-19',
            asset=asset,
            quantity=-20,
            price=0
        )
        self.accumulator.accumulate_operation(operation2)

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.price, 0)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 0)

    def test_accumulator_results(self):
        self.assertEqual(
            self.accumulator.results,
            {'trades': -200}
        )


class TestAccumulateOperationCase05(unittest.TestCase):
    """Test the accumulation of empty operations."""

    def setUp(self):
        asset = trade.Asset(symbol='some asset')
        operation = trade.Operation(
            date='2015-09-18',
            asset=asset,
            quantity=0,
            price=0
        )
        self.accumulator = trade.Accumulator(asset)
        self.accumulator.accumulate_operation(operation)

        operation2 = trade.Operation(
            date='2015-09-19',
            asset=asset,
            quantity=0,
            price=0,
            results={
                'some result': 1000
            }
        )
        self.accumulator.accumulate_operation(operation2)

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.price, 0)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 0)

    def test_accumulator_results(self):
        self.assertEqual(self.accumulator.results['some result'], 1000)
