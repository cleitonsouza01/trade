"""trade_tools: Tools To Work With Financial Data.

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

from __future__ import absolute_import

import math


def daytrade_condition(trade_a, trade_b):
	"""Check if two trades configure a daytrade."""
	return (
		trade_a.asset == trade_b.asset and
		not same_sign(trade_a.quantity, trade_b.quantity) and
		trade_a.quantity != 0 and
		trade_b.quantity != 0
	)


def calc_average_price(quantity_1, price_1, quantity_2, price_2):
    """Calculate the average price between two positions.

	A position is the quantity of an asset and its unitary average price.
    """
    return (quantity_1 * price_1 + quantity_2 * price_2) / \
			(quantity_1 + quantity_2)


def same_sign(x, y):
    """Check if two numbers have the same sign."""
    return x == math.copysign(x, y)
