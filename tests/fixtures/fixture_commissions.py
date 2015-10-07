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
    'brokerage': 2,
    'some tax': 1.5,
    'other tax': 1,
}
