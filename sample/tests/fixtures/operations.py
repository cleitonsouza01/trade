"""A set of operations for the accumualtor tests."""

from __future__ import absolute_import

from trade.occurrences import Operation

from trade_app.options import Exercise
from fixtures.assets import OPTION1, ASSET


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

OPERATION54 = Operation(
    quantity=100,
    price=5,
    subject=ASSET,
    date='2015-01-01'
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
