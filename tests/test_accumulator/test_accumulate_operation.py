from __future__ import absolute_import
import unittest

from trade import Accumulator as AssetAccumulator, OperationContainer
from trade import Asset, Operation


class Test_accumulate_operation_Case_00(unittest.TestCase):

    def setUp(self):
        self.asset = Asset()
        self.operation = Operation(
                            quantity=100,
                            price=10,
                            asset=self.asset,
                            date='2015-01-01'
                        )
        self.accumulator = AssetAccumulator(self.asset, logging=True)
        self.result = self.accumulator.accumulate_operation(self.operation)

    def test_returned_result(self):
        self.assertEqual(self.result, {'trades': 0})


class Test_accumulate_operation_Case_01(unittest.TestCase):

    def setUp(self):
        self.asset0 = Asset()
        self.asset1 = Asset('other')
        self.operation = Operation(
                            quantity=100,
                            price=10,
                            asset=self.asset0,
                            date='2015-01-01'
                        )
        self.accumulator = AssetAccumulator(self.asset1, logging=True)
        self.result = self.accumulator.accumulate_operation(self.operation)

    def test_returned_result(self):
        self.assertEqual(self.result, {'trades': 0})


class Test_accumulate_operation_Case_02(unittest.TestCase):

    def setUp(self):
        asset = Asset('some asset')
        operation = Operation(
                        date='2015-09-18',
                        asset=asset,
                        quantity=20,
                        price=10
                    )
        comissions = {
            'some comission': 1,
            'other comission': 3,
        }
        container = OperationContainer(
                        operations=[operation],
                        commissions=comissions
                    )
        container.fetch_positions()
        self.accumulator = AssetAccumulator(asset)
        operation = container.common_operations[asset]
        self.accumulator.accumulate_operation(operation)

    def test_accumulator_average_price(self):
        self.assertEqual(self.accumulator.price, 10.2)
