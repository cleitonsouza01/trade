"""Base class for the JSON tests."""

from __future__ import absolute_import
import unittest
import json

from trade.trade_json import TradeJSON
from trade.occurrences import Asset, Operation
from trade.container_tasks import fetch_daytrades, group_positions, find_volume


class TestJSON(unittest.TestCase):
    """Base class for the JSON tests."""

    json_input = None
    json_output = None
    maxDiff = None

    def setUp(self):
        types = {
            'Asset': Asset,
            'Operation': Operation,
        }
        self.interface = TradeJSON(
            [fetch_daytrades, group_positions, find_volume],
            types
        )

    def test_json_interface(self):
        """Test the json response."""
        if self.json_input:
            self.assertEqual(
                json.loads(self.interface.get_trade_results(self.json_input)),
                json.loads(self.json_output)
            )
