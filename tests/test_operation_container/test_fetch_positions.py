"""Tests for the fetch_positions() method of Accumulator."""

from __future__ import absolute_import
import unittest
from abc import ABCMeta, abstractmethod
import copy

import trade

from trade.plugins import prorate_commissions

from tests.fixtures.operations import (
    OPERATION24, OPERATION26, OPERATION27, OPERATION28,
    OPERATION34, OPERATION35, OPERATION37, OPERATION38
)
from tests.fixtures.assets import (
    ASSET, ASSET2, ASSET3,
)
from tests.fixtures.commissions import (
    COMMISSIONS13, COMMISSIONS8
)


class TaxManagerForTests(trade.TradingFees):
    """A TradingFees class for the tests."""

    __metaclass__ = ABCMeta

    @classmethod
    @abstractmethod
    def get_fees(cls, operation=None, operation_type=None):
        """A sample implementation of get_fees()."""
        if operation_type == 'daytrades':
            return {
                'emoluments': 0.005,
                'liquidation': 0.02,
                'registry': 0,
            }
        return {}


class TestFetchPositions(unittest.TestCase):
    """Create the default operations for the test cases."""

    def setUp(self):
        self.container = trade.OperationContainer()
        self.container.tasks = [
            trade.plugins.fetch_exercises,
            trade.plugins.fetch_daytrades,
        ]

class TestContainerFetchPositionsCase00(TestFetchPositions):
    """Test the fetch_positions() method of Accumulator."""

    def setUp(self):
        super(TestContainerFetchPositionsCase00, self).setUp()
        self.container.commissions = COMMISSIONS13
        self.container.operations = [
            copy.deepcopy(OPERATION24),
            copy.deepcopy(OPERATION26),
            copy.deepcopy(OPERATION27)
        ]
        self.container.fetch_positions()
        prorate_commissions(self.container)

    def test_container_volume(self):
        self.assertEqual(self.container.volume, 70)

    def test_daytrade0_buy_discounts(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].commissions['some discount'], 2),
            0.14
        )
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].commissions['other discount'], 2),
            0.43
        )

    def test_daytrade0_sale_discounts(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].commissions['some discount'], 2),
            0.21
        )
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].commissions['other discount'], 2),
            0.64
        )

    def test_operations0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].quantity, 5
        )

    def test_operations0_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].price, 2
        )

    def test_operations0_volume(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].volume, 10
        )

    def test_operations0_discounts(self):
        self.assertEqual(
            round(self.container.positions['operations'][ASSET.symbol]\
                .commissions['some discount'], 2),
            0.14
        )
        self.assertEqual(
            round(self.container.positions['operations'][ASSET.symbol]\
                .commissions['other discount'], 2),
            0.43
        )

    def test_operations1_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol]\
                .quantity, -5
        )

    def test_operations1_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol].price, 7
        )

    def test_operations1_volume(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol].volume, 35
        )

    def test_operations1_discounts(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol]\
                .commissions,
            {
                'some discount': 0.5,
                'other discount': 1.5
            }
        )


class TestContainerFetchPositionsCase01(TestFetchPositions):
    """Test the fetch_positions() method of Accumulator."""

    def setUp(self):
        super(TestContainerFetchPositionsCase01, self).setUp()
        self.container.operations = [
            copy.deepcopy(OPERATION24),
            copy.deepcopy(OPERATION26),
            copy.deepcopy(OPERATION27),
            copy.deepcopy(OPERATION28),
            copy.deepcopy(OPERATION38),
            copy.deepcopy(OPERATION34),
            copy.deepcopy(OPERATION35),
            copy.deepcopy(OPERATION34),
            copy.deepcopy(OPERATION37)
        ]
        self.container.fetch_positions()

    def test_operations_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)

    def test_operations0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol]\
                .quantity, 10
        )

    def test_operations0_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET.symbol].price, 3
        )

    def test_daytrades_len_should_be_3(self):
        self.assertEqual(
            len(self.container.positions['daytrades'].keys()), 3
        )

    def test_daytrade0_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].quantity, 5
        )

    def test_daytrade0_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].price, 2
        )

    def test_daytrade0_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].quantity, 5
        )

    def test_daytrade0_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].price, 3
        )

    def test_daytrade0_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].quantity, -5
        )

    def test_daytrade0_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].results,
            {'daytrades': 5}
        )

    def test_daytrade1_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol].quantity, 5
        )

    def test_daytrade1_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].price, 10
        )

    def test_daytrade1_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].quantity, 5
        )

    def test_daytrade1_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].price, 7
        )

    def test_daytrade1_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].quantity, -5
        )

    def test_daytrade1_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .results,
            {'daytrades': -15}
        )

    def test_daytrade2_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET3.symbol].quantity, 10
        )

    def test_daytrade2_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET3.symbol].\
                operations[0].price, 4
        )

    def test_daytrade2_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET3.symbol].\
                operations[0].quantity, 10
        )

    def test_daytrade2_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET3.symbol].\
                operations[1].price, 3
        )

    def test_daytrade2_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET3.symbol].\
                operations[1].quantity, -10
        )


class TestContainerFetchPositionsCase02(unittest.TestCase):
    """Daytrades, commissions and taxes."""

    def setUp(self):
        date = '2015-02-03'
        operations = []
        operations.append(
            trade.Operation(
                date=date, asset=ASSET, quantity=10, price=10
            )
        )
        operations.append(
            trade.Operation(
                date=date, asset=ASSET, quantity=-10, price=10
            )
        )
        self.container = trade.OperationContainer(
            operations=operations,
        )
        self.container.commissions = COMMISSIONS8
        self.container.tasks = [
            trade.plugins.fetch_exercises,
            trade.plugins.fetch_daytrades,
        ]
        self.container.trading_fees = TaxManagerForTests
        self.container.fetch_positions()
        prorate_commissions(self.container)

    def test_daytrade_buy_discounts(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[0].commissions,
            {
                'some': 1,
                'other': 0.75,
                'and other': 0.5,
            }
        )

    def test_daytrade_sale_discounts(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol]\
                .operations[1].commissions,
            {
                'some': 1,
                'other': 0.75,
                'and other': 0.5,
            }
        )

    def test_daytrade_buy_taxes(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].\
                operations[0].fees,
            {
                'emoluments': 0.005,
                'liquidation': 0.02,
                'registry': 0,
            }
        )

    def test_daytrade_sale_taxes(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].\
                operations[1].fees,
            {
                'emoluments': 0.005,
                'liquidation': 0.02,
                'registry': 0,
            }
        )

    def test_daytrade_result(self):
        self.assertEqual(
            round(
                self.container.positions['daytrades'][ASSET.symbol]\
                    .results['daytrades'], 8
            ), -4.55000000
        )

    def test_daytrade_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET.symbol].quantity, 10
        )

    def test_daytrade_buy_real_price(self):
        self.assertEqual(
            round(
                self.container.positions['daytrades'][ASSET.symbol]\
                    .operations[0].real_price, 8
            ), 10.22750000
        )

    def test_daytrade_sale_real_price(self):
        self.assertEqual(
            round(
                self.container.positions['daytrades'][ASSET.symbol]\
                    .operations[1].real_price, 8
            ), 9.77250000
        )

    def test_daytrade_buy_real_value(self):
        self.assertEqual(
            round(
                self.container.positions['daytrades'][ASSET.symbol].\
                    operations[0].real_value, 8
            ), 102.27500000
        )

    def test_daytrade_sale_real_value(self):
        self.assertEqual(
            round(
                self.container.positions['daytrades'][ASSET.symbol]\
                    .operations[1].real_value, 8
            ), -97.72500000
        )
