from __future__ import absolute_import
import unittest

import trade_tools


# TODO document this


class TestAssetCreation(unittest.TestCase):

    def setUp(self):
        self.asset1 = trade_tools.Asset(name='some stock')
        self.asset2 = trade_tools.Asset()

    def test_asset1_should_exist(self):
        self.assertTrue(self.asset1)

    def test_asset1_name_should_be_some_stock(self):
        self.assertEqual(self.asset1.name, 'some stock')

    def test_asset2_should_exist(self):
        self.assertTrue(self.asset2)

    def test_asset2_name_should_be_empty_string(self):
        self.assertEqual(self.asset2.name, '')
