"""Tests for the Portfolio class."""

from __future__ import absolute_import
import unittest

import trade


class TestPortfolioCase00(unittest.TestCase):
    """Test the Subject class and its default behavior."""

    def setUp(self):
        self.subject = trade.Subject()
        self.portfolio = trade.Portfolio()
        occurrence = trade.Occurrence(self.subject, '2015-01-01')
        self.portfolio.accumulate(occurrence)

    def test_assets_dict(self):
        self.assertTrue(self.portfolio.subjects)

    def test_accumulator_exists(self):
        self.assertTrue(
            isinstance(
                self.portfolio.subjects[self.subject.symbol], trade.Accumulator
            )
        )
