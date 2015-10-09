"""Tests the creation of Operation objects."""

from __future__ import absolute_import
from __future__ import division
import unittest
import copy

from tests.fixtures.operations import OPERATION19
from tests.fixtures.commissions import COMMISSIONS0


class TestOperationCreation(unittest.TestCase):
    """Test the creation of Operation objects."""

    def setUp(self):
        self.operation = copy.deepcopy(OPERATION19)
        self.operation.commissions = COMMISSIONS0

    def test_operation_exists(self):
        self.assertTrue(self.operation)

    def test_asset(self):
        self.assertEqual(self.operation.subject.symbol, 'some asset')

    def test_date(self):
        self.assertEqual(self.operation.date, '2015-09-18')

    def test_quantity(self):
        self.assertEqual(self.operation.quantity, 20)

    def test_price(self):
        self.assertEqual(self.operation.price, 10)

    def test_discounts(self):
        self.assertEqual(self.operation.commissions, {'some discount': 3})
