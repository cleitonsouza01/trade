"""events: A default set of events for the trade module.

This plugin provides a standard set of events for the trade module.
Events are passed to Accumulator objects to change their position.

It contains the definitions of:
- StockSplit
- ReverseStockSplit
- BonusShares

You may use the default events in your application or use them as a
base to create your own events.

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

from __future__ import absolute_import

from abc import ABCMeta

from ..trade import Occurrence
from ..utils import average_price


class Event(Occurrence):
    """An occurrence that change one or more asset's position.

    This is a base class for Events. Events can change the quantity,
    the price and the results stored on a asset accumulator.

    Attributes:
        date: A string 'YYYY-mm-dd', the date the event occurred.
        asset: The target asset of the event.
    """

    __metaclass__ = ABCMeta

    def __init__(self, asset, date, factor):
        self.factor = factor
        super(Event, self).__init__(asset, date)

    def update_container(self, container):
        raise NotImplementedError


class StockSplit(Event):
    """A stock split.

    This class represents both stock splits and reverse stock splits.
    Stock splits are represented by values greater than 1.
    Reverse stock splits are represented by values between 0 and 1.
    """

    def update_container(self, container):
        container.quantity = container.quantity * self.factor
        container.price = container.price / self.factor


class BonusShares(Event):
    """Bonus shares."""

    def update_container(self, container):
        new_quantity = container.quantity * self.factor
        container.price = average_price(
            container.quantity,
            container.price,
            new_quantity,
            0
        )
        container.quantity += new_quantity
