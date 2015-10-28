"""A set of operations for the accumualtor tests."""

from __future__ import absolute_import
import copy

from trade import Operation
from trade.plugins import Daytrade, Exercise
from .assets import ASSET, ASSET2, ASSET3, OPTION1


OPERATION77 = Operation(
    quantity=200,
    price=10,
    date='2015-01-01',
    subject=ASSET
)


# 2015-01-01
OPERATION54 = Operation(
    quantity=100,
    price=5,
    subject=ASSET,
    date='2015-01-01'
)
OPERATION55 = Operation(
    quantity=-20,
    price=10,
    subject=ASSET,
    date='2015-01-01'
)
OPERATION0 = Operation(
    quantity=-100,
    price=10,
    date='2015-01-01',
    subject=ASSET
)
OPERATION7 = Operation(
    quantity=-100,
    price=20,
    date='2015-01-01',
    subject=ASSET
)
OPERATION8 = Operation(
    quantity=-50,
    price=20,
    date='2015-01-01',
    subject=ASSET
)
OPERATION16 = Operation(
    quantity=50,
    price=10,
    date='2015-01-01',
    subject=ASSET
)
OPERATION9 = Operation(
    quantity=100,
    price=10,
    date='2015-01-01',
    subject=ASSET
)
OPERATION18 = Operation(
    quantity=100,
    price=10,
    subject=ASSET,
    date='2015-01-01'
)

#2015-01-02
OPERATION1 = Operation(
    quantity=100,
    price=10,
    date='2015-01-02',
    subject=ASSET
)
OPERATION10 = Operation(
    quantity=-100,
    price=10,
    date='2015-01-02',
    subject=ASSET
)
OPERATION17 = Operation(
    quantity=-100,
    price=20,
    date='2015-01-02',
    subject=ASSET
)

#2015-01-03
OPERATION2 = Operation(
    quantity=-100,
    price=10,
    date='2015-01-03',
    subject=ASSET
)
OPERATION11 = Operation(
    quantity=100,
    price=10,
    date='2015-01-03',
    subject=ASSET
)

#2015-01-04
OPERATION3 = Operation(
    quantity=100,
    price=20,
    date='2015-01-04',
    subject=ASSET
)
OPERATION12 = Operation(
    quantity=-100,
    price=20,
    date='2015-01-04',
    subject=ASSET
)

#2015-01-05
OPERATION4 = Operation(
    quantity=-100,
    price=20,
    date='2015-01-05',
    subject=ASSET
)
OPERATION13 = Operation(
    quantity=100,
    price=20,
    date='2015-01-05',
    subject=ASSET
)

#2015-01-06
OPERATION5 = Operation(
    quantity=100,
    price=40,
    date='2015-01-06',
    subject=ASSET
)
OPERATION6 = Operation(
    quantity=50,
    price=40,
    date='2015-01-06',
    subject=ASSET
)
OPERATION14 = Operation(
    quantity=-100,
    price=40,
    date='2015-01-06',
    subject=ASSET
)
OPERATION15 = Operation(
    quantity=-50,
    price=40,
    date='2015-01-06',
    subject=ASSET
)

# 2015-09-18
OPERATION19 = Operation(
    date='2015-09-18',
    subject=ASSET,
    quantity=20,
    price=10
)
OPERATION20 = Operation(
    date='2015-09-18',
    subject=ASSET,
    quantity=20,
    price=0
)
OPERATION22 = Operation(
    date='2015-09-18',
    subject=ASSET,
    quantity=0,
    price=0
)
OPERATION56 = Operation(
    date='2015-09-18',
    subject=ASSET,
    quantity=10,
    price=10,
)

# 2015-09-19
OPERATION21 = Operation(
    date='2015-09-19',
    subject=ASSET,
    quantity=-20,
    price=0
)
OPERATION23 = Operation(
    date='2015-09-19',
    subject=ASSET,
    quantity=0,
    price=0,
)


