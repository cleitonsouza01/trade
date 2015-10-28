"""A set of logs for the accumulator tests."""

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
        'quantity': 0,
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
