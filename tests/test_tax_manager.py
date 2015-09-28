from __future__ import absolute_import
import unittest

import trade


class TestTaxManager(unittest.TestCase):
    """Test the default 'dummy' tax manager.

    The default tax manager should return a empty dict
    for both daytrade and common operation taxes.
    """
    def setUp(self):
        self.tax_manager = trade.TaxManager()

    def test_assert_tax_manager_exists(self):
        self.assertTrue(self.tax_manager)

    def test_get_taxes_for_operation_should_return_empty_dict(self):
        operation = trade.Operation(
            asset=trade.Asset(),
            quantity=10,
            price=1,
            date='2015-09-25'
        )
        self.assertEqual(
            self.tax_manager.get_fees_for_operation(operation),
            {}
        )

    def test_get_taxes_for_daytrade_should_return_empty_dict(self):
        daytrade = trade.Daytrade('2015-09-25', trade.Asset(), 100, 10, 20)
        self.assertEqual(
            self.tax_manager.get_fees_for_daytrade(daytrade),
            {}
        )
