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

from abc import ABCMeta, abstractmethod

from .utils import average_price, same_sign



class Accumulator:
    """An accumulator of quantity @ some average price.

    Attributes:
        asset = An asset instance.
        date = A string 'YYYY-mm-dd' representing the date of the last
            status change of the accumulator
        quantity = The asset's accumulated quantity.
        price = The asset's average unitary price for the quantity
            accumulated.
        results = A dict with the total results from from the
            operations accumulated by the accumulator.
        log_operations = A boolean indicating if the accumulator should
            log the calls to the accumulate() method.
        log = A dict with all the operations performed with the asset,
            provided that self.log_operations is True.

    if created with log_operations=True the accumulator will keep a
    log of the data of every operation it accumulate.

    Results are calculated by the accumulator according to the value
    of the operations informed and the accumulator current status of
    the accumulator (the current quantity and average price of the
    asset).

    The method accumulate() can take a optional param 'results', a dict
    with other results to be included on the accumulator results dict
    and on the operation log.
    """

    def __init__(self, asset, initial_status=None, log_operations=False):
        """Create a instance of the accumulator.

        A initial status (quantity, average price and results) can be
        informed by passing a initial_status param like this:

            initial_status = {
                'date': 'YYYY-mm-dd'
                'quantity': float
                'price': float
                'results': {
                    'result name': float,
                    ...
                }
            }

        The log_operations param is by default set to False; the
        accumulator will not log any operation, just accumulate the
        quantity and results and calculate the average unitary price of
        the asset after each call to self.accumulate().

        If log_operations is set to True, then the accumulator will
        log the data informed on every call to self.accumulate().
        """
        self.asset = asset
        if initial_status:
            self.date = initial_status['date']
            self.quantity = initial_status['quantity']
            self.price = initial_status['price']
            self.results = initial_status['results']
        else:
            self.date = None
            self.quantity = 0
            self.price = 0
            self.results = {
                'trades': 0
            }
        self.log_operations = log_operations
        self.log = {}

    def log_operation(self, quantity, price, date, results):
        """Log operation data.

        If self.log_operations is True then this method is callled
        behind the scenes every time the method accumulate() is called.
        The operations are logged like this:

            self.log = {
                '2017-09-19': {
                    'position': {
                        'quantity': float
                        'price': float
                    }
                    'operations': [
                        {
                            'quantity': float,
                            'price': float,
                            'results': {
                                'result name': float
                            }
                        },
                        ...
                    ],
                },
                ...
            }
        """

        # If the date is not present in the dict keys,
        # a new key created.
        if date not in self.log:
            self.log[date] = {'operations': []}

        # Log the accumulator status and operation data
        self.log[date]['position'] = {
            'quantity': self.quantity,
            'price': self.price,
        }
        self.log[date]['operations'].append(
            {
                'quantity': quantity,
                'price': price,
                'results': results,
            }
        )

    def accumulate(self, quantity, price, date=None, results=None):
        """Accumulate trade data to the existing position.

        The method accumulate() can take a optional param 'results',
        a dict with other results to be included on the accumulator
        results dict.

        For example, if in 2015-09-19 you had 100 of *something* at the
        price of $10.45, and then proceeded to buy 10 more for 10
        dollars, then sold 10 on the same day for 20 dollars, you had a
        result related to this stock, but not a change in position. In
        this case you would call the accumulate() method like this:

            accumulator.accumulate(
                date='2015-09-19',
                results={
                    'daytrade': 100
                }
            )

        The result dict passed to this method must obey the format:

            results = {
                'result name': float
            }

        The accumulator take care of adding the custom results to the
        total results of the stock on its own results attribute, wich
        is a dict like this:

            self.results = {
                'result name': float,
                ...
            }

        The custom results will also be logged, if logging.
        """

        new_quantity = self.quantity + quantity

        if results is None:
            results = {'trades': 0}

        # if the quantity of the operation has the same sign
        # of the accumulated quantity then we need to
        # find out the new average price of the asset
        if same_sign(self.quantity, quantity):

            # if the new quantity is zero, then the new average
            # price is also zero; otherwise, we need to calc the
            # new average price
            if new_quantity:
                new_price = average_price(
                                self.quantity,
                                self.price,
                                quantity,
                                price
                            )
            else:
                new_price = 0

        # If the traded quantity has an opposite sign of the
        # asset's accumulated quantity and the accumulated
        # quantity is not zero, then there was a result.
        elif self.quantity != 0:

            # If the new accumulated quantity is of the same sign
            # of the old accumulated quantity, the average of price
            # will not change.
            if same_sign(self.quantity, new_quantity):
                new_price = self.price

            # If the new accumulated quantity is of different
            # sign of the old accumulated quantity then the
            # average price is now the price of the operation
            else:
                new_price = price

            # calculate the result of this operation and add
            # the new result to the accumulated results
            results['trades'] += abs(quantity)*price - abs(quantity)*self.price

        # If the accumulated quantity was zero then
        # there was no result and the new average price
        # is the price of the operation
        else:
            new_price = price

        # update the accumulator quantity and average
        # price with the new values
        self.quantity = new_quantity
        if new_quantity:
            self.price = new_price
        else:
            self.price = 0

        # add whatever result was informed with or generated
        # by this operation to the accumulator results dict
        for key, value in results.items():
            if key not in self.results:
                self.results[key] = 0
            self.results[key] += value

        # log the operation, if logging
        if self.log_operations:
            self.log_operation(quantity, price, date, results)

    def accumulate_operation(self, operation):
        """Interface to accumulate() that accepts an Operation object."""
        self.accumulate(
            operation.quantity,
            operation.real_price,
            date=operation.date
        )

    def accumulate_event(self, event):
        """Receive and event instance and let it do its work.

        An event can change the quantity, price and results  stored in
        the accumulator.

        The way it changes the position is up to the event object; each
        event object must implement a

            update_portfolio(quantity, price, results)
                return quantity, price

        method that implements the logic of the change in the
        portfolio.
        """
        self.quantity, self.price = event.update_portfolio(
                                            self.quantity,
                                            self.price,
                                            self.results
                                    )


class Event:
    """A portfolio-changing event.

    Events can change the quantity, the price and the results stored in
    the accumulator. This is a base class for Events; every event must
    inherit from this class and have a

        update_portfolio(quantity, price, results)
            return quantity, price

    method that implements the logic of the change in the portfolio.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def update_portfolio(quantity, price, results):
        return quantity, price
