"""Accumulator states."""


STATE01 = {
    'quantity': 10,
    'price': 1
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
STATE09 = {
    'quantity': 20,
    'price': 5.5
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
