"""Test the creation of Option objects."""

from __future__ import absolute_import
import unittest

import trade


class TestOptionCreation(unittest.TestCase):
    """Base class for the option creation tests."""

    def setUp(self):
        self.asset = trade.Asset(symbol='GOOGL')


class TestOptionCretionCase00(TestOptionCreation):
    """Test the creation of an option."""

    def test_no_underlying_assets(self):
        option = trade.plugins.Option(
            symbol='OPTIOSYMBOL', expiration_date='2015-12-21'
        )
        self.assertEqual(option.underlying_assets, {})
