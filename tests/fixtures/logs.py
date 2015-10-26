"""A set of logs for the accumulator tests."""

from __future__ import absolute_import
import unittest
import copy

import trade

from tests.fixtures.assets import (
    ASSET
)

class LogTest(unittest.TestCase):
    """Base class for Accumulator tests."""

    maxDiff = None
    initial_state = {}
    occurrences = []
    expected_log = {}
    expected_state = {
        'quantity': 0,
        'price': 0,
        'results': {},
    }

    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET, logging=True)
        if self.initial_state:
            self.accumulator.data = copy.deepcopy(self.initial_state)
        self.accumulate_occurrences()

    def accumulate_occurrences(self):
        """Accumulates all occurrences defined in the test case."""
        for occurrence in self.occurrences:
            self.accumulator.accumulate(occurrence)

    def test_purchase_result_log(self):
        """Test the log for the defined occurrences."""
        if self.expected_log:
            self.assertEqual(self.accumulator.log, self.expected_log)

    def test_accumulated_result(self):
        """Test the results for the defined occurrences."""
        self.assertEqual(
            self.accumulator.data['results'], self.expected_state['results'])

    def test_current_quantity(self):
        """Test the quantity for the defined occurrences."""
        self.assertEqual(
            self.accumulator.data['quantity'], self.expected_state['quantity'])

    def test_current_price(self):
        self.assertEqual(
            round(self.accumulator.data['price'], 2), self.expected_state['price'])


INITIAL_STATE0 = {
    'quantity': 100,
    'price': 10,
    'results': {'trades': 1200},
}




EXPECTED_STATE0 = {
    'quantity': 200,
    'price': 5,
    'results': {'trades': 1200},
}
EXPECTED_STATE1 = {
    'quantity': 0,
    'price': 0,
    'results': {},
}
EXPECTED_STATE2 = {
    'quantity': -100,
    'price': 10,
    'results': {},
}
EXPECTED_STATE3 = {
    'quantity': 0,
    'price': 0,
    'results': {'trades': -1000},
}
EXPECTED_STATE4 = {
    'quantity': -100,
    'price': 20,
    'results': {'trades': -1000},
}
EXPECTED_STATE5 = {
    'quantity': 0,
    'price': 0,
    'results': {'trades': -3000},
}
EXPECTED_STATE6 = {
    'quantity': -50,
    'price': 20,
    'results': {'trades': -2000},
}
EXPECTED_STATE7 = {
    'quantity': 0,
    'price': 0,
    'results': {'trades': 1000},
}
EXPECTED_STATE8 = {
    'quantity': 50,
    'price': 10,
    'results': {'trades': 500},
}
EXPECTED_STATE9 = {
    'quantity': 100,
    'price': 10,
    'results': {},
}
EXPECTED_STATE10 = {
    'quantity': 100,
    'price': 20,
    'results': {'trades': 1000},
}
EXPECTED_STATE11 = {
    'quantity': 0,
    'price': 0,
    'results': {'trades': 3000},
}
EXPECTED_STATE12 = {
    'quantity': 50,
    'price': 20,
    'results': {'trades': 2000},
}
EXPECTED_STATE13 = {
    'quantity': -50,
    'price': 20,
    'results': {'trades': 500},
}
EXPECTED_STATE14 = {
    'quantity': 100,
    'price': 10,
    'results': {'trades': 1202},
}
EXPECTED_STATE15 = {
    'quantity': 10,
    'price': 10.2,
    'results': {},
}
EXPECTED_STATE16 = {
    'quantity': 20,
    'price': 0,
    'results': {},
}
EXPECTED_STATE17 = {
    'quantity': 0,
    'price': 0,
    'results': {'trades': -200},
}
EXPECTED_STATE18 = {
    'quantity': 100,
    'price': 10,
    'results': {'trades': 1000},
}
EXPECTED_STATE19 = {
    'quantity': 100,
    'price': 10,
    'results': {'trades': 2000},
}
EXPECTED_STATE20 = {
    'quantity': 50,
    'price': 20,
    'results': {'trades': 1200},
}
EXPECTED_STATE21 = {
    'quantity': 300,
    'price': 3.33,
    'results': {'trades': 1200},
}
EXPECTED_STATE22 = {
    'quantity': 150,
    'price': 6.67,
    'results': {'trades': 1200},
}
EXPECTED_STATE23 = {
    'quantity': 100,
    'price': 10,
    'results': {'daytrades': 1000},
}
EXPECTED_STATE24 = {
    'quantity': 100,
    'price': 10,
    'results': {'daytrades': 2000},
}
EXPECTED_STATE25 = {
    'quantity': 0,
    'price': 0,
    'results': {'daytrades': 1000},
}
EXPECTED_STATE26 = {
    'quantity': 20,
    'price': 10.2,
    'results': {},
}


