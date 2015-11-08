"""Base class for the JSON tests."""

from __future__ import absolute_import
import unittest
import json

import trade


class TestJSON(unittest.TestCase):
    """Base class for the JSON tests."""

    json_input = None
    json_output = None

    def setUp(self):
        self.interface = trade.trade_json.TradeJSON()

    def test_json_interface(self):
        """Test the json response."""
        if self.json_input:
            self.assertEqual(
                json.loads(self.interface.get_trade_results(self.json_input)),
                json.loads(self.json_output)
            )
