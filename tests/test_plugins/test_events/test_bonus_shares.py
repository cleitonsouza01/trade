"""Tests for BonusShares events."""

from __future__ import absolute_import

from tests.fixtures.events import EVENT6, EVENT7, EVENT8
from tests.fixtures.logs import (
    LogTest, INITIAL_STATE0
)


class TestBonusSharesCase00(LogTest):
    """Test a bonus shares event with factor 1."""

    initial_state = INITIAL_STATE0
    occurrences = [EVENT6]
    expected_quantity = 200
    expected_price = 5
    expected_results = {'trades': 1200}


class TestBonusSharesCase01(LogTest):
    """Test a bonus shares event with factor 2."""

    initial_state = INITIAL_STATE0
    occurrences = [EVENT8]
    expected_quantity = 300
    expected_price = 3.33
    expected_results = {'trades': 1200}


class TestBonusSharesCase02(LogTest):
    """Test a bonus shares event with factor 0.5."""

    initial_state = INITIAL_STATE0
    occurrences = [EVENT7]
    expected_quantity = 150
    expected_price = 6.67
    expected_results = {'trades': 1200}