EXPECTED_LOG0 = {
    '2015-01-02': {
        'quantity': 0,
        'price': 0,
        'results': {},
    },
    '2015-01-01': {
        'quantity': 100,
        'price': 10,
        'results': {},
    }
}

EXPECTED_LOG1 = {
    '2015-01-03': {
        'quantity': 100,
        'price': 10,
        'results': {},
    },
    '2015-01-02': {
        'quantity': 0,
        'price': 0,
        'results': {},
    },
    '2015-01-01': {
        'quantity': 100,
        'price': 10,
        'results': {},
    }
}

EXPECTED_LOG2 = {
    '2015-01-04': {
        'quantity': 0,
        'price': 0,
        'results': {'trades': 1000},
    },
    '2015-01-03': {
        'quantity': 100,
        'price': 10,
        'results': {},
    },
    '2015-01-02': {
        'quantity': 0,
        'price': 0,
        'results': {},
    },
    '2015-01-01': {
        'quantity': 100,
        'price': 10,
        'results': {},
    }
}

EXPECTED_LOG3 = {
    '2015-01-05': {
        'quantity': 100,
        'price': 20,
        'results': {'trades': 1000},
    },
    '2015-01-04': {
        'quantity': 0,
        'price': 0,
        'results': {'trades': 1000},
    },
    '2015-01-03': {
        'quantity': 100,
        'price': 10,
        'results': {},
    },
    '2015-01-02': {
        'quantity': 0,
        'price': 0,
        'results': {},
    },
    '2015-01-01': {
        'quantity': 100,
        'price': 10,
        'results': {},
    }
}

EXPECTED_LOG4 = {
    '2015-01-06': {
        'quantity': 0,
        'price': 0,
        'results': {'trades': 3000},
    },
    '2015-01-05': {
        'quantity': 100,
        'price': 20,
        'results': {'trades': 1000},
    },
    '2015-01-04': {
        'quantity': 0,
        'price': 0,
        'results': {'trades': 1000},
    },
    '2015-01-03': {
        'quantity': 100,
        'price': 10,
        'results': {},
    },
    '2015-01-02': {
        'quantity': 0,
        'price': 0,
        'results': {},
    },
    '2015-01-01': {
        'quantity': 100,
        'price': 10,
        'results': {},
    }
}

EXPECTED_LOG5 = {
    '2015-01-06': {
        'quantity': 50,
        'price': 20,
        'results': {'trades': 2000},
    },
    '2015-01-05': {
        'quantity': 100,
        'price': 20,
        'results': {'trades': 1000},
    },
    '2015-01-04': {
        'quantity': 0,
        'price': 0,
        'results': {'trades': 1000},
    },
    '2015-01-03': {
        'quantity': 100,
        'price': 10,
        'results': {},
    },
    '2015-01-02': {
        'quantity': 0,
        'price': 0,
        'results': {},
    },
    '2015-01-01': {
        'quantity': 100,
        'price': 10,
        'results': {},
    }
}

EXPECTED_LOG6 = {
    '2015-01-02': {
        'quantity': -50,
        'price': 20,
        'results': {'trades': 500},
    },
    '2015-01-01': {
        'quantity': 50,
        'price': 10,
        'results': {},
    },

}


EXPECTED_LOG7 = {
    '2015-01-02': {
        'quantity': 0,
        'price': 0,
        'results': {},
    },
    '2015-01-01': {
        'quantity': -100,
        'price': 10,
        'results': {},
    }
}

EXPECTED_LOG8 = {
    '2015-01-03': {
        'quantity': -100,
        'price': 10,
        'results': {},
    },
    '2015-01-02': {
        'quantity': 0,
        'price': 0,
        'results': {},
    },
    '2015-01-01': {
        'quantity': -100,
        'price': 10,
        'results': {},
    }
}

EXPECTED_LOG9 = {
    '2015-01-05': {
        'quantity': -100,
        'price': 20,
        'results': {'trades': -1000},
    },
    '2015-01-04': {
        'quantity': 0,
        'price': 0,
        'results': {'trades': -1000},
    },
    '2015-01-03': {
        'quantity': -100,
        'price': 10,
        'results': {},
    },
    '2015-01-02': {
        'quantity': 0,
        'price': 0,
        'results': {},
    },
    '2015-01-01': {
        'quantity': -100,
        'price': 10,
        'results': {},
    }
}

