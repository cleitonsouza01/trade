"""trade: Tools For Stock Trading Applications.

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


class Event:
    """A portfolio-changing event.

    Events can change the quantity, the price and the results stored in
    the accumulator. This is a base class for Events; every event must
    inherit from this class and have a method like this:

        update_portfolio(quantity, price, results)
            # do stuff here...
            return quantity, price

    that implements the logic for the change in the portfolio.

    Events must have an "asset" attribute with reference to an Asset
    instance and a date 'YYYY-mm-dd' attribute.
    """

    def __init__(self, asset, date):
        self.asset = asset
        self.date = date

    def update_portfolio(self, quantity, price, results):
        return quantity, price


class StockSplit(Event):
    """A stock split."""

    def __init__(self, asset, date, factor):
        self.factor = factor
        self.asset = asset
        self.date = date

    def update_portfolio(self, quantity, price, results):
        quantity = quantity * self.factor
        price = price / self.factor
        return quantity, price


class ReverseStockSplit(Event):
    """ A reverse stock split."""

    def __init__(self, asset, date, factor):
        self.factor = factor
        self.asset = asset
        self.date = date

    def update_portfolio(self, quantity, price, results):
        quantity = quantity / self.factor
        price = price * self.factor
        return quantity, price
