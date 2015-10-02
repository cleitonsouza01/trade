from __future__ import absolute_import
import unittest

import trade


class TestBonusSharesEvent_Case_00(unittest.TestCase):
    """Test a bonus shares event with factor 1."""

    def setUp(self):
        self.asset = trade.Asset()
        self.accumulator = trade.Accumulator(self.asset, logging=True)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}
        event = trade.plugins.BonusShares(
                    asset=self.asset,
                    date='2015-09-24',
                    factor=1
                )
        self.accumulator.accumulate_event(event)

    def test_check_quantity_after_split(self):
        self.assertEqual(self.accumulator.quantity, 200)

    def test_check_price_after_split(self):
        self.assertEqual(self.accumulator.price, 5)

    def test_check_results_after_split(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})


class TestBonusSharesEvent_Case_01(unittest.TestCase):
    """Test a bonus shares event with factor 2."""

    def setUp(self):
        self.asset = trade.Asset()
        self.accumulator = trade.Accumulator(self.asset, logging=True)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}
        event = trade.plugins.BonusShares(
                    asset=self.asset,
                    date='2015-09-24',
                    factor=2
                )
        self.accumulator.accumulate_event(event)

    def test_check_quantity_after_split(self):
        self.assertEqual(self.accumulator.quantity, 300)

    def test_check_price_after_split(self):
        self.assertEqual(round(self.accumulator.price, 2), 3.33)

    def test_check_results_after_split(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})


class TestBonusSharesEvent_Case_02(unittest.TestCase):
    """Test a bonus shares event with factor 0.5."""

    def setUp(self):
        self.asset = trade.Asset()
        self.accumulator = trade.Accumulator(self.asset, logging=True)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}
        event = trade.plugins.BonusShares(
                    asset=self.asset,
                    date='2015-09-24',
                    factor=0.5
                )
        self.accumulator.accumulate_event(event)

    def test_check_quantity_after_split(self):
        self.assertEqual(self.accumulator.quantity, 150)

    def test_check_price_after_split(self):
        self.assertEqual(round(self.accumulator.price, 2), 6.67)

    def test_check_results_after_split(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})
