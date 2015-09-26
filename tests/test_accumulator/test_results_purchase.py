from __future__ import absolute_import
import unittest

from trade import Accumulator as AssetAccumulator
from trade import Asset, Operation


# TODO document this
# TODO more tests


class TestAccumulatorResults_purchase_case_00(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', logging=True)

        self.operation0 = Operation(-100, 10, date='2015-01-01', asset=Asset())
        self.accumulator.accumulate_operation(self.operation0)

        self.operation1 = Operation(100, 10, date='2015-01-02', asset=Asset())
        self.accumulator.accumulate_operation(self.operation1)

    def test_purchase_result_log(self):
        expected_log = {
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [self.operation1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': -100,
                    'price': 10,
                },
                'occurrences': [self.operation0]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        expected_log = {
            'daytrades':0, 'trades': 0
        }
        self.assertEqual(self.accumulator.results, expected_log)


class TestAccumulatorResults_purchase_case_01(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', logging=True)

        self.operation0 = Operation(-100, 10, date='2015-01-01', asset=Asset())
        self.accumulator.accumulate_operation(self.operation0)

        self.operation1 = Operation(100, 10, date='2015-01-02', asset=Asset())
        self.accumulator.accumulate_operation(self.operation1)

        self.operation2 = Operation(-100, 10, date='2015-01-03', asset=Asset())
        self.accumulator.accumulate_operation(self.operation2)

    def test_log_2015_01_01(self):
        expected_log  = {
                'position': {
                    'quantity': -100,
                    'price': 10,
                },
                'occurrences': [self.operation0]
        }
        self.assertEqual(self.accumulator.log['2015-01-01'], expected_log)

    def test_log_2015_01_02(self):
        expected_log  = {
            'position': {
                'quantity': 0,
                'price': 0,
            },
            'occurrences': [self.operation1]
        }
        self.assertEqual(self.accumulator.log['2015-01-02'], expected_log)

    def test_purchase_result_log(self):
        expected_log = {
            '2015-01-03': {
                'position': {
                    'quantity': -100,
                    'price': 10,
                },
                'occurrences': [self.operation2]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [self.operation1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': -100,
                    'price': 10,
                },
                'occurrences': [self.operation0]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        expected_log = {
            'daytrades':0, 'trades': 0
        }
        self.assertEqual(self.accumulator.results, expected_log)

    def test_current_quantity(self):
        self.assertEqual(self.accumulator.quantity, -100)

    def test_current_price(self):
        self.assertEqual(self.accumulator.price, 10)


class TestAccumulatorResults_purchase_case_02(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', logging=True)

        self.operation0 = Operation(-100, 10, date='2015-01-01', asset=Asset())
        self.accumulator.accumulate_operation(self.operation0)

        self.operation1 = Operation(100, 10, date='2015-01-02', asset=Asset())
        self.accumulator.accumulate_operation(self.operation1)

        self.operation2 = Operation(-100, 10, date='2015-01-03', asset=Asset())
        self.accumulator.accumulate_operation(self.operation2)

        self.operation3 = Operation(100, 20, date='2015-01-04', asset=Asset())
        self.accumulator.accumulate_operation(self.operation3)

    def test_purchase_result_log(self):
        expected_log = {
            '2015-01-04': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [self.operation3]
            },
            '2015-01-03': {
                'position': {
                    'quantity': -100,
                    'price': 10,
                },
                'occurrences': [self.operation2]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [self.operation1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': -100,
                    'price': 10,
                },
                'occurrences': [self.operation0]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        expected_log = {
            'daytrades':0, 'trades': -1000
        }
        self.assertEqual(self.accumulator.results, expected_log)


class TestAccumulatorResults_purchase_case_03(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', logging=True)

        self.operation0 = Operation(-100, 10, date='2015-01-01', asset=Asset())
        self.accumulator.accumulate_operation(self.operation0)

        self.operation1 = Operation(100, 10, date='2015-01-02', asset=Asset())
        self.accumulator.accumulate_operation(self.operation1)

        self.operation2 = Operation(-100, 10, date='2015-01-03', asset=Asset())
        self.accumulator.accumulate_operation(self.operation2)

        self.operation3 = Operation(100, 20, date='2015-01-04', asset=Asset())
        self.accumulator.accumulate_operation(self.operation3)

        self.operation4 = Operation(-100, 20, date='2015-01-05', asset=Asset())
        self.accumulator.accumulate_operation(self.operation4)

    def test_purchase_result_log(self):
        expected_log = {
            '2015-01-05': {
                'position': {
                    'quantity': -100,
                    'price': 20,
                },
                'occurrences': [self.operation4]
            },
            '2015-01-04': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [self.operation3]
            },
            '2015-01-03': {
                'position': {
                    'quantity': -100,
                    'price': 10,
                },
                'occurrences': [self.operation2]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [self.operation1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': -100,
                    'price': 10,
                },
                'occurrences': [self.operation0]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        expected_log = {
            'daytrades':0, 'trades': -1000
        }
        self.assertEqual(self.accumulator.results, expected_log)


class TestAccumulatorResults_purchase_case_04(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', logging=True)

        self.operation0 = Operation(-100, 10, date='2015-01-01', asset=Asset())
        self.accumulator.accumulate_operation(self.operation0)

        self.operation1 = Operation(100, 10, date='2015-01-02', asset=Asset())
        self.accumulator.accumulate_operation(self.operation1)

        self.operation2 = Operation(-100, 10, date='2015-01-03', asset=Asset())
        self.accumulator.accumulate_operation(self.operation2)

        self.operation3 = Operation(100, 20, date='2015-01-04', asset=Asset())
        self.accumulator.accumulate_operation(self.operation3)

        self.operation4 = Operation(-100, 20, date='2015-01-05', asset=Asset())
        self.accumulator.accumulate_operation(self.operation4)

        self.operation5 = Operation(100, 40, date='2015-01-06', asset=Asset())
        self.accumulator.accumulate_operation(self.operation5)

    def test_purchase_result_log(self):
        expected_log = {
            '2015-01-06': {
                'position': {
                    'quantity': 00,
                    'price': 0,
                },
                'occurrences': [self.operation5]
            },
            '2015-01-05': {
                'position': {
                    'quantity': -100,
                    'price': 20,
                },
                'occurrences': [self.operation4]
            },
            '2015-01-04': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [self.operation3]
            },
            '2015-01-03': {
                'position': {
                    'quantity': -100,
                    'price': 10,
                },
                'occurrences': [self.operation2]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [self.operation1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': -100,
                    'price': 10,
                },
                'occurrences': [self.operation0]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        expected_log = {
            'daytrades':0, 'trades': -3000
        }
        self.assertEqual(self.accumulator.results, expected_log)


class TestAccumulatorResults_purchase_case_05(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', logging=True)

        self.operation0 = Operation(-100, 10, date='2015-01-01', asset=Asset())
        self.accumulator.accumulate_operation(self.operation0)

        self.operation1 = Operation(100, 10, date='2015-01-02', asset=Asset())
        self.accumulator.accumulate_operation(self.operation1)

        self.operation2 = Operation(-100, 10, date='2015-01-03', asset=Asset())
        self.accumulator.accumulate_operation(self.operation2)

        self.operation3 = Operation(100, 20, date='2015-01-04', asset=Asset())
        self.accumulator.accumulate_operation(self.operation3)

        self.operation4 = Operation(-100, 20, date='2015-01-05', asset=Asset())
        self.accumulator.accumulate_operation(self.operation4)

        self.operation5 = Operation(50, 40, date='2015-01-06', asset=Asset())
        self.accumulator.accumulate_operation(self.operation5)

    def test_purchase_result_log(self):
        expected_log = {
            '2015-01-06': {
                'position': {
                    'quantity': -50,
                    'price': 20,
                },
                'occurrences': [self.operation5]
            },
            '2015-01-05': {
                'position': {
                    'quantity': -100,
                    'price': 20,
                },
                'occurrences': [self.operation4]
            },
            '2015-01-04': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [self.operation3]
            },
            '2015-01-03': {
                'position': {
                    'quantity': -100,
                    'price': 10,
                },
                'occurrences': [self.operation2]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [self.operation1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': -100,
                    'price': 10,
                },
                'occurrences': [self.operation0]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        expected_log = {
            'daytrades':0, 'trades': -2000
        }
        self.assertEqual(self.accumulator.results, expected_log)


class TestAccumulatorResults_purchase_case_06(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', logging=True)

        self.operation0 = Operation(-100, 20, date='2015-01-01', asset=Asset())
        self.accumulator.accumulate_operation(self.operation0)

        self.operation1 = Operation(100, 10, date='2015-01-02', asset=Asset())
        self.accumulator.accumulate_operation(self.operation1)

    def test_purchase_result_log(self):
        expected_log = {
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'occurrences': [self.operation1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': -100,
                    'price': 20,
                },
                'occurrences': [self.operation0]
            },

        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        expected_log = {
            'daytrades':0, 'trades': 1000
        }
        self.assertEqual(self.accumulator.results, expected_log)


class TestAccumulatorResults_purchase_case_07(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', logging=True)

        self.operation0 = Operation(-50, 20, date='2015-01-01', asset=Asset())
        self.accumulator.accumulate_operation(self.operation0)

        self.operation1 = Operation(100, 10, date='2015-01-02', asset=Asset())
        self.accumulator.accumulate_operation(self.operation1)

    def test_purchase_result_log(self):
        expected_log = {
            '2015-01-02': {
                'position': {
                    'quantity': 50,
                    'price': 10,
                },
                'occurrences': [self.operation1]
            },
            '2015-01-01': {
                'position': {
                    'quantity': -50,
                    'price': 20,
                },
                'occurrences': [self.operation0]
            },

        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        expected_log = {
            'daytrades':0, 'trades': 500
        }
        self.assertEqual(self.accumulator.results, expected_log)
