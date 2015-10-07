"""Tests the creation of Portfolio objects."""

from __future__ import absolute_import
import unittest

import trade


class TestCreatePortfolio(unittest.TestCase):
    """Test the creation of a Portfolio object."""

    def setUp(self):
        self.portfolio = trade.Portfolio()

    def test_portfolio_exists(self):
        self.assertTrue(self.portfolio)
