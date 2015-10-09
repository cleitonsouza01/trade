"""Test the function to fetch the exercise premium."""

from __future__ import absolute_import
import unittest
import copy

import trade

from tests.fixtures.operations import  (
    OPERATION46,
    EXERCISE_OPERATION4,
    OPTION_OPERATION1, OPTION_OPERATION2
)
from tests.fixtures.assets import (
    ASSET, OPTION1,
)


class TestExercisePremium(unittest.TestCase):

    def setUp(self):
        self.portfolio = trade.Portfolio()
        self.operation = copy.deepcopy(OPERATION46)
        self.exercise = copy.deepcopy(EXERCISE_OPERATION4)
        self.option_operation = copy.deepcopy(OPTION_OPERATION1)
        self.option_operation2 = copy.deepcopy(OPTION_OPERATION2) #20@1
        self.portfolio.accumulate(self.operation)


class TestExercisePremiumCase00(TestExercisePremium):
    """Test the accumulation of one operation with underlying assets."""

    def setUp(self):
        super(TestExercisePremiumCase00, self).setUp()
        self.portfolio.accumulate(self.option_operation)
        self.portfolio.accumulate(self.exercise)

    def test_option_name(self):
        self.assertEqual(OPTION1.symbol, 'some option')

    def test_option_expiration_date(self):
        self.assertEqual(OPTION1.expiration_date, '2015-10-02')

    def test_underlying_assets(self):
        self.assertEqual(OPTION1.underlying_assets, {ASSET: 1})

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.subjects.keys()), 2)

    def test_asset_accumulator_quantity(self):
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['quantity'], 20)

    def test_asset_accumulator_price(self):
        """Should have the premium included on the price"""
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['price'], 5.5)

    def test_option_accumulator_quantity(self):
        self.assertEqual(self.portfolio.subjects[OPTION1.symbol].data['quantity'], 0)

    def test_option_accumulator_price(self):
        self.assertEqual(self.portfolio.subjects[OPTION1.symbol].data['price'], 0)


class TestExercisePremiumCase01(TestExercisePremium):
    """Test the accumulation of one operation with underlying assets."""

    def setUp(self):
        super(TestExercisePremiumCase01, self).setUp()
        self.portfolio.accumulate(self.option_operation2)
        self.portfolio.accumulate(self.exercise)
        #print(self.exercise.operations[0].quantity)

    def test_portfolio_asset_keys(self):
        self.assertEqual(len(self.portfolio.subjects.keys()), 2)

    def test_asset_accumulator_quantity(self):
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['quantity'], 20)

    def test_asset_accumulator_price(self):
        """Should have the premium included on the price"""
        self.assertEqual(self.portfolio.subjects[ASSET.symbol].data['price'], 5.5)

    def test_option_accumulator_quantity(self):
        self.assertEqual(self.portfolio.subjects[OPTION1.symbol].data['quantity'], 10)

    def test_option_accumulator_price(self):
        self.assertEqual(self.portfolio.subjects[OPTION1.symbol].data['price'], 1)
