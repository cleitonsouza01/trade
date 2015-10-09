"""Tests for the Subject class."""

from __future__ import absolute_import
import unittest

import trade


class TestSubjectCase00(unittest.TestCase):
    """Test the Subject class and its default behavior."""

    def setUp(self):
        self.subject = trade.Subject()
        self.accumulator = trade.Accumulator(self.subject)
        self.accumulator.data = {'something': 0}

    def test_expire(self):
        self.subject.expire(self.accumulator)
        self.assertEqual(self.accumulator.data, {})

    def test_default_state(self):
        self.assertEqual(self.subject.get_default_state(), {})
