from __future__ import absolute_import
import unittest

from trade import Accumulator as AssetAccumulator


# TODO document this
# TODO more tests


class TestAccumulatorResults_sale_case_00(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', log_operations=True)
        self.accumulator.accumulate(100, 10, date='2015-01-01')
        self.accumulator.accumulate(-100, 10, date='2015-01-02')

    def test_sale_result_log(self):
        expected_log = {
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'operations': [{
                    'quantity': -100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        expected_log = {
            'trade': 0
        }
        self.assertEqual(self.accumulator.results, expected_log)


class TestAccumulatorResults_sale_case_01(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', log_operations=True)
        self.accumulator.accumulate(100, 10, date='2015-01-01')
        self.accumulator.accumulate(-100, 10, date='2015-01-02')
        self.accumulator.accumulate(100, 10, date='2015-01-03')

    def test_sale_result_log(self):
        expected_log = {
            '2015-01-03': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'operations': [{
                    'quantity': -100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        expected_log = {
            'trade': 0
        }
        self.assertEqual(self.accumulator.results, expected_log)


class TestAccumulatorResults_sale_case_02(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', log_operations=True)
        self.accumulator.accumulate(100, 10, date='2015-01-01')
        self.accumulator.accumulate(-100, 10, date='2015-01-02')
        self.accumulator.accumulate(100, 10, date='2015-01-03')
        self.accumulator.accumulate(-100, 20, date='2015-01-04')

    def test_sale_result_log(self):
        expected_log = {
            '2015-01-04': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'operations': [{
                    'quantity': -100,
                    'price': 20,
                    'results': {
                        'trade': 1000
                    }
                }]
            },
            '2015-01-03': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'operations': [{
                    'quantity': -100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        expected_log = {
            'trade': 1000
        }
        self.assertEqual(self.accumulator.results, expected_log)



class TestAccumulatorResults_sale_case_01(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', log_operations=True)
        self.accumulator.accumulate(100, 10, date='2015-01-01')
        self.accumulator.accumulate(-100, 10, date='2015-01-02')
        self.accumulator.accumulate(100, 10, date='2015-01-03')

    def test_sale_result_log(self):
        expected_log = {
            '2015-01-03': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 00,
                    'price': 0,
                },
                'operations': [{
                    'quantity': -100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            },
        '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        expected_log = {
            'trade': 0
        }
        self.assertEqual(self.accumulator.results, expected_log)


class TestAccumulatorResults_sale_case_03(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', log_operations=True)
        self.accumulator.accumulate(100, 10, date='2015-01-01')
        self.accumulator.accumulate(-100, 10, date='2015-01-02')
        self.accumulator.accumulate(100, 10, date='2015-01-03')
        self.accumulator.accumulate(-100, 20, date='2015-01-04')
        self.accumulator.accumulate(100, 20, date='2015-01-05')

    def test_sale_result_log(self):
        expected_log = {
            '2015-01-05': {
                'position': {
                    'quantity': 100,
                    'price': 20,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 20,
                    'results': {
                        'trade': 0
                    }
                }]
            },
            '2015-01-04': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'operations': [{
                    'quantity': -100,
                    'price': 20,
                    'results': {
                        'trade': 1000
                    }
                }]
            },
            '2015-01-03': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'operations': [{
                    'quantity': -100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        expected_log = {
            'trade': 1000
        }
        self.assertEqual(self.accumulator.results, expected_log)



class TestAccumulatorResults_sale_case_04(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', log_operations=True)
        self.accumulator.accumulate(100, 10, date='2015-01-01')
        self.accumulator.accumulate(-100, 10, date='2015-01-02')
        self.accumulator.accumulate(100, 10, date='2015-01-03')
        self.accumulator.accumulate(-100, 20, date='2015-01-04')
        self.accumulator.accumulate(100, 20, date='2015-01-05')
        self.accumulator.accumulate(-100, 40, date='2015-01-06')

    def test_sale_result_log(self):
        expected_log = {
            '2015-01-06': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'operations': [{
                    'quantity': -100,
                    'price': 40,
                    'results': {
                        'trade': 2000
                    }
                }]
            },
            '2015-01-05': {
                'position': {
                    'quantity': 100,
                    'price': 20,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 20,
                    'results': {
                        'trade': 0
                    }
                }]
            },
            '2015-01-04': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'operations': [{
                    'quantity': -100,
                    'price': 20,
                    'results': {
                        'trade': 1000
                    }
                }]
            },
            '2015-01-03': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'operations': [{
                    'quantity': -100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        expected_log = {
            'trade': 3000
        }
        self.assertEqual(self.accumulator.results, expected_log)


class TestAccumulatorResults_sale_case_05(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.accumulator = AssetAccumulator('euro', log_operations=True)
        self.accumulator.accumulate(100, 10, date='2015-01-01')
        self.accumulator.accumulate(-100, 10, date='2015-01-02')
        self.accumulator.accumulate(100, 10, date='2015-01-03')
        self.accumulator.accumulate(-100, 20, date='2015-01-04')
        self.accumulator.accumulate(100, 20, date='2015-01-05')
        self.accumulator.accumulate(-50, 40, date='2015-01-06')

    def test_sale_result_log(self):
        expected_log = {
            '2015-01-06': {
                'position': {
                    'quantity': 50,
                    'price': 20,
                },
                'operations': [{
                    'quantity': -50,
                    'price': 40,
                    'results': {
                        'trade': 1000
                    }
                }]
            },
            '2015-01-05': {
                'position': {
                    'quantity': 100,
                    'price': 20,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 20,
                    'results': {
                        'trade': 0
                    }
                }]
            },
            '2015-01-04': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'operations': [{
                    'quantity': -100,
                    'price': 20,
                    'results': {
                        'trade': 1000
                    }
                }]
            },
            '2015-01-03': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 0,
                    'price': 0,
                },
                'operations': [{
                    'quantity': -100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10,
                },
                'operations': [{
                    'quantity': 100,
                    'price': 10,
                    'results': {
                        'trade': 0
                    }
                }]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_accumulated_result(self):
        expected_log = {
            'trade': 2000
        }
        self.assertEqual(self.accumulator.results, expected_log)