# 2015-09-21
OPERATION60 = Operation(
    date='2015-09-21',
    subject=ASSET,
    quantity=10,
    price=3
)
OPERATION24 = Operation(
    date='2015-09-21',
    subject=ASSET,
    quantity=10,
    price=2
)
OPERATION25 = Operation(
    date='2015-09-21',
    subject=ASSET,
    quantity=-10,
    price=3
)
OPERATION26 = Operation(
    date='2015-09-21',
    subject=ASSET,
    quantity=-5,
    price=3
)
OPERATION27 = Operation(
    date='2015-09-21',
    subject=ASSET2,
    quantity=-5,
    price=7
)
OPERATION28 = Operation(
    date='2015-09-21',
    subject=ASSET2,
    quantity=5,
    price=10
)
OPERATION29 = Operation(
    date='2015-09-21',
    subject=ASSET,
    quantity=-5,
    price=10
)
OPERATION30 = Operation(
    date='2015-09-21',
    subject=ASSET,
    quantity=-5,
    price=20
)
OPERATION32 = Operation(
    date='2015-09-21',
    subject=ASSET,
    quantity=5,
    price=4
)
OPERATION34 = Operation(
    date='2015-09-21',
    subject=ASSET3,
    quantity=5,
    price=4
)
OPERATION62 = Operation(
    date='2015-09-21',
    subject=ASSET3,
    quantity=5,
    price=4
)
OPERATION35 = Operation(
    date='2015-09-21',
    subject=ASSET3,
    quantity=-5,
    price=2
)
OPERATION37 = Operation(
    date='2015-09-21',
    subject=ASSET3,
    quantity=-5,
    price=4
)
OPERATION38 = Operation(
    date='2015-09-21',
    subject=ASSET,
    quantity=5,
    price=4
)
OPERATION39 = Operation(
    date='2015-09-21',
    subject=ASSET,
    quantity=-10,
    price=2
)
OPERATION40 = Operation(
    date='2015-09-21',
    subject=ASSET,
    quantity=5,
    price=1
)
OPERATION41 = Operation(
    date='2015-09-21',
    subject=ASSET2,
    quantity=20,
    price=5
)
OPERATION42 = Operation(
    date='2015-09-21',
    subject=ASSET2,
    quantity=-10,
    price=2
)
OPERATION43 = Operation(
    date='2015-09-21',
    subject=ASSET2,
    quantity=-20,
    price=2
)
OPERATION44 = Operation(
    date='2015-09-21',
    subject=ASSET3,
    quantity=-20,
    price=2
)
OPERATION45 = Operation(
    date='2015-09-21',
    subject=ASSET,
    quantity=10,
    price=4
)


OPERATION59 = Operation(
    quantity=0,
    price=5,
    date='2015-09-22',
    subject=ASSET2
)

# 2015-10-01
OPERATION58 = Operation(
    quantity=-5,
    price=0,
    date='2015-10-01',
    subject=ASSET
)
OPERATION57 = Operation(
    quantity=0,
    price=5,
    date='2015-10-01',
    subject=ASSET
)
OPERATION56 = Operation(
    quantity=0,
    price=0,
    date='2015-10-01',
    subject=ASSET
)
OPERATION55 = Operation(
    quantity=-10,
    price=5,
    date='2015-10-01',
    subject=ASSET
)
OPERATION46 = Operation(
    subject=ASSET,
    date='2015-10-01',
    quantity=10,
    price=5
)
OPERATION47 = Operation(
    subject=ASSET,
    date='2015-10-05',
    quantity=10,
    price=7.5
)

OPERATION48 = Operation(
    subject=ASSET,
    date='2015-10-01',
    quantity=10,
    price=1
)
OPERATION49 = Operation(
    subject=ASSET2,
    date='2015-10-01',
    quantity=20,
    price=2
)
OPERATION50 = Operation(
    subject=ASSET2,
    date='2015-10-01',
    quantity=20,
    price=4
)
OPERATION51 = Operation(
    subject=ASSET2,
    date='2015-10-02',
    quantity=20,
    price=3
)
OPERATION52 = Operation(
    subject=ASSET,
    date='2015-10-06',
    quantity=10,
    price=2
)
OPERATION53 = Operation(
    subject=ASSET3,
    date='2015-10-01',
    quantity=20,
    price=2
)


OPTION_OPERATION1 = Operation(
    subject=OPTION1,
    date='2015-10-02',
    quantity=10,
    price=1
)
OPTION_OPERATION2 = Operation(
    subject=OPTION1,
    date='2015-10-04',
    quantity=20,
    price=1
)
OPTION_OPERATION3 = Operation(
    quantity=100,
    price=10,
    subject=OPTION1,
    date='2015-01-01'
)

EXERCISE_OPERATION1 = Exercise(
    subject=OPTION1,
    date='2015-10-04',
    quantity=10,
    price=10
)
EXERCISE_OPERATION2 = Exercise(
    date='2015-09-18',
    subject=OPTION1,
    quantity=100,
    price=1
)
EXERCISE_OPERATION3 = Exercise(
    date='2015-09-18',
    subject=OPTION1,
    quantity=100,
    price=3
)
EXERCISE_OPERATION4 = Exercise(
    subject=OPTION1,
    date='2015-10-02',
    quantity=10,
    price=5
)
EXERCISE_OPERATION5 = Exercise(
    quantity=100,
    price=10,
    subject=OPTION1,
    date='2015-01-01'
)
EXERCISE_OPERATION6 = Exercise(
    date='2015-09-18',
    subject=OPTION1,
    quantity=-100,
    price=10
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
