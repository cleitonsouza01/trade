"""Tests the volume property of Operation objects."""

from __future__ import absolute_import
from __future__ import division
import unittest

import trade


class Test_operation_volume_case_00(unittest.TestCase):
    """Test the volume property of Operation objects.

    The volume of the operation is its absolute quantity * its price.
    """

    def test_volume_should_be_100(self):
        operation = trade.Operation(
            price=10,
            quantity=10
        )
        self.assertEqual(operation.volume, 100)

    def test_purchase_volume_should_be_200(self):
        operation = trade.Operation(
            price=10,
            quantity=20
        )
        self.assertEqual(operation.volume, 200)

    def test_sale_volume_should_be_200(self):
        operation = trade.Operation(
            price=10,
            quantity=-20
        )
        self.assertEqual(operation.volume, 200)

    def test_sale_volume_should_be_200_with_commissions_and_taxes(self):
        operation = trade.Operation(
            price=10,
            quantity=-20,
            commissions={
                'brokerage': 2,
                'some tax': 1.5,
                'other tax': 1,
            },
            fees={
                'some tax': 0.005,
                'some other tax': 0.0275
            }
        )
        self.assertEqual(operation.volume, 200)
