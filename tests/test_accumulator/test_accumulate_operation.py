"""Tests the method accumulate() of the Accumulator."""

from __future__ import absolute_import
import copy

from trade import trade

from trade.container_tasks import (
    prorate_commissions, group_positions, find_volume
)
from tests.fixtures.logtest import LogTest
from tests.fixtures.operations import (
    ASSET, OPERATION19, OPERATION20, OPERATION21, OPERATION22,
    OPERATION23, OPERATION28
)
from tests.fixtures.commissions import (
    COMMISSIONS13
)
from tests.fixtures.accumulator_states import (
    EXPECTED_STATE1, EXPECTED_STATE16,
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
            tasks=[find_volume, group_positions, prorate_commissions]
        )
        container.commissions = COMMISSIONS13
        container.fetch_positions()
        if 'positions' in container.context:
            self.occurrences = [
                container.context['positions']['operations'][ASSET.symbol]
            ]
        super(TestAccumulateOperationCase01, self).setUp()


class TestAccumulateOperationCase02(LogTest):
    """Test the accumulation of 1 operation with zero price."""

    expected_state = EXPECTED_STATE16

    def setUp(self):
        container = trade.OperationContainer(
            operations=[copy.deepcopy(OPERATION20)],
            tasks=[find_volume, group_positions]
        )
        container.fetch_positions()
        if 'positions' in container.context:
            self.occurrences = [
                container.context['positions']['operations'][ASSET.symbol]
            ]
        super(TestAccumulateOperationCase02, self).setUp()


class TestAccumulateOperationCase03(LogTest):
    """Test the accumulation of 2 operations in consecutive dates."""

    expected_state = EXPECTED_STATE17

    def setUp(self):
        container = trade.OperationContainer(
            operations=[copy.deepcopy(OPERATION19)],
            tasks=[find_volume, group_positions]
        )
        container.fetch_positions()
        if 'positions' in container.context:
            self.occurrences = [
                container.context['positions']['operations'][ASSET.symbol],
                copy.deepcopy(OPERATION21)
            ]
        super(TestAccumulateOperationCase03, self).setUp()


class TestAccumulateOperationCase04(LogTest):
    """Test the accumulation of empty operations."""

    expected_state = EXPECTED_STATE7

    def setUp(self):
        operation2 = copy.deepcopy(OPERATION23)
        operation2.raw_results = {'trades': 1000}
        self.occurrences = [OPERATION22, operation2]
        super(TestAccumulateOperationCase04, self).setUp()
