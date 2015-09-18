from __future__ import absolute_import
import unittest

from trade_tools import trade_tools


class TestAssetCreation(unittest.TestCase):

    def setUp(self):
        self.asset = trade_tools.Asset(name='some stock')

    def test_asset_exists(self):
        self.assertTrue(self.asset)

    def test_asset_name_should_be_some_stock(self):
        self.assertEqual(self.asset.name, 'some stock')
