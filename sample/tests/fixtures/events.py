"""A set of events for the tests."""

from __future__ import absolute_import

from trade.occurrences import Operation

from trade_app.events import StockSplit, BonusShares
from fixtures.assets import ASSET


class TestEvent(Operation):
    """A dummy event for the tests."""

    def update_accumulator(self, container):
        pass


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

EVENT6 = BonusShares(
    asset=ASSET,
    date='2015-09-24',
    factor=1
)
EVENT7 = BonusShares(
    asset=ASSET,
    date='2015-09-24',
    factor=0.5
)
EVENT8 = BonusShares(
    asset=ASSET,
    date='2015-09-24',
    factor=2
)
EVENT9 = StockSplit(
    asset=ASSET,
    date='2015-09-24',
    factor=0.5
)
