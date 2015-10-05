"""Test the properties of the Accumulator."""

from __future__ import absolute_import
import unittest

import trade


class TestTradeContainer_total_discount_value_one_discount(
        unittest.TestCase
    ):
    """Test the total_commission_value property of the Container."""

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        self.trade_container = trade.OperationContainer(commissions=discounts)

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_trade_container_raw_discounts(self):
        expected_discounts = {
            'some discount': 1,
        }
        self.assertEqual(self.trade_container.commissions, expected_discounts)

    def test_trade_container_total_discount_value_should_be_one(self):
        self.assertEqual(self.trade_container.total_commission_value, 1)


class TestTradeContainer_total_discount_value_multiple_discounts(
        unittest.TestCase
    ):
    """Test the total_commission_value property of the Container."""

    def setUp(self):
        discounts = {
            'some discount': 1,
            'other discount': 3,
        }
        self.trade_container = trade.OperationContainer(commissions=discounts)

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_check_raw_discounts(self):
        expected_discounts = {
            'some discount': 1,
            'other discount': 3,
        }
        self.assertEqual(self.trade_container.commissions, expected_discounts)

    def test_total_discount_value(self):
        self.assertEqual(self.trade_container.total_commission_value, 4)


class TestTradeContainer_volume_one_trade(unittest.TestCase):
    """Test the volume property of the Container."""

    def setUp(self):
        asset = trade.Asset('some asset')
        operation = trade.Operation(
            date='2015-09-21',
            asset=asset,
            quantity=10,
            price=2
        )
        self.trade_container = trade.OperationContainer(operations=[operation])

    def test_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_container_operations(self):
        self.assertEqual(len(self.trade_container.operations), 1)

    def test_container_volume(self):
        self.assertEqual(self.trade_container.volume, 20)


class TestTradeContainer_volume_multiple_trades_case_00(unittest.TestCase):
    """Test the volume property of the Container."""

    def setUp(self):
        asset = trade.Asset('some asset')
        operation1 = trade.Operation(
            date='2015-09-21',
            asset=asset,
            quantity=10,
            price=2
        )
        operation2 = trade.Operation(
            date='2015-09-21',
            asset=asset,
            quantity=5,
            price=1
        )
        self.trade_container = trade.OperationContainer(
            operations=[
                operation1,
                operation2
            ]
        )

    def testcontainer_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_container_operations(self):
        self.assertEqual(len(self.trade_container.operations), 2)

    def test_container_volume(self):
        self.assertEqual(self.trade_container.volume, 25)


class TestTradeContainer_volume_multiple_trades_case_01(unittest.TestCase):
    """Test the volume property of the Container."""

    def setUp(self):
        asset = trade.Asset('some asset')
        operation1 = trade.Operation(
            date='2015-09-21',
            asset=asset,
            quantity=-10,
            price=2
        )
        operation2 = trade.Operation(
            date='2015-09-21',
            asset=asset,
            quantity=5,
            price=1
        )
        self.trade_container = trade.OperationContainer(
            operations=[
                operation1,
                operation2
            ]
        )

    def test_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_container_operations(self):
        self.assertEqual(len(self.trade_container.operations), 2)

    def test_container_volume(self):
        self.assertEqual(self.trade_container.volume, 25)


class TestTradeContainer_volume_multiple_trades_case_02(unittest.TestCase):
    """Test the volume property of the Container."""

    def setUp(self):
        asset1 = trade.Asset('some asset')
        asset2 = trade.Asset('some other asset')
        operation1 = trade.Operation(
            date='2015-09-21',
            asset=asset1,
            quantity=-10,
            price=2
        )
        operation2 = trade.Operation(
            date='2015-09-21',
            asset=asset1,
            quantity=5,
            price=1
        )
        operation3 = trade.Operation(
            date='2015-09-21',
            asset=asset2,
            quantity=20,
            price=5
        )
        self.trade_container = trade.OperationContainer(
            operations=[
                operation1,
                operation2,
                operation3
            ]
        )

    def test_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_container_operations(self):
        self.assertEqual(len(self.trade_container.operations), 3)

    def test_container_volume(self):
        self.assertEqual(self.trade_container.volume, 125)
