"""Tests the result calc for sale operations."""

from __future__ import absolute_import
import unittest

from trade import Accumulator

from . fixture_operations import (
    ASSET,
    OPERATION9,
    OPERATION10,
    OPERATION11,
    OPERATION12,
    OPERATION13,
    OPERATION14,
    OPERATION15,
    OPERATION16,
    OPERATION17
)

EXPECTED_LOG0 = {
    '2015-01-02': {
        'position': {
            'quantity': 0,
            'price': 0,
        },
        'occurrences': [OPERATION10]
    },
    '2015-01-01': {
        'position': {
            'quantity': 100,
            'price': 10,
        },
        'occurrences': [OPERATION9]
    }
}

EXPECTED_LOG1 = {
    '2015-01-03': {
        'position': {
            'quantity': 100,
            'price': 10,
        },
        'occurrences': [OPERATION11]
    },
    '2015-01-02': {
        'position': {
            'quantity': 0,
            'price': 0,
        },
        'occurrences': [OPERATION10]
    },
    '2015-01-01': {
        'position': {
            'quantity': 100,
            'price': 10,
        },
        'occurrences': [OPERATION9]
    }
}

EXPECTED_LOG2 = {
    '2015-01-04': {
        'position': {
            'quantity': 0,
            'price': 0,
        },
        'occurrences': [OPERATION12]
    },
    '2015-01-03': {
        'position': {
            'quantity': 100,
            'price': 10,
        },
        'occurrences': [OPERATION11]
    },
    '2015-01-02': {
        'position': {
            'quantity': 0,
            'price': 0,
        },
        'occurrences': [OPERATION10]
    },
    '2015-01-01': {
        'position': {
            'quantity': 100,
            'price': 10,
        },
        'occurrences': [OPERATION9]
    }
}

EXPECTED_LOG3 = {
    '2015-01-05': {
        'position': {
            'quantity': 100,
            'price': 20,
        },
        'occurrences': [OPERATION13]
    },
    '2015-01-04': {
        'position': {
            'quantity': 0,
            'price': 0,
        },
        'occurrences': [OPERATION12]
    },
    '2015-01-03': {
        'position': {
            'quantity': 100,
            'price': 10,
        },
        'occurrences': [OPERATION11]
    },
    '2015-01-02': {
        'position': {
            'quantity': 0,
            'price': 0,
        },
        'occurrences': [OPERATION10]
    },
    '2015-01-01': {
        'position': {
            'quantity': 100,
            'price': 10,
        },
        'occurrences': [OPERATION9]
    }
}


EXPECTED_LOG4 = {
    '2015-01-06': {
        'position': {
            'quantity': 0,
            'price': 0,
        },
        'occurrences': [OPERATION14]
    },
    '2015-01-05': {
        'position': {
            'quantity': 100,
            'price': 20,
        },
        'occurrences': [OPERATION13]
    },
    '2015-01-04': {
        'position': {
            'quantity': 0,
            'price': 0,
        },
        'occurrences': [OPERATION12]
    },
    '2015-01-03': {
        'position': {
            'quantity': 100,
            'price': 10,
        },
        'occurrences': [OPERATION11]
    },
    '2015-01-02': {
        'position': {
            'quantity': 0,
            'price': 0,
        },
        'occurrences': [OPERATION10]
    },
    '2015-01-01': {
        'position': {
            'quantity': 100,
            'price': 10,
        },
        'occurrences': [OPERATION9]
    }
}

EXPECTED_LOG5 = {
    '2015-01-06': {
        'position': {
            'quantity': 50,
            'price': 20,
        },
        'occurrences': [OPERATION15]
    },
    '2015-01-05': {
        'position': {
            'quantity': 100,
            'price': 20,
        },
        'occurrences': [OPERATION13]
    },
    '2015-01-04': {
        'position': {
            'quantity': 0,
            'price': 0,
        },
        'occurrences': [OPERATION12]
    },
    '2015-01-03': {
        'position': {
            'quantity': 100,
            'price': 10,
        },
        'occurrences': [OPERATION11]
    },
    '2015-01-02': {
        'position': {
            'quantity': 0,
            'price': 0,
        },
        'occurrences': [OPERATION10]
    },
    '2015-01-01': {
        'position': {
            'quantity': 100,
            'price': 10,
        },
        'occurrences': [OPERATION9]
    }
}

EXPECTED_LOG6 = {
    '2015-01-02': {
        'position': {
            'quantity': -50,
            'price': 20,
        },
        'occurrences': [OPERATION17]
    },
    '2015-01-01': {
        'position': {
            'quantity': 50,
            'price': 10,
        },
        'occurrences': [OPERATION16]
    },

}


class TestAccumulatorSaleResults(unittest.TestCase):

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION9)
        self.accumulator.accumulate_occurrence(OPERATION10)

class TestAccumulatorResultsSaleCase00(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG0)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {})


class TestAccumulatorResultsSaleCase01(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        super(TestAccumulatorResultsSaleCase01, self).setUp()
        self.accumulator.accumulate_occurrence(OPERATION11)

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG1)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {})


class TestAccumulatorResultsSaleCase02(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        super(TestAccumulatorResultsSaleCase02, self).setUp()
        self.accumulator.accumulate_occurrence(OPERATION11)
        self.accumulator.accumulate_occurrence(OPERATION12)

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG2)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 1000})


class TestAccumulatorResultsSaleCase04(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        super(TestAccumulatorResultsSaleCase04, self).setUp()
        self.accumulator.accumulate_occurrence(OPERATION11)
        self.accumulator.accumulate_occurrence(OPERATION12)
        self.accumulator.accumulate_occurrence(OPERATION13)

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG3)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 1000})


class TestAccumulatorResultsSaleCase05(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        super(TestAccumulatorResultsSaleCase05, self).setUp()
        self.accumulator.accumulate_occurrence(OPERATION11)
        self.accumulator.accumulate_occurrence(OPERATION12)
        self.accumulator.accumulate_occurrence(OPERATION13)
        self.accumulator.accumulate_occurrence(OPERATION14)

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG4)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 3000})


class TestAccumulatorResultsSaleCase06(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        super(TestAccumulatorResultsSaleCase06, self).setUp()

        self.accumulator.accumulate_occurrence(OPERATION11)
        self.accumulator.accumulate_occurrence(OPERATION12)
        self.accumulator.accumulate_occurrence(OPERATION13)
        self.accumulator.accumulate_occurrence(OPERATION15)

    def test_sale_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG5)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 2000})


class TestAccumulatorResultsSaleCase07(TestAccumulatorSaleResults):
    """Test profits or losses originating from sale operations."""

    def setUp(self):
        self.accumulator = Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(OPERATION16)
        self.accumulator.accumulate_occurrence(OPERATION17)

    def test_purchase_result_log(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG6)

    def test_accumulated_result(self):
        self.assertEqual(self.accumulator.results, {'trades': 500})
