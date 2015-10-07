"""Tests for the fetch_positions() method of Accumulator."""

from __future__ import absolute_import
import unittest
from abc import ABCMeta, abstractmethod

import trade


ASSET1 = trade.Asset(symbol='some asset')
ASSET2 = trade.Asset(symbol='some other asset')
ASSET3 = trade.Asset(symbol='even other asset')


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
        self.operation1 = trade.Operation(
            date='2015-09-21', asset=ASSET1, quantity=10, price=2
        )
        self.operation2 = trade.Operation(
            date='2015-09-21', asset=ASSET1, quantity=-5, price=3
        )
        self.operation3 = trade.Operation(
            date='2015-09-21', asset=ASSET2, quantity=-5, price=7
        )
        self.operation4 = trade.Operation(
            date='2015-09-21', asset=ASSET2, quantity=5, price=10
        )
        self.operation5 = trade.Operation(
            date='2015-09-21', asset=ASSET1, quantity=5, price=4
        )
        self.operation6 = trade.Operation(
            date='2015-09-21', asset=ASSET3, quantity=5, price=4
        )
        self.operation7 = trade.Operation(
            date='2015-09-21', asset=ASSET3, quantity=-5, price=2
        )
        self.operation8 = trade.Operation(
            date='2015-09-21', asset=ASSET3, quantity=5, price=4
        )
        self.operation9 = trade.Operation(
            date='2015-09-21', asset=ASSET3, quantity=-5, price=4
        )
        self.container = trade.OperationContainer()
        self.container.tasks = [
            trade.plugins.fetch_exercises,
            trade.plugins.fetch_daytrades,
        ]

class TestContainerFetchPositionsCase00(TestFetchPositions):
    """Test the fetch_positions() method of Accumulator."""

    def setUp(self):
        super(TestContainerFetchPositionsCase00, self).setUp()
        self.container.commissions = {
            'some discount': 1,
            'other discount': 3
        }
        self.container.operations = [
            self.operation1, self.operation2, self.operation3
        ]
        self.container.fetch_positions()

    def test_container_volume(self):
        self.assertEqual(self.container.volume, 70)

    def test_daytrade0_buy_discounts(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET1.symbol]\
                .operations[0].commissions['some discount'], 2),
            0.14
        )
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET1.symbol]\
                .operations[0].commissions['other discount'], 2),
            0.43
        )

    def test_daytrade0_sale_discounts(self):
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET1.symbol]\
                .operations[1].commissions['some discount'], 2),
            0.21
        )
        self.assertEqual(
            round(self.container.positions['daytrades'][ASSET1.symbol]\
                .operations[1].commissions['other discount'], 2),
            0.64
        )

    def test_operations0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET1.symbol].quantity,
            5
        )

    def test_operations0_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET1.symbol].price,
            2
        )

    def test_operations0_volume(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET1.symbol].volume,
            10
        )

    def test_operations0_discounts(self):
        self.assertEqual(
            round(self.container.positions['operations'][ASSET1.symbol]\
                .commissions['some discount'], 2),
            0.14
        )
        self.assertEqual(
            round(self.container.positions['operations'][ASSET1.symbol]\
                .commissions['other discount'], 2),
            0.43
        )

    def test_operations1_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol]\
                .quantity,
            -5
        )

    def test_operations1_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol].price,
            7
        )

    def test_operations1_volume(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol].volume,
            35
        )

    def test_operations1_discounts(self):
        expected_discounts = {
            'some discount': 0.5,
            'other discount': 1.5
        }
        self.assertEqual(
            self.container.positions['operations'][ASSET2.symbol]\
                .commissions,
            expected_discounts
        )


