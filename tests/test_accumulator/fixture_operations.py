"""A set of operations for the accumualtor tests."""

from __future__ import absolute_import
import copy

from trade import Asset, Operation
from trade.plugins import Daytrade, Event, StockSplit

ASSET = Asset(symbol='some asset')


# 2015-01-01
OPERATION0 = Operation(
    quantity=-100,
    price=10,
    date='2015-01-01',
    asset=ASSET
)
OPERATION7 = Operation(
    quantity=-100,
    price=20,
    date='2015-01-01',
    asset=ASSET
)
OPERATION8 = Operation(
    quantity=-50,
    price=20,
    date='2015-01-01',
    asset=ASSET
)
OPERATION16 = Operation(
    quantity=50,
    price=10,
    date='2015-01-01',
    asset=ASSET
)
OPERATION9 = Operation(
    quantity=100,
    price=10,
    date='2015-01-01',
    asset=ASSET
)
OPERATION18 = Operation(
    quantity=100,
    price=10,
    asset=ASSET,
    date='2015-01-01'
)


#2015-01-02
OPERATION1 = Operation(
    quantity=100,
    price=10,
    date='2015-01-02',
    asset=ASSET
)
OPERATION10 = Operation(
    quantity=-100,
    price=10,
    date='2015-01-02',
    asset=ASSET
)
OPERATION17 = Operation(
    quantity=-100,
    price=20,
    date='2015-01-02',
    asset=ASSET
)


#2015-01-03
OPERATION2 = Operation(
    quantity=-100,
    price=10,
    date='2015-01-03',
    asset=ASSET
)
OPERATION11 = Operation(
    quantity=100,
    price=10,
    date='2015-01-03',
    asset=ASSET
)


#2015-01-04
OPERATION3 = Operation(
    quantity=100,
    price=20,
    date='2015-01-04',
    asset=ASSET
)
OPERATION12 = Operation(
    quantity=-100,
    price=20,
    date='2015-01-04',
    asset=ASSET
)


#2015-01-05
OPERATION4 = Operation(
    quantity=-100,
    price=20,
    date='2015-01-05',
    asset=ASSET
)
OPERATION13 = Operation(
    quantity=100,
    price=20,
    date='2015-01-05',
    asset=ASSET
)


#2015-01-06
OPERATION5 = Operation(
    quantity=100,
    price=40,
    date='2015-01-06',
    asset=ASSET
)
OPERATION6 = Operation(
    quantity=50,
    price=40,
    date='2015-01-06',
    asset=ASSET
)
OPERATION14 = Operation(
    quantity=-100,
    price=40,
    date='2015-01-06',
    asset=ASSET
)
OPERATION15 = Operation(
    quantity=-50,
    price=40,
    date='2015-01-06',
    asset=ASSET
)


# 2015-09-18
OPERATION19 = Operation(
    date='2015-09-18',
    asset=ASSET,
    quantity=20,
    price=10
)

OPERATION20 = Operation(
    date='2015-09-18',
    asset=ASSET,
    quantity=20,
    price=0
)
OPERATION22 = Operation(
    date='2015-09-18',
    asset=ASSET,
    quantity=0,
    price=0
)


# 2015-09-19
OPERATION21 = Operation(
    date='2015-09-19',
    asset=ASSET,
    quantity=-20,
    price=0
)
OPERATION23 = Operation(
    date='2015-09-19',
    asset=ASSET,
    quantity=0,
    price=0,
)


# DAYTRADES

DAYTRADE0 = Daytrade(
    copy.deepcopy(OPERATION18),
    copy.deepcopy(OPERATION7)
)
DAYTRADE1 = Daytrade(
    copy.deepcopy(OPERATION1),
    copy.deepcopy(OPERATION17)
)
DAYTRADE2 = Daytrade(
    copy.deepcopy(OPERATION9),
    copy.deepcopy(OPERATION7)
)
DAYTRADE3 = copy.deepcopy(DAYTRADE2)
DAYTRADE3.date = '2015-01-02'


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
