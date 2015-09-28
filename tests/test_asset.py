from __future__ import absolute_import
import unittest

import trade


class TestAssetCreation_Case_00(unittest.TestCase):
    """Test the creation of Asset objects.

    - Test the creation of an Asset object with a name.
    - Test the creation of an Asset object without any argument.
    - Test the creation of an Asset object with a name and a symbol.
    - Test the creation of an Asset object with a name, a symbol and
      a expiration date.
    """

    def setUp(self):
        self.asset1 = trade.Asset(name='some stock')
        self.asset2 = trade.Asset()
        self.asset3 = trade.Asset(name='other stock', symbol='AAAA')
        self.asset4 = trade.Asset(
            name='some stuff',
            symbol='STFF',
            expiration_date='2015-12-31'
        )

    def test_asset1_should_exist(self):
        self.assertTrue(self.asset1)

    def test_asset1_name_should_be_some_stock(self):
        self.assertEqual(self.asset1.name, 'some stock')

    def test_asset1_symbol_should_be_None(self):
        self.assertEqual(self.asset1.symbol, None)

    def test_asset1_expiration_date_should_be_None(self):
        self.assertEqual(self.asset1.expiration_date, None)

    def test_asset2_should_exist(self):
        self.assertTrue(self.asset2)

    def test_asset2_name_should_be_empty_string(self):
        self.assertEqual(self.asset2.name, None)

    def test_asset2_symbol_should_be_None(self):
        self.assertEqual(self.asset2.symbol, None)

    def test_asset2_expiration_date_should_be_None(self):
        self.assertEqual(self.asset2.expiration_date, None)

    def test_asset3_name_should_be_other_stock(self):
        self.assertEqual(self.asset3.name, 'other stock')

    def test_asset3_symbol_should_be_AAAA(self):
        self.assertEqual(self.asset3.symbol, 'AAAA')

    def test_asset3_expiration_date_should_be_None(self):
        self.assertEqual(self.asset3.expiration_date, None)

    def test_asset4_name_should_be_some_stuff(self):
        self.assertEqual(self.asset4.name, 'some stuff')

    def test_asset4_symbol_should_be_STFF(self):
        self.assertEqual(self.asset4.symbol, 'STFF')

    def test_asset4_expiration_date_should_be_other_2105_12_31(self):
        self.assertEqual(self.asset4.expiration_date, '2015-12-31')
