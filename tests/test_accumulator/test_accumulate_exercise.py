from __future__ import absolute_import
import unittest

import trade


class Test_accumulate_exercise_Case_00(unittest.TestCase):
    """Accumulate a Option operation.
    """

    def setUp(self):
        self.asset = trade.Asset(name='Main')
        self.option = trade.Option(
                    name='Option',
                    expiration_date='2015-12-31',
                    underlying_assets=[self.asset],
                    ratio=1
                )

        # Accumulate a option operation
        self.operation = trade.Operation(
                            quantity=100,
                            price=10,
                            asset=self.option,
                            date='2015-01-01'
                        )
        self.accumulator = trade.Accumulator(self.option)
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


class Test_accumulate_exercise_Case_01(unittest.TestCase):
    """Accumulate a Option operation, and then its Exercise operation."""


    def setUp(self):

        # create a option and a underlying asset
        self.asset = trade.Asset(name='Main')
        self.option = trade.Option(
                    name='Option',
                    expiration_date='2015-12-31',
                    underlying_assets=[self.asset],
                    ratio=1
                )

        # create a accumultor for the options, a accumulator for the asset
        self.option_accumulator = trade.Accumulator(self.option)
        self.asset_accumulator = trade.Accumulator(self.asset)

        # Accumulate a option operation
        self.operation = trade.Operation(
                            quantity=100,
                            price=10,
                            asset=self.option,
                            date='2015-01-01'
                        )

        self.option_accumulator.accumulate_operation(self.operation)

        # Accumulate a exercise operation on the asset accumulator
        # and on the option accumulator
        # When accumulating operations, the Operation object should
        # be passed to the accumulator of all its assets
        self.exercise = trade.Exercise(
                            quantity=100,
                            price=10,
                            asset=self.option,
                            date='2015-01-01'
                        )
        self.exercise.fetch_operations()
        self.asset_accumulator.accumulate_operation(self.exercise)
        self.option_accumulator.accumulate_operation(self.exercise)


    def test_asset_accumulator_price(self):
        self.assertEqual(self.asset_accumulator.price, 10)

    def test_asset_accumulator_quantity(self):
        self.assertEqual(self.asset_accumulator.quantity, 100)

    def test_asset_accumulator_results(self):
        self.assertEqual(
            self.asset_accumulator.results,
            {'daytrades': 0, 'trades': 0}
        )

    def test_option_accumulator_price(self):
        self.assertEqual(self.option_accumulator.price, 0)

    def test_option_accumulator_quantity(self):
        self.assertEqual(self.option_accumulator.quantity, 0)

    def test_option_accumulator_results(self):
        self.assertEqual(
            self.option_accumulator.results,
            {'daytrades': 0, 'trades': 0}
        )


class Test_accumulate_exercise_Case_02(unittest.TestCase):
    """Accumulate a operation, an option and then the exericse."""

    def setUp(self):

        # create a option and a underlying asset
        self.asset = trade.Asset(name='Main')
        self.option = trade.Option(
                    name='Option',
                    expiration_date='2015-12-31',
                    underlying_assets=[self.asset],
                    ratio=1
                )

        # create a accumultor for the options, a accumulator for the asset
        self.option_accumulator = trade.Accumulator(self.option)
        self.asset_accumulator = trade.Accumulator(self.asset)

        # Accumulate a option operation
        self.operation = trade.Operation(
                            quantity=100,
                            price=10,
                            asset=self.option,
                            date='2015-01-01'
                        )

        self.option_accumulator.accumulate_operation(self.operation)

        # Accumulate a exercise operation on the asset accumulator
        # and on the option accumulator
        # When accumulating operations, the Operation object should
        # be passed to the accumulator of all its assets
        self.exercise = trade.Exercise(
                            quantity=100,
                            price=10,
                            asset=self.option,
                            date='2015-01-01'
                        )
        self.exercise.fetch_operations()
        self.asset_accumulator.accumulate_operation(self.exercise)
        self.option_accumulator.accumulate_operation(self.exercise)


    def test_asset_accumulator_price(self):
        self.assertEqual(self.asset_accumulator.price, 10)

    def test_asset_accumulator_quantity(self):
        self.assertEqual(self.asset_accumulator.quantity, 100)

    def test_asset_accumulator_results(self):
        self.assertEqual(
            self.asset_accumulator.results,
            {'daytrades': 0, 'trades': 0}
        )

    def test_option_accumulator_price(self):
        self.assertEqual(self.option_accumulator.price, 0)

    def test_option_accumulator_quantity(self):
        self.assertEqual(self.option_accumulator.quantity, 0)

    def test_option_accumulator_results(self):
        self.assertEqual(
            self.option_accumulator.results,
            {'daytrades': 0, 'trades': 0}
        )
