"""Tests for the prorate_commissions() method of Accumulator."""

from __future__ import absolute_import

from .container_test_base import TestFetchPositions
from tests.fixtures.operations import (
    OPERATION39, OPERATION42, OPERATION43, OPERATION44,
)
from tests.fixtures.commissions import (
    COMMISSIONS9, COMMISSIONS10, COMMISSIONS11,
)
from tests.fixtures.assets import (
    ASSET, ASSET2, ASSET3
)
from tests.fixtures.operation_sequences import (
    OPERATION_SEQUENCE2
)


class TestProrateCommissionsByPositionCase01(TestFetchPositions):
    """Test pro rata of one commission for one operation."""

    volume = 20
    commissions = COMMISSIONS11
    operations = [OPERATION39]
    positions = {
        ASSET.symbol: {
            'quantity': -10,
            'price': 2,
            'volume': 20,
            'commissions': {
                'some discount': 1,
            }
        },
    }


class TestProrateCommissionsByPositionCase02(TestFetchPositions):
    """Test pro rata of 1 commission for 3 operations."""

    volume = 40
    commissions = COMMISSIONS11
    operations = [OPERATION39, OPERATION42]
    positions = {
        ASSET.symbol: {
            'quantity': -10,
            'price': 2,
            'volume': 20,
            'commissions': {
                'some discount': 0.5,
            }
        },
        ASSET2.symbol: {
            'quantity': -10,
            'price': 2,
            'volume': 20,
            'commissions': {
                'some discount': 0.5,
            }
        },
    }


class TestProrateCommissionsByPositionCase03(TestFetchPositions):
    """Test pro rata of 1 commission for 2 operations."""

    volume = 60
    commissions = COMMISSIONS11
    operations = [OPERATION39, OPERATION43]
    positions = {
        ASSET.symbol: {
            'quantity': -10,
            'price': 2,
            'volume': 20,
            'commissions': {
                'some discount': 0.33333333333333326,
            }
        },
        ASSET2.symbol: {
            'quantity': -20,
            'price': 2,
            'volume': 40,
            'commissions': {
                'some discount': 0.6666666666666665,
            }
        },
    }


class TestProrateCommissionsByPositionCase04(TestFetchPositions):
    """Test pro rata of 1 commission for 3 sale operations."""

    volume = 80
    commissions = COMMISSIONS10
    operations = [OPERATION39, OPERATION44, OPERATION42]
    positions = {
        ASSET.symbol: {
            'quantity': -10,
            'price': 2,
            'volume': 20,
            'commissions': {
                'some discount': 1,
            }
        },
        ASSET2.symbol: {
            'quantity': -10,
            'price': 2,
            'volume': 20,
            'commissions': {
                'some discount': 1,
            }
        },
        ASSET3.symbol: {
            'quantity': -20,
            'price': 2,
            'volume': 40,
            'commissions': {
                'some discount': 2,
            }
        }
    }


class TestProrateCommissionsByPositionCase05(TestFetchPositions):
    """Test pro rata of 1 commission for daytrades."""

    volume = 70
    commissions = COMMISSIONS9
    operations = OPERATION_SEQUENCE2
    positions = {
        ASSET.symbol: {
            'quantity': 5,
            'price': 2,
            'volume': 10,
            'commissions': {
                'other discount': 0.8571428571428571,
                'some discount': 0.2857142857142857
            }
        },
        ASSET2.symbol: {
            'quantity': -5,
            'price': 7,
            'volume': 35,
            'commissions': {
                'other discount': 3,
                'some discount': 1
            }
        }
    }
    daytrades = {
        ASSET.symbol: {
            'quantity': 5,
            'buy quantity': 5,
            'buy price': 2,
            'sale quantity': -5,
            'sale price': 3,
            'result': {'daytrades': 2.1428571428571423},
            'buy commissions': {
                'some discount': 0.2857142857142857,
                'other discount': 0.8571428571428571
            },
            'sale commissions': {
                'some discount': 0.42857142857142855,
                'other discount': 1.2857142857142856
            }
        }
    }
