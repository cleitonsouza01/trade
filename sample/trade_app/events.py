"""Some sample events.

http://trade.readthedocs.org/
https://github.com/rochars/trade
License: MIT

This plugin provides a standard set of events for the trade module.
Events are subclasses of the Occurrence class. They are passed to
Accumulator and Porfolio objects to change asset data.

It contains the definitions of:
- Event
- StockSplit
- BonusShares


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

from trade.trade import Event
from trade.utils import average_price


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
