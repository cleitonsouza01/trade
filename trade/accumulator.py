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
import math

from .utils import average_price, same_sign


class Accumulator:
    """An accumulator of quantity @ some average price.

    Attributes:
        asset: An asset instance, the asset whose data are being
            accumulated.
        date: A string 'YYYY-mm-dd' representing the date of the last
            status change of the accumulator.
        quantity: The asset's accumulated quantity.
        price: The asset's average price for the quantity accumulated.
        results: A dict with the total results from the operations
            accumulated.
        logging: A boolean indicating if the accumulator should log
            the calls to the accumulate() method.
        log: A dict with all the operations performed with the asset,
            provided that self.logging is True.

    if created with logging=True the accumulator will log the every
    operation it accumulates.

    Results are calculated by the accumulator according to the value
    of the operations informed and the current status of the
    accumulator (the current quantity and average price of the asset).
    """

    def __init__(self, asset=None, initial_status=None, logging=False):
        """Creates a instance of the accumulator.

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

        The logging param is by default set to False; the accumulator
        will not log any operation, just accumulate the quantity and
        calculate the average price and results related to the asset
        after each call to accumulate_operation(),
        accumulate_daytrade() and accumulate_event().

        If logging is set to True the accumulator will log the data
        passed on every call to accumulate_operation(),
        accumulate_daytrade() and accumulate_event().
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
                'trades': 0,
                'daytrades': 0
            }
        self.logging = logging
        self.log = {}

    def log_occurrence(self, operation):
        """Log Operation, Daytrade and Event objects.

        If logging, this method is called behind the scenes every
        time the method accumulate() is called. The occurrences are
        logged like this:

            self.log = {
                '2017-09-19': {
                    'position': {
                        'quantity': float
                        'price': float
                    }
                    'occurrences': [Operation, ...],
                },
                ...
            }
        """

        # If the date is not present in the dict keys,
        # a new key created.
        if operation.date not in self.log:
            self.log[operation.date] = {'occurrences': []}

        # Log the accumulator status and operation data
        self.log[operation.date]['position'] = {
            'quantity': self.quantity,
            'price': self.price,
        }

        self.log[operation.date]['occurrences'].append(operation)

    def accumulate_operation(self, operation):
        """Accumulates operation data to the existing position.

        The accumulator takes care of adding any custom results already
        present on the operation "results' attribute to the total
        results of the stock in the accumulator.
        """
        new_quantity = self.quantity + operation.quantity

        if operation.results is None:
            operation.results = {'trades': 0}

        # if the quantity of the operation has the same sign
        # of the accumulated quantity then we need to
        # find out the new average price of the asset
        if same_sign(self.quantity, operation.quantity):

            # if the new quantity is zero, then the new average
            # price is also zero; otherwise, we need to calc the
            # new average price
            if new_quantity:
                new_price = average_price(
                                self.quantity,
                                self.price,
                                operation.quantity,
                                operation.real_price
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
                new_price = operation.real_price

            # check if we are trading more than what
            # we have on our portfolio; if yes,
            # the result will be calculated based
            # only on what was traded (the rest create
            # a new position)
            if abs(operation.quantity) > abs(self.quantity):
                    result_quantity = self.quantity * -1

            # If we're not trading more than what we have,
            # then use the operation quantity to calculate
            # the result
            else:
                result_quantity = operation.quantity

            # calculate the result of this operation and add
            # the new result to the accumulated results
            operation.results['trades'] += \
                result_quantity*self.price - result_quantity*operation.real_price

        # If the accumulated quantity was zero then
        # there was no result and the new average price
        # is the price of the operation
        else:
            new_price = operation.real_price

        # update the accumulator quantity and average
        # price with the new values
        self.quantity = new_quantity
        if new_quantity:
            self.price = new_price
        else:
            self.price = 0

        # add whatever result was informed with or generated
        # by this operation to the accumulator results dict
        for key, value in operation.results.items():
            if key not in self.results:
                self.results[key] = 0
            self.results[key] += value

        # log the operation, if logging
        if self.logging:
            self.log_occurrence(operation)

        return operation.results

    def accumulate_daytrade(self, daytrade):
        """Accumulates a Daytrade operation."""
        self.results['daytrades'] += daytrade.result
        if self.logging:
            self.log_occurrence(daytrade)
        return daytrade.result

    def accumulate_event(self, event):
        """Receives a Event subclass instance and lets it do its work.

        An event can change the quantity, price and results stored in
        the accumulator.

        The way it changes this information is up to the event object;
        each Event subclass must implement a method like this:

            update_portfolio(quantity, price, results)
                # do stuff here...
                return quantity, price

        that have the logic for the change in the accumulator's
        quantity, price and results.
        """
        self.quantity, self.price = event.update_portfolio(
                                            self.quantity,
                                            self.price,
                                            self.results
                                    )
        if self.logging:
            self.log_occurrence(event)


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

    __metaclass__ = ABCMeta

    def __init__(self, asset, date):
        self.asset = asset
        self.date = date

    @abstractmethod
    def update_portfolio(quantity, price, results):
        return quantity, price
