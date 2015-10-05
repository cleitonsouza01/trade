"""Test the properties of the Accumulator."""

from __future__ import absolute_import
import unittest

import trade


class TestContainerPropertiesCase00(
        unittest.TestCase
    ):
    """Test the total_commission_value property of the Container."""

    def setUp(self):
        discounts = {
            'some discount': 1,
        }
        self.trade_container = trade.OperationContainer(commissions=discounts)

    def test_container_exists(self):
        self.assertTrue(self.trade_container)

    def test_raw_discounts(self):
        expected_discounts = {
            'some discount': 1,
        }
        self.assertEqual(self.trade_container.commissions, expected_discounts)

    def test_total_commission_value(self):
        self.assertEqual(self.trade_container.total_commission_value, 1)


class TestContainerPropertiesCase01(
        unittest.TestCase
    ):
    """Test the total_commission_value property of the Container."""

    def setUp(self):
        discounts = {
            'some discount': 1,
            'other discount': 3,
        }
        self.trade_container = trade.OperationContainer(commissions=discounts)

    def test_container_exists(self):
        self.assertTrue(self.trade_container)

    def test_raw_discounts(self):
        expected_discounts = {
            'some discount': 1,
            'other discount': 3,
        }
        self.assertEqual(self.trade_container.commissions, expected_discounts)

    def test_total_discount_value(self):
        self.assertEqual(self.trade_container.total_commission_value, 4)


class TestContainerPropertiesCase02(unittest.TestCase):
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

    def test_container_exists(self):
        self.assertTrue(self.trade_container)

    def test_operations(self):
        self.assertEqual(len(self.trade_container.operations), 1)

    def test_volume(self):
        self.assertEqual(self.trade_container.volume, 20)


class TestContainerPropertiesCase03(unittest.TestCase):
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

    def test_container_exists(self):
        self.assertTrue(self.trade_container)

    def test_operations(self):
        self.assertEqual(len(self.trade_container.operations), 2)

    def test_volume(self):
        self.assertEqual(self.trade_container.volume, 25)


class TestContainerPropertiesCase04(unittest.TestCase):
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

    def test_container_exists(self):
        self.assertTrue(self.trade_container)

    def test_operations(self):
        self.assertEqual(len(self.trade_container.operations), 2)

    def test_volume(self):
        self.assertEqual(self.trade_container.volume, 25)


class TestContainerPropertiesCase05(unittest.TestCase):
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

    def test_container_exists(self):
        self.assertTrue(self.trade_container)

    def test_operations(self):
        self.assertEqual(len(self.trade_container.operations), 3)

    def test_volume(self):
        self.assertEqual(self.trade_container.volume, 125)
