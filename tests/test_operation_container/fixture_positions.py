"""Expected operation container states for the tests."""

from tests.fixtures.assets import (
    ASSET, ASSET2,
)

POSITION0 = {
    ASSET.symbol: {
        'quantity': 5,
        'price': 2,
        'volume': 10
    }
}

POSITION1 = {
    ASSET.symbol: {
        'quantity': 5,
        'price': 2,
        'volume': 10
    },
    ASSET2.symbol: {
        'quantity': -5,
        'price': 7,
        'volume': 35
    }
}

POSITION2 = {
    ASSET.symbol: {
        'quantity': 10,
        'price': 3,
        'volume': 30
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
