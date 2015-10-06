"""Tests the result calc for sale operations."""

from __future__ import absolute_import
import unittest

from trade import Accumulator
from trade import Asset, Operation


ASSET = Asset()
OPERATION0 = Operation(
    quantity=100,
    price=10,
    date='2015-01-01',
    asset=ASSET
)
OPERATION1 = Operation(
    quantity=-100,
    price=10,
    date='2015-01-02',
    asset=ASSET
)
OPERATION2 = Operation(
    quantity=100,
    price=10,
    date='2015-01-03',
    asset=ASSET
)
OPERATION3 = Operation(
    quantity=-100,
    price=20,
    date='2015-01-04',
    asset=ASSET
)
OPERATION4 = Operation(
    quantity=100,
    price=20,
    date='2015-01-05',
    asset=ASSET
)
OPERATION5 = Operation(
    quantity=-100,
    price=40,
    date='2015-01-06',
    asset=ASSET
)


class TestAccumulatorResultsSaleCase00(unittest.TestCase):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)

    def test_sale_result_log(self):
        expected_log = {
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [OPERATION1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'occurrences': [OPERATION0]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {})


class TestAccumulatorResultsSaleCase01(unittest.TestCase):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(OPERATION2)

    def test_sale_result_log(self):
        expected_log = {
            '2015-01-03': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'occurrences': [OPERATION2]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [OPERATION1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'occurrences': [OPERATION0]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {})


class TestAccumulatorResultsSaleCase02(unittest.TestCase):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(OPERATION2)
        self.accumulator.accumulate_occurrence(OPERATION3)

    def test_sale_result_log(self):
        expected_log = {
            '2015-01-04': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [OPERATION3]
            },
            '2015-01-03': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'occurrences': [OPERATION2]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [OPERATION1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'occurrences': [OPERATION0]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 1000})


class TestAccumulatorResultsSaleCase04(unittest.TestCase):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(OPERATION2)
        self.accumulator.accumulate_occurrence(OPERATION3)
        self.accumulator.accumulate_occurrence(OPERATION4)

    def test_sale_result_log(self):
        expected_log = {
            '2015-01-05': {
                'position': {
                    'quantity': 100,
                    'price': 20,
                },
                'occurrences': [OPERATION4]
            },
            '2015-01-04': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [OPERATION3]
            },
            '2015-01-03': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'occurrences': [OPERATION2]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [OPERATION1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'occurrences': [OPERATION0]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 1000})


class TestAccumulatorResultsSaleCase05(unittest.TestCase):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(OPERATION2)
        self.accumulator.accumulate_occurrence(OPERATION3)
        self.accumulator.accumulate_occurrence(OPERATION4)
        self.accumulator.accumulate_occurrence(OPERATION5)

    def test_sale_result_log(self):
        expected_log = {
            '2015-01-06': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [OPERATION5]
            },
            '2015-01-05': {
                'position': {
                    'quantity': 100,
                    'price': 20,
                },
                'occurrences': [OPERATION4]
            },
            '2015-01-04': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [OPERATION3]
            },
            '2015-01-03': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'occurrences': [OPERATION2]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [OPERATION1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'occurrences': [OPERATION0]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 3000})


class TestAccumulatorResultsSaleCase06(unittest.TestCase):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.operation5 = Operation(
            quantity=-50,
            price=40,
            date='2015-01-06',
            asset=ASSET
        )
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(OPERATION2)
        self.accumulator.accumulate_occurrence(OPERATION3)
        self.accumulator.accumulate_occurrence(OPERATION4)
        self.accumulator.accumulate_occurrence(self.operation5)

    def test_sale_result_log(self):
        expected_log = {
            '2015-01-06': {
                'position': {
                    'quantity': 50,
                    'price': 20,
                },
                'occurrences': [self.operation5]
            },
            '2015-01-05': {
                'position': {
                    'quantity': 100,
                    'price': 20,
                },
                'occurrences': [OPERATION4]
            },
            '2015-01-04': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [OPERATION3]
            },
            '2015-01-03': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'occurrences': [OPERATION2]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [OPERATION1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'occurrences': [OPERATION0]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 2000})


class TestAccumulatorResultsSaleCase07(unittest.TestCase):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        self.asset = Asset()
        self.accumulator = Accumulator(self.asset, logging=True)

        self.operation0 = Operation(
            quantity=50,
            price=10,
            date='2015-01-01',
            asset=self.asset
        )
        self.operation1 = Operation(
            quantity=-100,
            price=20,
            date='2015-01-02',
            asset=self.asset
        )
        self.accumulator.accumulate_occurrence(self.operation0)
        self.accumulator.accumulate_occurrence(self.operation1)

    def test_purchase_result_log(self):
        expected_log = {
            '2015-01-02': {
                'position': {
                    'quantity': -50,
                    'price': 20,
                },
                'occurrences': [self.operation1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 50,
                    'price': 10,
                },
                'occurrences': [self.operation0]
            },

        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 500})
