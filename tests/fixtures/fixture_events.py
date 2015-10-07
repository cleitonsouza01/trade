"""A set of operations for the accumualtor tests."""

from __future__ import absolute_import

from .fixture_operations import ASSET
from trade.plugins import  Event, StockSplit


# EVENTS

class TestEvent(Event):
    """A dummy event for the tests."""

    def update_container(self, container):
        pass


EVENT0 = TestEvent(
    asset=ASSET,
    date='2015-01-01',
    factor=1
)
EVENT1 = TestEvent(
    asset=ASSET,
    date='2015-01-03',
    factor=1
)
EVENT2 = TestEvent(
    asset=ASSET,
    date='2015-01-02',
    factor=1
)

EVENT3 = TestEvent(
    ASSET,
    '2015-09-25',
    factor=1
)
EVENT4 = TestEvent(
    ASSET,
    '2015-09-24',
    factor=1,
)

EVENT5 = StockSplit(
    asset=ASSET,
    date='2015-09-24',
    factor=2
)
