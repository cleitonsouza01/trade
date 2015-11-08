"""events: A default set of events for the trade module.

This plugin provides a standard set of events for the trade module.
Events are subclasses of trade.Occurrence. They are passed to
Accumulator and Porfolio objects to change asset accumulation data.

It contains the definitions of:
- Event
- StockSplit
- ReverseStockSplit
- BonusShares

Events can be accumulated by Portfolio objects just like any other
occurrence. Just like any other Occurrence subclass, each event must
for implement a update_container() method that receives a
trade.Accumulator object. This method will contain the logic for the
update on the accumulator data.

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
        super(Event, self).__init__(asset, date)
        self.factor = factor


class StockSplit(Event):
    """A stock split.

    This class represents both stock splits and reverse stock splits.
    Stock splits are represented by values greater than 1.
    Reverse stock splits are represented by values between 0 and 1.
    """

    def update_accumulator(self, container):
        """Performs a split or a reverse split on the stock."""
        container.state['quantity'] = container.state['quantity'] * self.factor
        container.state['price'] = container.state['price'] / self.factor


class BonusShares(Event):
    """Bonus shares."""

    def update_accumulator(self, container):
        """Add stocks received as bonus shares do the accumulator."""
        new_quantity = container.state['quantity'] * self.factor
        container.state['price'] = average_price(
            container.state['quantity'], container.state['price'],
            new_quantity, 0
        )
        container.state['quantity'] += new_quantity
