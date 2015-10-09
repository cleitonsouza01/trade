"""Tests for Asset and Derivative."""

from __future__ import absolute_import
import unittest

import trade


class TestAssetCreationCase00(unittest.TestCase):
    """Test the creation of Asset objects.

    - Test the creation of an Asset object with a name.
    - Test the creation of an Asset object without any argument.
    - Test the creation of an Asset object with a name and a symbol.
    - Test the creation of an Asset object with a name, a symbol and
      a expiration date.
    """

    def setUp(self):
        self.asset1 = trade.Asset(
            name='some stock'
        )
        self.asset2 = trade.Asset()
        self.asset3 = trade.Asset(
            name='other stock',
            symbol='AAAA'
        )
        self.asset4 = trade.Asset(
            name='some stuff',
            symbol='STFF',
            expiration_date='2015-12-31'
        )

    def test_asset1_should_exist(self):
        self.assertTrue(self.asset1)

    def test_asset1_name(self):
        self.assertEqual(self.asset1.name, 'some stock')

    def test_asset1_symbol(self):
        self.assertEqual(self.asset1.symbol, None)

    def test_asset1_expiration_date(self):
        self.assertEqual(self.asset1.expiration_date, None)

    def test_asset2_exists(self):
        self.assertTrue(self.asset2)

    def test_asset2_name(self):
        self.assertEqual(self.asset2.name, None)

    def test_asset2_symbol(self):
        self.assertEqual(self.asset2.symbol, None)

    def test_asset2_expiration_date(self):
        self.assertEqual(self.asset2.expiration_date, None)

    def test_asset3_name(self):
        self.assertEqual(self.asset3.name, 'other stock')

    def test_asset3_symbol(self):
        self.assertEqual(self.asset3.symbol, 'AAAA')

    def test_asset3_expiration_date(self):
        self.assertEqual(self.asset3.expiration_date, None)

    def test_asset4_name(self):
        self.assertEqual(self.asset4.name, 'some stuff')

    def test_asset4_symbol(self):
        self.assertEqual(self.asset4.symbol, 'STFF')

    def test_asset4_expiration_date(self):
        self.assertEqual(self.asset4.expiration_date, '2015-12-31')


class TestDerivativeCreationCase00(unittest.TestCase):
    """Test the creation of Derivatives."""

    def setUp(self):
        self.asset1 = trade.Asset(
            symbol='STCK'
        )
        self.asset5 = trade.plugins.Option(
            symbol='ATVI000',
            name='some stuff',
            expiration_date='2015-12-31',
            underlying_assets={self.asset1: 1}
        )
        self.asset6 = trade.plugins.Option(
            symbol='STFF',
            name='some stuff',
            expiration_date='2015-12-31',
            underlying_assets={self.asset1: 2},
        )

    def test_asset5_symbol(self):
        self.assertEqual(self.asset5.symbol, 'ATVI000')

    def test_asset5_expiration_date(self):
        self.assertEqual(self.asset5.expiration_date, '2015-12-31')

    def test_asset5_underlying_assets(self):
        self.assertTrue(self.asset1 in self.asset5.underlying_assets)

    def test_asset5_ratio(self):
        self.assertEqual(self.asset5.underlying_assets[self.asset1], 1)

    def test_asset6_symbol(self):
        self.assertEqual(self.asset6.symbol, 'STFF')

    def test_asset6_expiration_date(self):
        self.assertEqual(self.asset6.expiration_date, '2015-12-31')

    def test_asset6_ratio(self):
        self.assertEqual(self.asset6.underlying_assets[self.asset1], 2)
