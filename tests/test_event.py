from __future__ import absolute_import
import unittest

import trade


class TestBaseEventBehavior(unittest.TestCase):
    """Test the Event class and its default behavior.
    """

    def setUp(self):
        self.asset = trade.Asset()
        self.date = '2015-09-29'
        self.event = trade.Event(asset=self.asset, date=self.date)

    def test_event_should_exist(self):
        self.assertTrue(self.event)

    def test_event_asset(self):
        self.assertEqual(self.event.asset, self.asset)

    def test_event_date(self):
        self.assertEqual(self.event.date, self.date)

    def test_event_update_portfolio(self):
        expected_return = (10,1)
        self.assertEqual(self.event.update_portfolio(10,1,{}), expected_return)


class TestBaseEventAccumulation(unittest.TestCase):
    """The the accumulation of an Event object by the Accumulator.
    """

    def setUp(self):
        self.asset = trade.Asset()
        self.date = '2015-09-29'
        self.accumulator = trade.Accumulator(self.asset)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}

    def test_check_initial_quantity(self):
        self.assertEqual(self.accumulator.quantity, 100)

    def test_check_initial_price(self):
        self.assertEqual(self.accumulator.price, 10)

    def test_check_initial_results(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})

    def test_check_quantity_after_event(self):
        event = trade.Event(asset=self.asset, date=self.date)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.quantity, 100)

    def test_check_price_after_event(self):
        event = trade.Event(asset=self.asset, date=self.date)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.price, 10)

    def test_check_results_after_event(self):
        event = trade.Event(asset=self.asset, date=self.date)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.results, {'trades': 1200})



class TestStockSplitEvent_Case_00(unittest.TestCase):
    """Test the accumulation of a StockSplit event by the Accumulator.
    """

    def setUp(self):
        self.asset = trade.Asset()
        self.accumulator = trade.Accumulator(self.asset, logging=True)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}
        event = trade.plugins.StockSplit(
                    asset=self.asset,
                    date='2015-09-24',
                    factor=2
                )
        self.accumulator.accumulate_event(event)

    def test_check_quantity_after_split(self):
        self.assertEqual(self.accumulator.quantity, 200)

    def test_check_price_after_split(self):
        self.assertEqual(self.accumulator.price, 5)

    def test_check_results_after_split(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})


class TestReverseStockSplitEvent_Case_00(unittest.TestCase):
    """Test the accumulation of a ReverseStockSplit event.
    """

    def setUp(self):
        self.asset = trade.Asset()
        self.accumulator = trade.Accumulator(self.asset, logging=True)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}
        event = trade.plugins.ReverseStockSplit(
                    asset=self.asset,
                    date='2015-09-24',
                    factor=2
                )
        self.accumulator.accumulate_event(event)

    def test_check_quantity_after_split(self):
        self.assertEqual(self.accumulator.quantity, 50)

    def test_check_price_after_split(self):
        self.assertEqual(self.accumulator.price, 20)

    def test_check_results_after_split(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})
