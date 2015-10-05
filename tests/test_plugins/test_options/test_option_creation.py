"""Test the creation of Option objects."""

from __future__ import absolute_import
import unittest

import trade


class TestOptionCreationCase00(unittest.TestCase):
    """Test the creation of a call.
    """

    def setUp(self):

        self.asset = trade.Asset(symbol='GOOGL')
        self.option = trade.plugins.Option(
            symbol='GOOG151002C00540000',
            expiration_date='2015-10-02',
            underlying_assets=[self.asset]
        )
    def test_option_should_exist(self):
        self.assertTrue(self.option)

    def test_option_name(self):
        self.assertEqual(self.option.symbol, 'GOOG151002C00540000')

    def test_option_expiration_date(self):
        self.assertEqual(self.option.expiration_date, '2015-10-02')

    def test_underlying_assets(self):
        self.assertEqual(self.option.underlying_assets, [self.asset])
