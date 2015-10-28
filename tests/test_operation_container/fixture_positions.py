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
