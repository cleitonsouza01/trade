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
        symbol: A string representing the symbol of the subject.
        name: A string representing the name of the subject.
        expiration_date: A string 'YYYY-mm-dd' representing the
            expiration date of the subject, if any.
        default_state: a dictionary with the default state
            of this subject.
    """

    default_state = {}

    def __init__(self, symbol=None, name=None, expiration_date=None):
        self.symbol = symbol
        self.name = name
        self.expiration_date = expiration_date

    def get_default_state(self):
        """Should set the default state of the Accumulator.

        Every time an Accumulator object is created it calls this
        method from the Asset object it is accumulating data from.
        """
        return copy.deepcopy(self.default_state)

    def expire(self, accumulator):
        """Updates the accumulator with the expiration of this subject."""
        accumulator.state = copy.deepcopy(self.default_state)


class Occurrence(object):
    """An occurrence with an subject in a date.

    This is a base class for any occurrence. An occurrence is
    anything that interferes with an subject accumulation, like
    a purchase or sale operation of the subject or a stock split.

    Attributes:
        subject: An Asset object.
        date: A string 'YYYY-mm-dd'.
    """

    def __init__(self, subject, date):
        self.subject = subject
        self.date = date

    def update_portfolio(self, portfolio):
        """Should udpate the portfolio data."""
        pass

    def update_accumulator(self, accumulator):
        """Should udpate the accumulator data."""
        pass


class Accumulator(object):
    """An accumulator of occurrences with an subject.

    It can accumulate a series of occurrence objects and update its
    state based on the occurrences it accumulates.

    The update of the accumulator object state is responsibility
    of the occurrence it accumulates.

    It accumualates occurrences of a single subject.

    Attributes:
        subject: An subject instance, the subject whose data are being
            accumulated.
        date: A string 'YYYY-mm-dd' representing the date of the last
            status change of the accumulator.
        state: A dictionary with the state of this accumulator.
        logging: A boolean indicating if the accumulator should log
            the data passed to accumulate().
        log: A dict with all the occurrences performed with the subject,
            provided that self.logging is True.
    """

    def __init__(self, subject, state=None, logging=False):
        if state:
            self.state = copy.deepcopy(state)
        else:
            self.state = subject.get_default_state()
        self.subject = subject
        self.logging = logging
        self.date = None
        self.log = {}

    def accumulate(self, occurrence):
        """Accumulates an occurrence."""
        occurrence.update_accumulator(self)
        if self.logging:
            self.log_occurrence(occurrence)

    def log_occurrence(self, operation):
        """Log the state of the accumulator.

        If logging, this method is called behind the scenes every
        time accumulate() is called. The states are logged by day
        like this:
        {
            'YYYY-mm-dd': {},
            ...
        }
        """
        self.log[operation.date] = copy.deepcopy(self.state)


class Portfolio(object):
    """A portfolio of subjects.

    A portfolio is a collection of Accumulator objects.
    It receives Occurrence objects and update its accumulators
    with them.

    Attributes:
        subjects: A dict {Asset.symbol: Accumulator}.
    """

    def __init__(self):
        self.subjects = {}

    def accumulate(self, occurrence):
        """Accumulate an occurrence on its corresponding accumulator."""
        occurrence.update_portfolio(self)
        self.accumulate_occurrence(occurrence)

    def accumulate_occurrence(self, occurrence):
        """Accumulates an occurrence on its corresponding accumulator."""
        if occurrence.subject.symbol not in self.subjects:
            self.subjects[occurrence.subject.symbol] = Accumulator(
                occurrence.subject
            )
        self.subjects[occurrence.subject.symbol].accumulate(occurrence)
