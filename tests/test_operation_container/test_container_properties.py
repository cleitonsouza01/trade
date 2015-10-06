"""Test the properties of the Accumulator."""

from __future__ import absolute_import
import unittest

import trade


ASSET1 = trade.Asset('some asset')
ASSET2 = trade.Asset('some other asset')


class TestContainerProperties(unittest.TestCase):
    """A base class with all operations used in the test cases."""

    def setUp(self):
        self.operation1 = trade.Operation(
            date='2015-09-21',
            asset=ASSET1,
            quantity=-10,
            price=2
        )
        self.operation2 = trade.Operation(
            date='2015-09-21',
            asset=ASSET1,
            quantity=5,
            price=1
        )
        self.operation3 = trade.Operation(
            date='2015-09-21',
            asset=ASSET2,
            quantity=20,
            price=5
        )


class TestContainerPropertiesCase00(TestContainerProperties):
    """Test the total_commission_value property of the Container."""

    def setUp(self):
        super(TestContainerPropertiesCase00, self).setUp()
        discounts = {
            'some discount': 1,
        }
        self.trade_container = trade.OperationContainer(commissions=discounts)

    def test_total_commission_value(self):
        self.assertEqual(self.trade_container.total_commission_value, 1)


class TestContainerPropertiesCase01(TestContainerProperties):
    """Test the total_commission_value property of the Container."""

    def setUp(self):
        super(TestContainerPropertiesCase01, self).setUp()
        discounts = {
            'some discount': 1,
            'other discount': 3,
        }
        self.trade_container = trade.OperationContainer(commissions=discounts)

    def test_total_discount_value(self):
        self.assertEqual(self.trade_container.total_commission_value, 4)


class TestContainerPropertiesCase02(TestContainerProperties):
    """Test the volume property of the Container."""

    def setUp(self):
        super(TestContainerPropertiesCase02, self).setUp()
        self.trade_container = trade.OperationContainer(
            operations=[self.operation1]
        )

    def test_volume(self):
        self.assertEqual(self.trade_container.volume, 20)


class TestContainerPropertiesCase03(TestContainerProperties):
    """Test the volume property of the Container."""

    def setUp(self):
        super(TestContainerPropertiesCase03, self).setUp()
        self.trade_container = trade.OperationContainer(
            operations=[
                self.operation1,
                self.operation2
            ]
        )

    def test_volume(self):
        self.assertEqual(self.trade_container.volume, 25)


class TestContainerPropertiesCase05(TestContainerProperties):
    """Test the volume property of the Container."""

    def setUp(self):
        super(TestContainerPropertiesCase05, self).setUp()
        self.trade_container = trade.OperationContainer(
            operations=[
                self.operation1,
                self.operation2,
                self.operation3
            ]
        )

    def test_volume(self):
        self.assertEqual(self.trade_container.volume, 125)
