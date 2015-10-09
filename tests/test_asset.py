"""Tests for Asset and Derivative."""

from __future__ import absolute_import
import unittest

from tests.fixtures.assets import ASSET, ASSET2, ASSET3, ASSET4, OPTION1


class TestAssetCreationCase00(unittest.TestCase):
    """Test the creation of Asset objects.

    - Test the creation of an Asset object with a name.
    - Test the creation of an Asset object without any argument.
    - Test the creation of an Asset object with a name and a symbol.
    - Test the creation of an Asset object with a name, a symbol and
      a expiration date.
    """

    def test_asset1_should_exist(self):
        self.assertTrue(ASSET)

    def test_asset1_name(self):
        self.assertEqual(ASSET.name, None)

    def test_asset1_symbol(self):
        self.assertEqual(ASSET.symbol, 'some asset')

    def test_asset1_expiration_date(self):
        self.assertEqual(ASSET.expiration_date, None)

    def test_asset2_exists(self):
        self.assertTrue(ASSET2)

    def test_asset2_name(self):
        self.assertEqual(ASSET2.name, None)

    def test_asset2_symbol(self):
        self.assertEqual(ASSET2.symbol, 'some other asset')

    def test_asset2_expiration_date(self):
        self.assertEqual(ASSET2.expiration_date, None)

    def test_asset3_name(self):
        self.assertEqual(ASSET3.name, None)

    def test_asset3_symbol(self):
        self.assertEqual(ASSET3.symbol, 'even other asset')

    def test_asset3_expiration_date(self):
        self.assertEqual(ASSET3.expiration_date, None)

    def test_asset4_name(self):
        self.assertEqual(ASSET4.name, 'asset that expires')

    def test_asset4_symbol(self):
        self.assertEqual(ASSET4.symbol, 'EXPR')

    def test_asset4_expiration_date(self):
        self.assertEqual(ASSET4.expiration_date, '2015-12-31')


class TestDerivativeCreationCase00(unittest.TestCase):
    """Test the creation of Derivatives."""

    def test_asset5_symbol(self):
        self.assertEqual(OPTION1.symbol, 'some option')

    def test_asset5_expiration_date(self):
        self.assertEqual(OPTION1.expiration_date, '2015-10-02')

    def test_asset5_underlying_assets(self):
        self.assertTrue(ASSET in OPTION1.underlying_assets)

    def test_asset5_ratio(self):
        self.assertEqual(OPTION1.underlying_assets[ASSET], 1)
