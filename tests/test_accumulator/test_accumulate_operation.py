from __future__ import absolute_import
import unittest

import trade


class Test_accumulate_operation_Case_00(unittest.TestCase):

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
        self.assertEqual(self.result, {'trades': 0})

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.price, 10)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 100)

    def test_accumulator_results(self):
        self.assertEqual(
            self.accumulator.results,
            {'daytrades': 0, 'trades': 0}
        )


class Test_accumulate_operation_Case_01(unittest.TestCase):
    """Attempt to accumulate a Operation with a different asset.
    """

    def setUp(self):
        self.asset0 = trade.Asset()
        self.asset1 = trade.Asset('other')
        self.operation = trade.Operation(
                            quantity=-100,
                            price=10,
                            asset=self.asset0,
                            date='2015-01-01'
                        )
        self.accumulator = trade.Accumulator(self.asset1)
        self.result = self.accumulator.accumulate_operation(self.operation)

    def test_returned_result(self):
        self.assertEqual(self.result, {'trades': 0})

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.price, 0)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 0)

    def test_accumulator_results(self):
        self.assertEqual(
            self.accumulator.results,
            {'daytrades': 0, 'trades': 0}
        )


class Test_accumulate_operation_Case_02(unittest.TestCase):

    def setUp(self):
        asset = trade.Asset('some asset')
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
        container.fetch_positions_tasks = [
            trade.fetch_exercises,
            trade.fetch_daytrades,
            #trade.prorate_commissions
        ]
        container.fetch_positions()
        self.accumulator = trade.Accumulator(asset)
        operation = container.positions['common operations'][asset]
        self.accumulator.accumulate_operation(operation)

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.price, 10.2)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 20)

    def test_accumulator_results(self):
        self.assertEqual(
            self.accumulator.results,
            {'daytrades': 0, 'trades': 0}
        )


class Test_accumulate_operation_Case_03(unittest.TestCase):

    def setUp(self):
        asset = trade.Asset('some asset')
        operation = trade.Operation(
                        date='2015-09-18',
                        asset=asset,
                        quantity=20,
                        price=0
                    )
        container = trade.OperationContainer(
                        operations=[operation]
                    )
        container.fetch_positions_tasks = [
            trade.fetch_exercises,
            trade.fetch_daytrades,
            #trade.prorate_commissions
        ]
        container.fetch_positions()
        self.accumulator = trade.Accumulator(asset)
        operation = container.positions['common operations'][asset]
        self.accumulator.accumulate_operation(operation)

    def test_accumulator_average_price(self):
        self.assertEqual(self.accumulator.price, 0)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 20)

    def test_accumulator_results(self):
        self.assertEqual(
            self.accumulator.results,
            {'daytrades': 0, 'trades': 0}
        )


class Test_accumulate_operation_Case_04(unittest.TestCase):

    def setUp(self):
        asset = trade.Asset('some asset')
        operation = trade.Operation(
                        date='2015-09-18',
                        asset=asset,
                        quantity=20,
                        price=10
                    )
        container = trade.OperationContainer(
                        operations=[operation]
                    )
        container.fetch_positions_tasks = [
            trade.fetch_exercises,
            trade.fetch_daytrades,
            #trade.prorate_commissions
        ]
        container.fetch_positions()
        self.accumulator = trade.Accumulator(asset)

        self.accumulator.accumulate_operation(
            container.positions['common operations'][asset]
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
            {'daytrades': 0, 'trades': -200}
        )


class Test_accumulate_operation_Case_05(unittest.TestCase):

    def setUp(self):
        asset = trade.Asset('some asset')
        operation = trade.Operation(
                        date='2015-09-18',
                        asset=asset,
                        quantity=0,
                        price=0
                    )
        container = trade.OperationContainer(
                        operations=[operation]
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
