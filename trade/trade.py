"""trade: Tools For Stock Trading Applications.

trade is Python framework to ease the development of investment
management applications. It is focused in, but not limited to,
stock exchange markets.

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

import copy


class Subject(object):
    """A subject of an occurrence.

    Attributes:
        name: A string representing the name of the asset.
        symbol: A string representing the symbol of the asset.
        expiration_date: A string 'YYYY-mm-dd' representing the
            expiration date of the asset, if any.
        default_state: a dictionary with the default state
            of this subject.
    """

    default_state = {}

    def __init__(self, name=None, symbol=None, expiration_date=None):
        self.name = name
        self.symbol = symbol
        self.expiration_date = expiration_date

    def get_default_state(self):
        """Should set the default state of the Accumulator.

        Every time an Accumulator object is created it calls this
        method from the Asset object it is accumulating data from.
        """
        return copy.deepcopy(self.default_state)

    def expire(self, accumulator):
        """Updates the accumulator with the expiration of this subject."""
        accumulator.data = copy.deepcopy(self.default_state)


class Occurrence(object):
    """An occurrence with an asset in a date.

    This is a base class for any occurrence. An occurrence is
    anything that interferes with an asset accumulation, like
    a purchase or sale operation of the asset or a stock split.

    Attributes:
        asset: An Asset object.
        date: A string 'YYYY-mm-dd'.
    """

    def __init__(self, asset, date):
        self.asset = asset
        self.date = date

    def update_portfolio(self, portfolio):
        """Should udpate the portfolio data."""
        pass

    def update_accumulator(self, accumulator):
        """Should udpate the accumulator data."""
        pass


class Accumulator(object):
    """An accumulator of occurrences with an asset.

    It can accumulate a series of occurrence objects and update its
    state based on the occurrences it accumulates.

    The update of the accumulator object state is responsibility
    of the occurrence it accumulates.

    It accumualates occurrences of a single asset.

    Attributes:
        asset: An asset instance, the asset whose data are being
            accumulated.
        date: A string 'YYYY-mm-dd' representing the date of the last
            status change of the accumulator.
        data: A dictionary with the state of this accumulator. The
            state is updated according to the accumulation of
            occurrences.
        logging: A boolean indicating if the accumulator should log
            the data passed to accumulate().
        log: A dict with all the operations performed with the asset,
            provided that self.logging is True.
    """

    def __init__(self, asset, logging=False):
        self.asset = asset
        self.logging = logging
        self.date = None
        self.data = asset.get_default_state()
        self.log = {}

    def accumulate(self, occurrence):
        """Accumulates an occurrence to the existing position."""
        occurrence.update_accumulator(self)
        if self.logging:
            self.log_occurrence(occurrence)

    def log_occurrence(self, operation):
        """Log Operation, Daytrade and Event objects.

        If logging, this method is called behind the scenes every
        time accumulate() is called. The occurrences are logged
        like this:
        {
            'YYYY-mm-dd': {
                'data': {}
                'occurrences': [operation, ...],
            },
            ...
        }
        """
        if operation.date not in self.log:
            self.log[operation.date] = {'occurrences': []}
        self.log[operation.date]['data'] = copy.deepcopy(self.data)
        self.log[operation.date]['occurrences'].append(operation)


class Portfolio(object):
    """A portfolio of assets.

    A portfolio is a collection of Accumulator objects.
    It can receive Occurrence subclass objects and update the
    its accumulators with them.

    Attributes:
        assets: A dict {Asset.symbol: Accumulator}.
    """

    def __init__(self):
        self.assets = {}

    def accumulate(self, occurrence):
        """Accumulate an operation on its corresponding accumulator."""
        occurrence.update_portfolio(self)
        self.accumulate_occurrence(occurrence)

    def accumulate_occurrence(self, occurrence):
        """Accumulates an occurrence on its corresponding accumulator."""
        if occurrence.asset.symbol not in self.assets:
            self.assets[occurrence.asset.symbol] = Accumulator(
                occurrence.asset
            )
        self.assets[occurrence.asset.symbol].accumulate(occurrence)
