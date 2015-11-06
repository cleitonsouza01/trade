"""Tests for the fetch_positions() method of OperationContainer."""

from __future__ import absolute_import
from abc import ABCMeta

from .container_test_base import TestFetchPositions
from .fixture_positions import (
    DT_POSITION0, DT_POSITION1, DT_POSITION2, POSITION4, POSITION2,
    DT_POSITION6, DT_POSITION9,
)
from .fixture_tasks import find_trading_fees_for_positions

from tests.fixtures.assets import (
    ASSET, ASSET2, ASSET3,
)
from tests.fixtures.commissions import (
    COMMISSIONS13, COMMISSIONS8
)
from tests.fixtures.operation_sequences import (
    OPERATION_SEQUENCE2, OPERATION_SEQUENCE8, OPERATION_SEQUENCE24
)


class TaxManagerForTests(object):
    """A TradingFees class for the tests."""

    __metaclass__ = ABCMeta

    @classmethod
    def get_fees(cls, operation=None, operation_type=None):
        """A sample implementation of get_fees()."""
        if operation_type == 'daytrades':
            return cls.get_fees_for_daytrades(operation)
        return {}

    @classmethod
    def get_fees_for_daytrades(cls, operation):
        """Get the fees for a daytrade operation."""
        return {
            'emoluments': operation.volume * 0.005 / 100,
            'liquidation': operation.volume * 0.02 / 100,
            'registry': 0,
        }

class TestContainerFetchPositionsCase00(TestFetchPositions):
    """Test the fetch_positions() method of Accumulator."""

    commissions = COMMISSIONS13
    operations = OPERATION_SEQUENCE2
    positions = POSITION4
    daytrades = {
        ASSET.symbol: DT_POSITION6
    }


class TestContainerFetchPositionsCase01(TestFetchPositions):
    """Test the fetch_positions() method of Accumulator."""

    operations = OPERATION_SEQUENCE8
    positions = POSITION2
    daytrades = {
        ASSET.symbol: DT_POSITION0,
        ASSET2.symbol: DT_POSITION1,
        ASSET3.symbol: DT_POSITION2
    }


class TestContainerFetchPositionsCase02(TestFetchPositions):
    """Daytrades, commissions and taxes."""

    commissions = COMMISSIONS8
    operations = OPERATION_SEQUENCE24
    daytrades = {
        ASSET.symbol: DT_POSITION9,
    }

    def setUp(self):
        super(TestContainerFetchPositionsCase02, self).setUp()
        self.container.trading_fees = TaxManagerForTests
        find_trading_fees_for_positions(self.container)
