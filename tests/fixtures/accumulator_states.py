"""A set of states for the accumulator tests."""

STATE01 = {
    'quantity': 10,
    'price': 1
}
STATE02 = {
    'quantity': 20,
    'price': 1.5
}
STATE03 = {
    'quantity': 20,
    'price': 2
}
STATE04 = {
    'quantity': 40,
    'price': 3
}
STATE05 = {
    'quantity': 60,
    'price': 3
}
STATE06 = {
    'quantity': 0,
    'price': 0
}
STATE07 = {
    'quantity': 20,
    'price': 8
}
STATE08 = {
    'quantity': 30,
    'price': 7.833333333333333
}

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
    'price': 3.3333333333333335,
    'results': {'trades': 1200},
}
EXPECTED_STATE22 = {
    'quantity': 150,
    'price': 6.666666666666667,
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
