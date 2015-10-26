"""Tests the method accumulate() of the Accumulator."""

from __future__ import absolute_import
from __future__ import division

import trade
import trade.plugins

from tests.fixtures.operations import ASSET
from tests.fixtures.logs import (
    LogTest, INITIAL_STATE0, EXPECTED_STATE14
)


class EventThatChangeResults(trade.plugins.Event):
    """A fictional event for the tests."""

    def update_accumulator(self, accumulator):
        """Increment all results in the container with the factor."""
        for key in accumulator.data['results'].keys():
            accumulator.data['results'][key] += self.factor


class TestEventThatChangeResultsCase00(LogTest):
    """Test the accumulation of an Event object.

    In this test we use the EventThatChangeResults object
    to test the consequences of an Event accumulation.
    """
    initial_state = INITIAL_STATE0
    occurrences = [
        EventThatChangeResults(ASSET, '2015-09-27', 2)
    ]
    expected_state = EXPECTED_STATE14
