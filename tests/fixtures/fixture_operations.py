"""A set of operations for the accumualtor tests."""

from __future__ import absolute_import
import copy

from trade import Asset, Operation
from trade.plugins import Daytrade

ASSET = Asset(symbol='some asset')
ASSET2 = Asset(symbol='some other asset')
ASSET3 = Asset(symbol='even other asset')


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


# 2015-09-21
OPERATION24 = Operation(
    date='2015-09-21',
    asset=ASSET,
    quantity=10,
    price=2
)
OPERATION25 = Operation(
    date='2015-09-21',
    asset=ASSET,
    quantity=-10,
    price=3
)
OPERATION26 = Operation(
    date='2015-09-21',
    asset=ASSET,
    quantity=-5,
    price=3
)
OPERATION27 = Operation(
    date='2015-09-21',
    asset=ASSET2,
    quantity=-5,
    price=7
)
OPERATION28 = Operation(
    date='2015-09-21',
    asset=ASSET2,
    quantity=5,
    price=10
)
OPERATION29 = Operation(
    date='2015-09-21',
    asset=ASSET,
    quantity=-5,
    price=10
)
OPERATION30 = Operation(
    date='2015-09-21',
    asset=ASSET,
    quantity=-5,
    price=20
)
OPERATION32 = Operation(
    date='2015-09-21',
    asset=ASSET,
    quantity=5,
    price=4
)
OPERATION34 = Operation(
    date='2015-09-21',
    asset=ASSET3,
    quantity=5,
    price=4
)
OPERATION35 = Operation(
    date='2015-09-21',
    asset=ASSET3,
    quantity=-5,
    price=2
)
OPERATION37 = Operation(
    date='2015-09-21',
    asset=ASSET3,
    quantity=-5,
    price=4
)
OPERATION38 = Operation(
    date='2015-09-21',
    asset=ASSET,
    quantity=5,
    price=4
)
OPERATION39 = Operation(
    date='2015-09-21',
    asset=ASSET,
    quantity=-10,
    price=2
)
OPERATION40 = Operation(
    date='2015-09-21',
    asset=ASSET,
    quantity=5,
    price=1
)
OPERATION41 = Operation(
    date='2015-09-21',
    asset=ASSET2,
    quantity=20,
    price=5
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
