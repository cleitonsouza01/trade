"""Tests for Asset and Derivative."""

from __future__ import absolute_import
import unittest

from trade.occurrences import Asset


class TestAsset(unittest.TestCase):
    """Base class for Asset tests."""

    KINDS = {
        'asset': Asset,
    }

    kind = 'asset'
    symbol = None
    name = None
    expiration_date = None
    underlying_assets = {}

    def setUp(self):
        """Create the asset described in the class attrs"""
        self.asset = self.KINDS[self.kind](
            symbol=self.symbol,
            name=self.name,
            expiration_date=self.expiration_date,
        )
        if self.underlying_assets:
            self.asset.underlying_assets = self.underlying_assets

    def test_asset_should_exist(self):
        """Asset should have been created."""
        self.assertTrue(self.asset)

    def test_name(self):
        """Check the asset name."""
        self.assertEqual(self.asset.name, self.name)

    def test_symbol(self):
        """Check the asset symbol."""
        self.assertEqual(self.asset.symbol, self.symbol)

    def test_expiration_date(self):
        """Check the asset expiration date."""
        self.assertEqual(self.asset.expiration_date, self.expiration_date)

    def test_underlying_assets(self):
        """Check the underlying assets of the asset, if any."""
        if self.underlying_assets:
            self.assertEqual(
                self.underlying_assets,
                self.asset.underlying_assets
            )

    def test_ratio(self):
        """Check the ratio of the underlying assets of the asset."""
        if self.underlying_assets:
            for asset, ratio in self.underlying_assets.items():
                self.assertEqual(
                    self.asset.underlying_assets[asset],
                    ratio
                )


class TestAssetCase00(TestAsset):
    """Teste Asset Case 00 - Asset"""
    symbol = 'GOOG'
    name = None
    expiration_date = None


class TestAssetCase01(TestAsset):
    """Teste Asset Case 01 - Asset"""

    symbol = 'ATVI'
    name = 'Activision Blizzard, Inc'
    expiration_date = None


class TestAssetCase02(TestAsset):
    """Teste Asset Case 02 - Asset"""

    symbol = 'TEST'
    name = 'Some asset that expires'
    expiration_date = '2015-11-10'
