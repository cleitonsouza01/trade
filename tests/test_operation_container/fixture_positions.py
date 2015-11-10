"""Expected operation container states for the tests."""

import copy

from tests.fixtures.assets import (
    ASSET, ASSET2, ASSET3
)


POSITION01 = {
    'quantity': -10,
    'price': 2,
    'volume': 20,
    'commissions': {
        'some discount': 1,
    }
}
POSITION02 = copy.deepcopy(POSITION01)
POSITION02['commissions'] = {
    'some discount': 0.5,
}

POSITION03 = {
    'quantity': -20,
    'price': 2,
    'volume': 40,
    'commissions': {
        'some discount': 2,
    }
}

POSITION04 = copy.deepcopy(POSITION01)
POSITION04['commissions'] = {
    'some discount': 0.33333333333333326,
}

POSITION05 = copy.deepcopy(POSITION03)
POSITION05['commissions'] = {
    'some discount': 0.6666666666666665,
}

POSITION06 = {
    'quantity': 5,
    'price': 2,
    'volume': 10,
    'commissions': {
        'other discount': 0.8571428571428571,
        'some discount': 0.2857142857142857
    }
}
POSITION07 = {
    'quantity': -5,
    'price': 7,
    'volume': 35,
    'commissions': {
        'other discount': 3,
        'some discount': 1
    }
}

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


DT_POSITION9 = {
    'quantity': 10,
    'buy quantity': 10,
    'buy price': 10,
    'sale quantity': -10,
    'sale price': 10,
    'result': {'daytrades': -4.549999999999983},
    'buy commissions': {
        'some': 1,
        'other': 0.75,
        'and other': 0.5,
        'emoluments': 0.005,
        'liquidation': 0.02,
        'registry': 0,
    },
    'sale commissions': {
        'some': 1,
        'other': 0.75,
        'and other': 0.5,
        'emoluments': 0.005,
        'liquidation': 0.02,
        'registry': 0,
    }
}

DT_POSITION10 = copy.deepcopy(DT_POSITION0)
DT_POSITION10['results'] = {'daytrades': 2.1428571428571423}
DT_POSITION10['buy commissions'] = {
    'some discount': 0.2857142857142857,
    'other discount': 0.8571428571428571
}
DT_POSITION10['sale commissions'] = {
    'some discount': 0.42857142857142855,
    'other discount': 1.2857142857142856
}


CONTAINER_POSITION0 = {
    ASSET.symbol: POSITION01,
}

CONTAINER_POSITION1 = {
    ASSET.symbol: POSITION02,
    ASSET2.symbol: POSITION02,
}

CONTAINER_POSITION2 = {
    ASSET.symbol: POSITION04,
    ASSET2.symbol: POSITION05,
}

CONTAINER_POSITION3 = {
    ASSET.symbol: POSITION01,
    ASSET2.symbol: POSITION01,
    ASSET3.symbol: POSITION03
}

CONTAINER_POSITION4 = {
    ASSET.symbol: POSITION06,
    ASSET2.symbol: POSITION07
}

CONTAINER_DAYTRADE_POSITION0 = {
    ASSET.symbol: DT_POSITION10
}
