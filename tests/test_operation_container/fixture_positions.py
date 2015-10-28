"""Expected operation container states for the tests."""

import copy

from tests.fixtures.assets import (
    ASSET, ASSET2,
)


POSITION0 = {
    ASSET.symbol: {
        'quantity': 5,
        'price': 2,
        'volume': 10,
        'commissions': {
        }
    }
}

POSITION1 = copy.deepcopy(POSITION0)
POSITION1[ASSET2.symbol] = {
    'quantity': -5,
    'price': 7,
    'volume': 35,
    'commissions': {}
}

POSITION4 = copy.deepcopy(POSITION1)
POSITION4[ASSET.symbol]['commissions'] = {
    'other discount': 0.42857142857142855,
    'some discount': 0.14285714285714285
}
POSITION4[ASSET2.symbol]['commissions'] = {
    'other discount': 1.5,
    'some discount': 0.5
}

POSITION2 = {
    ASSET.symbol: {
        'quantity': 10,
        'price': 3,
        'volume': 30,
        'commissions': {}
    }
}

DT_POSITION0 = {
    'quantity': 5,
    'buy quantity': 5,
    'buy price': 2,
    'sale quantity': -5,
    'sale price': 3,
    'result': {'daytrades': 5},
    'buy commissions': {},
    'sale commissions': {}
}
DT_POSITION6 = copy.deepcopy(DT_POSITION0)
DT_POSITION6['buy commissions'] = {
    'some discount': 0.14285714285714285,
    'other discount': 0.42857142857142855
}
DT_POSITION6['sale commissions'] = {
    'some discount': 0.21428571428571427,
    'other discount': 0.6428571428571428
}
DT_POSITION6['result'] = {'daytrades': 3.571428571428573}

DT_POSITION1 = {
    'quantity': 5,
    'buy quantity': 5,
    'buy price': 10,
    'sale quantity': -5,
    'sale price': 7,
    'result': {'daytrades': -15},
    'buy commissions': {},
    'sale commissions': {}
}
DT_POSITION2 = {
    'quantity': 10,
    'buy quantity':10,
    'buy price': 4,
    'sale quantity': -10,
    'sale price': 3,
    'result': {'daytrades': -10},
    'buy commissions': {},
    'sale commissions': {}
}
DT_POSITION4 = {
    'quantity': 10,
    'buy quantity': 10,
    'buy price': 2,
    'sale quantity': -10,
    'sale price': 3,
    'result': {'daytrades': 10},
    'buy commissions': {},
    'sale commissions': {}
}
DT_POSITION5 = {
    'quantity': 10,
    'buy quantity': 10,
    'buy price': 2,
    'sale quantity': -10,
    'sale price': 15,
    'result': {'daytrades': 130},
    'buy commissions': {},
    'sale commissions': {}
}
