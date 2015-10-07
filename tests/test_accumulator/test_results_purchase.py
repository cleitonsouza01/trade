"""Tests the result calc for purchase operations."""

from __future__ import absolute_import
import unittest

from trade import Accumulator

from . fixture_operations import (
    ASSET,
    OPERATION0,
    OPERATION1,
    OPERATION2,
    OPERATION3,
    OPERATION4,
    OPERATION5,
    OPERATION6,
    OPERATION7,
    OPERATION8
)

EXPECTED_LOG0 = {
    '2015-01-02': {
        'position': {
            'quantity': 0,
            'price': 0,
        },
        'occurrences': [OPERATION1]
    },
    '2015-01-01': {
        'position': {
            'quantity': -100,
            'price': 10,
        },
        'occurrences': [OPERATION0]
    }
}

EXPECTED_LOG1 = {
    '2015-01-03': {
        'position': {
            'quantity': -100,
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
            'quantity': -100,
            'price': 10,
        },
        'occurrences': [OPERATION0]
    }
}

EXPECTED_LOG2 = {
    '2015-01-04': {
        'position': {
            'quantity': 0,
            'price': 0,
        },
        'occurrences': [OPERATION3]
    },
    '2015-01-03': {
        'position': {
            'quantity': -100,
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
            'quantity': -100,
            'price': 10,
        },
        'occurrences': [OPERATION0]
    }
}

EXPECTED_LOG3 = {
    '2015-01-05': {
        'position': {
            'quantity': -100,
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
            'quantity': -100,
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
            'quantity': -100,
            'price': 10,
        },
        'occurrences': [OPERATION0]
    }
}

EXPECTED_LOG4 = {
    '2015-01-06': {
        'position': {
            'quantity': 00,
            'price': 0,
        },
        'occurrences': [OPERATION5]
    },
    '2015-01-05': {
        'position': {
            'quantity': -100,
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
            'quantity': -100,
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
            'quantity': -100,
            'price': 10,
        },
        'occurrences': [OPERATION0]
    }
}

EXPECTED_LOG5 = {
    '2015-01-06': {
        'position': {
            'quantity': -50,
            'price': 20,
        },
        'occurrences': [OPERATION6]
    },
    '2015-01-05': {
        'position': {
            'quantity': -100,
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
            'quantity': -100,
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
            'quantity': -100,
            'price': 10,
        },
        'occurrences': [OPERATION0]
    }
}

EXPECTED_LOG6 = {
    '2015-01-02': {
        'position': {
            'quantity': 0,
            'price': 0,
        },
        'occurrences': [OPERATION1]
    },
    '2015-01-01': {
        'position': {
            'quantity': -100,
            'price': 20,
        },
        'occurrences': [OPERATION7]
    },
}

EXPECTED_LOG7 = {
    '2015-01-02': {
        'position': {
            'quantity': 50,
            'price': 10,
        },
        'occurrences': [OPERATION1]
    },
    '2015-01-01': {
        'position': {
            'quantity': -50,
            'price': 20,
        },
        'occurrences': [OPERATION8]
    },
}


class TestAccumulatorResultsPurchaseCase00(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG0)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {})


class TestAccumulatorResultsPurchaseCase01(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(OPERATION2)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG1)

    def test_accumulated_result(self):
        expected_log = {}
        self.assertEqual(self.accumulator.results, expected_log)

    def test_current_quantity(self):
        self.assertEqual(self.accumulator.quantity, -100)

    def test_current_price(self):
        self.assertEqual(self.accumulator.price, 10)


class TestAccumulatorResultsPurchaseCase02(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(OPERATION2)
        self.accumulator.accumulate_occurrence(OPERATION3)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG2)

    def test_accumulated_result(self):
        expected_log = {'trades': -1000}
        self.assertEqual(self.accumulator.results, expected_log)


class TestAccumulatorResultsPurchaseCase03(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(OPERATION2)
        self.accumulator.accumulate_occurrence(OPERATION3)
        self.accumulator.accumulate_occurrence(OPERATION4)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG3)

    def test_accumulated_result(self):
        expected_log = {'trades': -1000}
        self.assertEqual(self.accumulator.results, expected_log)


class TestAccumulatorResultsPurchaseCase04(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(OPERATION2)
        self.accumulator.accumulate_occurrence(OPERATION3)
        self.accumulator.accumulate_occurrence(OPERATION4)
        self.accumulator.accumulate_occurrence(OPERATION5)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG4)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': -3000})


class TestAccumulatorResultsPurchaseCase05(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION0)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.accumulator.accumulate_occurrence(OPERATION2)
        self.accumulator.accumulate_occurrence(OPERATION3)
        self.accumulator.accumulate_occurrence(OPERATION4)
        self.accumulator.accumulate_occurrence(OPERATION6)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG5)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': -2000})


class TestAccumulatorResultsPurchaseCase06(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION7)
        self.accumulator.accumulate_occurrence(OPERATION1)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG6)

    def test_accumulated_result(self):
        expected_log = {'trades': 1000}
        self.assertEqual(self.accumulator.results, expected_log)


class TestAccumulatorResultsPurchaseCase07(unittest.TestCase):
    """Test profits or losses originating from purchase operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION8)
        self.accumulator.accumulate_occurrence(OPERATION1)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG7)

    def test_accumulated_result(self):
        expected_log = {'trades': 500}
        self.assertEqual(self.accumulator.results, expected_log)
