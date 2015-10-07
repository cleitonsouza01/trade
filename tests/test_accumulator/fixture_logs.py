"""A set of operations for the accumualtor tests."""

from __future__ import absolute_import

from tests.fixtures.fixture_operations import (
    OPERATION0, OPERATION1, OPERATION2, OPERATION3, OPERATION4, OPERATION5,
    OPERATION6, OPERATION7, OPERATION8, OPERATION9, OPERATION10, OPERATION11,
    OPERATION12, OPERATION13, OPERATION14, OPERATION15, OPERATION16,
    OPERATION17, OPERATION18,

    DAYTRADE0, DAYTRADE2, DAYTRADE3, DAYTRADE1,
)
from tests.fixtures.fixture_events import (
    EVENT0, EVENT1, EVENT2, EVENT3, EVENT5,
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


EXPECTED_LOG7 = {
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

EXPECTED_LOG8 = {
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

EXPECTED_LOG9 = {
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

EXPECTED_LOG10 = {
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

EXPECTED_LOG11 = {
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

EXPECTED_LOG12 = {
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

EXPECTED_LOG13 = {
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

EXPECTED_LOG14 = {
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

EXPECTED_LOG15 = {
    '2015-01-01': {
        'position': {
            'quantity': 100,
            'price': 10
        },
        'occurrences': [OPERATION18]
    }
}

EXPECTED_LOG16 = {
    '2015-01-01': {
        'position': {
            'quantity': 0,
            'price': 0
        },
        'occurrences': [DAYTRADE0]
    }
}

EXPECTED_LOG17 = {
    '2015-09-24': {
        'position': {
            'price': 5.0,
            'quantity': 200
        },
        'occurrences': [EVENT5]
    }
}

EXPECTED_LOG18 = {
    '2015-09-25': {
        'position': {
            'price': 5.0,
            'quantity': 200
        },
        'occurrences': [EVENT3]
    },
    '2015-09-24': {
        'position': {
            'price': 5.0,
            'quantity': 200
        },
        'occurrences': [EVENT5]
    }
}

EXPECTED_LOG19 = {
    '2015-01-01': {
        'position': {
            'quantity': 100,
            'price': 10
        },
        'occurrences': [DAYTRADE2, OPERATION18, EVENT0]
    }
}


EXPECTED_LOG20 = {
    '2015-01-03': {
        'position': {
            'quantity': 100,
            'price': 10
        },
        'occurrences': [EVENT1]
    },
    '2015-01-02': {
        'position': {
            'quantity': 100,
            'price': 10
        },
        'occurrences': [OPERATION1]
    },
    '2015-01-01': {
        'position': {
            'quantity': 0,
            'price': 0
        },
        'occurrences': [DAYTRADE2]
    }
}

EXPECTED_LOG21 = {
    '2015-01-02': {
        'position': {
            'quantity': 100,
            'price': 10
        },
        'occurrences': [OPERATION1, DAYTRADE3, EVENT2]
    },
    '2015-01-01': {
        'position': {
            'quantity': 0,
            'price': 0
        },
        'occurrences': [DAYTRADE2]
    }
}

EXPECTED_LOG22 = {
    '2015-01-01': {
        'position': {
            'quantity': 100,
            'price': 10
        },
        'occurrences': [DAYTRADE0, OPERATION18]
    }
}

EXPECTED_LOG23 = {
    '2015-01-02': {
        'position': {
            'quantity': 100,
            'price': 10
        },
        'occurrences': [OPERATION1]
    },
    '2015-01-01': {
        'position': {
            'quantity': 0,
            'price': 0
        },
        'occurrences': [DAYTRADE0]
    }
}


EXPECTED_LOG24 = {
    '2015-01-02': {
        'position': {
            'quantity': 100,
            'price': 10
        },
        'occurrences': [OPERATION1, DAYTRADE1]
    },
    '2015-01-01': {
        'position': {
            'quantity': 0,
            'price': 0
        },
        'occurrences': [DAYTRADE0]
    }
}
