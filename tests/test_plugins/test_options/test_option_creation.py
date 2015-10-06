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
