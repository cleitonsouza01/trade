"""events: A default set of events for the trade module.

This plugin provides a standard set of events for the trade module.
Events are passed to Accumulator objects to change their position.

It contains the definitions of:
- StockSplit
- ReverseStockSplit

You may use the default events in your application or use them as a
base to create your own events.

License: MIT
http://trade.readthedocs.org/
https://github.com/rochars/trade

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

from ..trade import Event, average_price


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


class BonusShares(Event):
    """Bonus shares."""

    def __init__(self, asset, date, factor):
        self.factor = factor
        self.asset = asset
        self.date = date

    def update_portfolio(self, quantity, price, results):
        new_quantity = quantity * self.factor
        price = average_price (quantity, price, new_quantity, 0)
        quantity += new_quantity
        return quantity, price