EXPECTED_LOG10 = {
    '2015-01-06': {
        'quantity': 00,
        'price': 0,
        'results': {'trades': -3000},
    },
    '2015-01-05': {
        'quantity': -100,
        'price': 20,
        'results': {'trades': -1000},
    },
    '2015-01-04': {
        'quantity': 0,
        'price': 0,
        'results': {'trades': -1000},
    },
    '2015-01-03': {
        'quantity': -100,
        'price': 10,
        'results': {},
    },
    '2015-01-02': {
        'quantity': 0,
        'price': 0,
        'results': {},
    },
    '2015-01-01': {
        'quantity': -100,
        'price': 10,
        'results': {},
    }
}

EXPECTED_LOG11 = {
    '2015-01-04': {
        'quantity': 0,
        'price': 0,
        'results': {'trades': -1000},
    },
    '2015-01-03': {
        'quantity': -100,
        'price': 10,
        'results': {},
    },
    '2015-01-02': {
        'quantity': 0,
        'price': 0,
        'results': {},
    },
    '2015-01-01': {
        'quantity': -100,
        'price': 10,
        'results': {},
    }
}

EXPECTED_LOG12 = {
    '2015-01-06': {
        'quantity': -50,
        'price': 20,
        'results': {'trades': -2000},
    },
    '2015-01-05': {
        'quantity': -100,
        'price': 20,
        'results': {'trades': -1000},
    },
    '2015-01-04': {
        'quantity': 0,
        'price': 0,
        'results': {'trades': -1000},
    },
    '2015-01-03': {
        'quantity': -100,
        'price': 10,
        'results': {},
    },
    '2015-01-02': {
        'quantity': 0,
        'price': 0,
        'results': {},
    },
    '2015-01-01': {
        'quantity': -100,
        'price': 10,
        'results': {},
    }
}

EXPECTED_LOG13 = {
    '2015-01-02': {
        'quantity': 50,
        'price': 10,
        'results': {'trades': 500},
    },
    '2015-01-01': {
        'quantity': -50,
        'price': 20,
        'results': {},
    },
}

EXPECTED_LOG14 = {
    '2015-01-02': {
        'quantity': 0,
        'price': 0,
        'results': {'trades': 1000},
    },
    '2015-01-01': {
        'quantity': -100,
        'price': 20,
        'results': {},
    },
}

EXPECTED_LOG15 = {
    '2015-01-01': {
        'quantity': 100,
        'price': 10,
        'results': {},
    }
}

EXPECTED_LOG16 = {
    '2015-01-01': {
        'quantity': 0,
        'price': 0,
        'results': {'daytrades': 1000},
    }
}

EXPECTED_LOG17 = {
    '2015-09-24': {
        'price': 5.0,
        'quantity': 200,
        'results': {'trades': 1200},
    }
}

EXPECTED_LOG18 = {
    '2015-09-25': {
        'price': 5.0,
        'quantity': 200,
        'results': {'trades': 1200},
    },
    '2015-09-24': {
        'price': 5.0,
        'quantity': 200,
        'results': {'trades': 1200},
    }
}
EXPECTED_LOG25 = {
    '2015-09-24': {
        'price': 5.0,
        'quantity': 200,
        'results': {'trades': 1200},
    }
}


EXPECTED_LOG19 = {
    '2015-01-01': {
        'quantity': 100,
        'price': 10,
        'results': {'daytrades': 1000},
    }
}


EXPECTED_LOG20 = {
    '2015-01-03': {
        'quantity': 100,
        'price': 10,
        'results': {'daytrades': 1000},
    },
    '2015-01-02': {
        'quantity': 100,
        'price': 10,
        'results': {'daytrades': 1000},
    },
    '2015-01-01': {
        'quantity': 0,
        'price': 0,
        'results': {'daytrades': 1000},
    }
}

EXPECTED_LOG21 = {
    '2015-01-02': {
        'quantity': 100,
        'price': 10,
        'results': {'daytrades': 2000}
    },
    '2015-01-01': {
        'quantity': 0,
        'price': 0,
        'results': {'daytrades': 1000}
    }
}

EXPECTED_LOG22 = {
    '2015-01-01': {
        'quantity': 100,
        'price': 10,
        'results': {'daytrades': 1000}
    }
}

EXPECTED_LOG23 = {
    '2015-01-02': {
        'quantity': 100,
        'price': 10,
        'results': {'daytrades': 1000}
    },
    '2015-01-01': {
        'quantity': 0,
        'price': 0,
        'results': {'daytrades': 1000}
    }
}


EXPECTED_LOG24 = {
    '2015-01-02': {
        'quantity': 100,
        'price': 10,
        'results': {'daytrades': 2000}
    },
    '2015-01-01': {
        'quantity': 0,
        'price': 0,
        'results': {'daytrades': 1000}
    }
}
