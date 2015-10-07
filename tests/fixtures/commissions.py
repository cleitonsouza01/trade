"""Tests the real_price property of Operation objects."""

from __future__ import absolute_import


COMMISSIONS0 = {
    'some discount': 3
}
COMMISSIONS1 = {
    'some discount': 3,
    'other discount': 1
}
COMMISSIONS2 = {
    'some discount': 3,
    'other discount': 1,
    'more discounts': 2
}
COMMISSIONS3 = {
    'some discount': 3,
    'other discount': 1,
    'negative discount': -1
}
COMMISSIONS4 = {
    'some discount': 6
}
COMMISSIONS5 = {
    'some discount': 7,
    'other discount': 1
}
COMMISSIONS6 = {
    'some discount': 10,
    'other discount': 1,
    'more discounts': 2
}
COMMISSIONS7 = {
    'some discount': 5,
    'other discount': 1,
    'negative discount': -1
}
COMMISSIONS8 = {
    'some': 2,
    'other': 1.5,
    'and other': 1,
}
COMMISSIONS9 = {
    'some discount': 2,
    'other discount': 6
}
COMMISSIONS10 = {
    'some discount': 4,
}
COMMISSIONS11 = {
    'some discount': 1,
}
COMMISSIONS12 = {
    'brokerage': 2.3,
    'other': 1
}
COMMISSIONS13 = {
    'some discount': 1,
    'other discount': 3,
}
