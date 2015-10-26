"""Tests the method accumulate() of the Accumulator."""

from __future__ import absolute_import
import copy

import trade
from trade.plugins import prorate_commissions
from tests.fixtures.operations import (
    ASSET, OPERATION19, OPERATION20, OPERATION21, OPERATION22,
    OPERATION23, OPERATION28
)
from tests.fixtures.commissions import (
    COMMISSIONS13
)
from tests.fixtures.logs import (
    LogTest, EXPECTED_STATE1, EXPECTED_STATE16,
    EXPECTED_STATE17, EXPECTED_STATE7, EXPECTED_STATE26
)


class TestAccumulateOperationCase00(LogTest):
    """Attempt to accumulate a Operation with a different asset.

    The Accumulator should only accumulate operations from assets
    with the same code from self.asset.
    """

    occurrences = [OPERATION28]
    expected_state = EXPECTED_STATE1


class TestAccumulateOperationCase01(LogTest):
    """Test the accumulation of 1 operation with commissions."""

    expected_state = EXPECTED_STATE26

    def setUp(self):
        container = trade.OperationContainer(
            operations=[copy.deepcopy(OPERATION19)],
        )
        container.commissions = COMMISSIONS13
        container.fetch_positions()
        prorate_commissions(container)
        self.occurrences = [
            container.positions['operations'][ASSET.symbol]
        ]
        super(TestAccumulateOperationCase01, self).setUp()


class TestAccumulateOperationCase02(LogTest):
    """Test the accumulation of 1 operation with zero price."""

    expected_state = EXPECTED_STATE16

    def setUp(self):
        container = trade.OperationContainer(
            operations=[copy.deepcopy(OPERATION20)]
        )
        container.fetch_positions()
        self.occurrences = [
            container.positions['operations'][ASSET.symbol]
        ]
        super(TestAccumulateOperationCase02, self).setUp()


class TestAccumulateOperationCase03(LogTest):
    """Test the accumulation of 2 operations in consecutive dates."""

    expected_state = EXPECTED_STATE17

    def setUp(self):
        container = trade.OperationContainer(
            operations=[copy.deepcopy(OPERATION19)]
        )
        container.fetch_positions()
        self.occurrences = [
            container.positions['operations'][ASSET.symbol],
            copy.deepcopy(OPERATION21)
        ]
        super(TestAccumulateOperationCase03, self).setUp()


class TestAccumulateOperationCase04(LogTest):
    """Test the accumulation of empty operations."""

    expected_state = EXPECTED_STATE7

    def setUp(self):
        operation2 = copy.deepcopy(OPERATION23)
        operation2.raw_results = {
            'trades': 1000
        }
        self.occurrences = [OPERATION22, operation2]
        super(TestAccumulateOperationCase04, self).setUp()
