"""Utility functions for the trade module.

trade: Financial Application Framework
http://trade.readthedocs.org/
https://github.com/rochars/trade
License: MIT

Copyright (c) 2015 Rafael da Silva Rocha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from __future__ import division


def merge_operations(existing_operation, operation):
    """Merges two operations."""
    existing_operation.price = average_price(
        existing_operation.quantity,
        existing_operation.price,
        operation.quantity,
        operation.price
    )
    existing_operation.quantity += operation.quantity


def average_price(quantity_1, price_1, quantity_2, price_2):
    """Calculates the average price between two asset states."""
    return (quantity_1 * price_1 + quantity_2 * price_2) / \
            (quantity_1 + quantity_2)


def same_sign(number_1, number_2):
    """Checks if two numbers have the same sign."""
    return (number_1 >= 0) ^ (number_2 < 0)


def daytrade_condition(operation_a, operation_b):
    """Checks if two operations are day trades."""
    return (
        operation_a.subject.symbol == operation_b.subject.symbol and
        not same_sign(operation_a.quantity, operation_b.quantity)
    )


def find_purchase_and_sale(operation_a, operation_b):
    """Finds which operation is a purchase and which is a sale."""
    if operation_b.quantity > operation_a.quantity:
        return operation_b, operation_a
    return operation_a, operation_b
