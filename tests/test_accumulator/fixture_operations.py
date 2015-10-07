"""A set of operations for the accumualtor tests."""

from __future__ import absolute_import

from trade import Asset, Operation

ASSET = Asset(symbol='some asset')
OPERATION0 = Operation(
    quantity=-100,
    price=10,
    date='2015-01-01',
    asset=ASSET
)
OPERATION1 = Operation(
    quantity=100,
    price=10,
    date='2015-01-02',
    asset=ASSET
)
OPERATION2 = Operation(
    quantity=-100,
    price=10,
    date='2015-01-03',
    asset=ASSET
)
OPERATION3 = Operation(
    quantity=100,
    price=20,
    date='2015-01-04',
    asset=ASSET
)
OPERATION4 = Operation(
    quantity=-100,
    price=20,
    date='2015-01-05',
    asset=ASSET
)
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

OPERATION9 = Operation(
    quantity=100,
    price=10,
    date='2015-01-01',
    asset=ASSET
)
OPERATION10 = Operation(
    quantity=-100,
    price=10,
    date='2015-01-02',
    asset=ASSET
)
OPERATION11 = Operation(
    quantity=100,
    price=10,
    date='2015-01-03',
    asset=ASSET
)
OPERATION12 = Operation(
    quantity=-100,
    price=20,
    date='2015-01-04',
    asset=ASSET
)
OPERATION13 = Operation(
    quantity=100,
    price=20,
    date='2015-01-05',
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
OPERATION16 = Operation(
    quantity=50,
    price=10,
    date='2015-01-01',
    asset=ASSET
)
OPERATION17 = Operation(
    quantity=-100,
    price=20,
    date='2015-01-02',
    asset=ASSET
)


OPERATION18 = Operation(
    quantity=100,
    price=10,
    asset=ASSET,
    date='2015-01-01'
)

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
OPERATION21 = Operation(
    date='2015-09-19',
    asset=ASSET,
    quantity=-20,
    price=0
)


OPERATION22 = Operation(
    date='2015-09-18',
    asset=ASSET,
    quantity=0,
    price=0
)
