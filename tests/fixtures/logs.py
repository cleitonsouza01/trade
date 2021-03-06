"""A set of logs for the accumulator tests."""

from .accumulator_states import (
    EXPECTED_STATE1, EXPECTED_STATE9, EXPECTED_STATE7, EXPECTED_STATE10,
    EXPECTED_STATE11, EXPECTED_STATE25, EXPECTED_STATE2, EXPECTED_STATE23,
    EXPECTED_STATE24, EXPECTED_STATE12, EXPECTED_STATE3,
    EXPECTED_STATE13, EXPECTED_STATE4, EXPECTED_STATE5, EXPECTED_STATE6,
    EXPECTED_STATE8
)

EXPECTED_LOG0 = {
    '2015-01-02': EXPECTED_STATE1,
    '2015-01-01': EXPECTED_STATE9
}

EXPECTED_LOG1 = {
    '2015-01-03': EXPECTED_STATE9,
    '2015-01-02': EXPECTED_STATE1,
    '2015-01-01': EXPECTED_STATE9
}

EXPECTED_LOG2 = {
    '2015-01-04': EXPECTED_STATE7,
    '2015-01-03': EXPECTED_STATE9,
    '2015-01-02': EXPECTED_STATE1,
    '2015-01-01': EXPECTED_STATE9
}

EXPECTED_LOG3 = {
    '2015-01-05': EXPECTED_STATE10,
    '2015-01-04': EXPECTED_STATE7,
    '2015-01-03': EXPECTED_STATE9,
    '2015-01-02': EXPECTED_STATE1,
    '2015-01-01': EXPECTED_STATE9
}

EXPECTED_LOG4 = {
    '2015-01-06': EXPECTED_STATE11,
    '2015-01-05': EXPECTED_STATE10,
    '2015-01-04': EXPECTED_STATE7,
    '2015-01-03': EXPECTED_STATE9,
    '2015-01-02': EXPECTED_STATE1,
    '2015-01-01': EXPECTED_STATE9
}

EXPECTED_LOG5 = {
    '2015-01-06': EXPECTED_STATE12,
    '2015-01-05': EXPECTED_STATE10,
    '2015-01-04': EXPECTED_STATE7,
    '2015-01-03': EXPECTED_STATE9,
    '2015-01-02': EXPECTED_STATE1,
    '2015-01-01': EXPECTED_STATE9
}

EXPECTED_LOG6 = {
    '2015-01-02': EXPECTED_STATE13,
    '2015-01-01': {
        'quantity': 50,
        'price': 10,
        'results': {},
    },

}

EXPECTED_LOG7 = {
    '2015-01-02': EXPECTED_STATE1,
    '2015-01-01': EXPECTED_STATE2
}

EXPECTED_LOG8 = {
    '2015-01-03': EXPECTED_STATE2,
    '2015-01-02': EXPECTED_STATE1,
    '2015-01-01': EXPECTED_STATE2
}

EXPECTED_LOG9 = {
    '2015-01-05': EXPECTED_STATE4,
    '2015-01-04': EXPECTED_STATE3,
    '2015-01-03': EXPECTED_STATE2,
    '2015-01-02': EXPECTED_STATE1,
    '2015-01-01': EXPECTED_STATE2
}

EXPECTED_LOG10 = {
    '2015-01-06': EXPECTED_STATE5,
    '2015-01-05': EXPECTED_STATE4,
    '2015-01-04': EXPECTED_STATE3,
    '2015-01-03': EXPECTED_STATE2,
    '2015-01-02': EXPECTED_STATE1,
    '2015-01-01': EXPECTED_STATE2
}

EXPECTED_LOG11 = {
    '2015-01-04': EXPECTED_STATE3,
    '2015-01-03': EXPECTED_STATE2,
    '2015-01-02': EXPECTED_STATE1,
    '2015-01-01': EXPECTED_STATE2
}

EXPECTED_LOG12 = {
    '2015-01-06': EXPECTED_STATE6,
    '2015-01-05': EXPECTED_STATE4,
    '2015-01-04': EXPECTED_STATE3,
    '2015-01-03': EXPECTED_STATE2,
    '2015-01-02': EXPECTED_STATE1,
    '2015-01-01': EXPECTED_STATE2
}

EXPECTED_LOG13 = {
    '2015-01-02': EXPECTED_STATE8,
    '2015-01-01': {
        'quantity': -50,
        'price': 20,
        'results': {},
    },
}

EXPECTED_LOG14 = {
    '2015-01-02': EXPECTED_STATE7,
    '2015-01-01': {
        'quantity': -100,
        'price': 20,
        'results': {},
    },
}

EXPECTED_LOG15 = {
    '2015-01-01': EXPECTED_STATE9
}

EXPECTED_LOG16 = {
    '2015-01-01': EXPECTED_STATE25
}

EXPECTED_LOG19 = {
    '2015-01-01': EXPECTED_STATE23
}

EXPECTED_LOG20 = {
    '2015-01-03': EXPECTED_STATE23,
    '2015-01-02': EXPECTED_STATE23,
    '2015-01-01': EXPECTED_STATE25
}

EXPECTED_LOG21 = {
    '2015-01-02': EXPECTED_STATE24,
    '2015-01-01': EXPECTED_STATE25
}

EXPECTED_LOG23 = {
    '2015-01-02': EXPECTED_STATE23,
    '2015-01-01': EXPECTED_STATE25
}