class TestContainerFetchPositionsCase01(TestFetchPositions):
    """Test the fetch_positions() method of Accumulator."""

    def setUp(self):
        super(TestContainerFetchPositionsCase01, self).setUp()
        self.container.operations = [
            self.operation1,
            self.operation2,
            self.operation3,
            self.operation4,
            self.operation5,
            self.operation6,
            self.operation7,
            self.operation8,
            self.operation9
        ]
        self.container.fetch_positions()

    def test_operations_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)

    def test_operations0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET1.symbol]\
                .quantity,
            10
        )

    def test_operations0_price(self):
        self.assertEqual(
            self.container.positions['operations'][ASSET1.symbol].price,
            3
        )

    def test_daytrades_len_should_be_3(self):
        self.assertEqual(
            len(self.container.positions['daytrades'].keys()),
            3
        )

    def test_daytrade0_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET1.symbol].quantity,
            5
        )

    def test_daytrade0_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET1.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET1.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade0_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET1.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade0_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET1.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade0_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET1.symbol].results,
            {'daytrades': 5}
        )

    def test_daytrade1_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol].quantity,
            5
        )

    def test_daytrade1_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade1_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET2.symbol]\
                .results,
            {'daytrades': -15}
        )

    def test_daytrade2_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET3.symbol].quantity,
            10
        )

    def test_daytrade2_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET3.symbol].\
                operations[0].price,
            4
        )

    def test_daytrade2_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET3.symbol].\
                operations[0].quantity,
            10
        )

    def test_daytrade2_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET3.symbol].\
                operations[1].price,
            3
        )

    def test_daytrade2_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET3.symbol].\
                operations[1].quantity,
            -10
        )


class TestContainerFetchPositionsCase02(unittest.TestCase):
    """Daytrades, commissions and taxes."""

    def setUp(self):
        date = '2015-02-03'
        operations = []
        operations.append(
            trade.Operation(
                date=date, asset=ASSET1, quantity=10, price=10
            )
        )
        operations.append(
            trade.Operation(
                date=date, asset=ASSET1, quantity=-10, price=10
            )
        )
        commissions = {
            'some': 2,
            'other': 1.5,
            'and other': 1,
        }
        self.container = trade.OperationContainer(
            operations=operations, commissions=commissions
        )
        self.container.tasks = [
            trade.plugins.fetch_exercises,
            trade.plugins.fetch_daytrades,
        ]
        self.container.trading_fees = TaxManagerForTests
        self.container.fetch_positions()

    def test_daytrade_buy_discounts(self):
        discounts = {
            'some': 1,
            'other': 0.75,
            'and other': 0.5,
        }
        self.assertEqual(
            self.container.positions['daytrades'][ASSET1.symbol]\
                .operations[0].commissions,
            discounts
        )

    def test_daytrade_sale_discounts(self):
        discounts = {
            'some': 1,
            'other': 0.75,
            'and other': 0.5,
        }
        self.assertEqual(
            self.container.positions['daytrades'][ASSET1.symbol]\
                .operations[1].commissions,
            discounts
        )

    def test_daytrade_buy_taxes(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET1.symbol].\
                operations[0].fees,
            {
                'emoluments': 0.005,
                'liquidation': 0.02,
                'registry': 0,
            }
        )

    def test_daytrade_sale_taxes(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET1.symbol].\
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
                self.container.positions['daytrades'][ASSET1.symbol]\
                    .results['daytrades'],
                8
            ),
            -4.55000000
        )

    def test_daytrade_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][ASSET1.symbol].quantity,
            10
        )

    def test_daytrade_buy_real_price(self):
        self.assertEqual(
            round(
                self.container.positions['daytrades'][ASSET1.symbol]\
                    .operations[0].real_price,
                8
            ),
            10.22750000
        )

    def test_daytrade_sale_real_price(self):
        self.assertEqual(
            round(
                self.container.positions['daytrades'][ASSET1.symbol]\
                    .operations[1].real_price,
                8
            ),
            9.77250000
        )

    def test_daytrade_buy_real_value(self):
        self.assertEqual(
            round(
                self.container.positions['daytrades'][ASSET1.symbol].\
                    operations[0].real_value,
                8
            ),
            102.27500000
        )

    def test_daytrade_sale_real_value(self):
        self.assertEqual(
            round(
                self.container.positions['daytrades'][ASSET1.symbol]\
                    .operations[1].real_value,
                8
            ),
            -97.72500000
        )
