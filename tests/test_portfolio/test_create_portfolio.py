from __future__ import absolute_import
import unittest

import trade


class TestCreatePortfolio(unittest.TestCase):

    def setUp(self):
        self.portfolio = trade.Portfolio()

    def test_portfolio_should_exist(self):
        self.assertTrue(self.portfolio)
