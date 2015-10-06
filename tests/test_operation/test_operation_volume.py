"""Tests the volume property of Operation objects."""

from __future__ import absolute_import
from __future__ import division
import unittest

import trade

OPERATION0 = trade.Operation(
    price=10,
    quantity=20
)
OPERATION1 = trade.Operation(
    price=10,
    quantity=-20
)


class TestOperationVolumeCase00(unittest.TestCase):
    """Test the volume property of Operation objects.

    The volume of the operation is its absolute quantity * its price.
    """

    def test_purchase(self):
        self.assertEqual(OPERATION0.volume, 200)

    def test_sale(self):
        self.assertEqual(OPERATION1.volume, 200)

    def test_sale_with_discounts(self):
        OPERATION1.commissions = {
            'brokerage': 2,
            'some tax': 1.5,
            'other tax': 1,
        },
        OPERATION1.fees = {
            'some tax': 0.005,
            'some other tax': 0.0275
        }
        self.assertEqual(OPERATION1.volume, 200)
