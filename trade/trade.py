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
from __future__ import division

import math
import copy

from .utils import (
    average_price, daytrade_condition, same_sign, find_purchase_and_sale
)


class Asset:
    """An asset represents anything that can be traded.

    Attributes:
        name: A string representing the name of the asset.
    """

    def __init__(self, name=''):
        self.name = name

    def __deepcopy__(self, memo):
        return self


class Operation:
    """An operation represents the purchase or sale of an asset.

    Attributes:
        date: A string 'YYYY-mm-dd', the date the operation occurred.
        asset: An Asset instance, the asset that is being traded.
        quantity: A number representing the quantity being traded.
        price: The raw unitary price of the asset being traded.
        discounts: A dict of discount string names and floar values.
    """

    def __init__(self, quantity, price,
                    date=None, asset=None, discounts=None):
        self.date = date
        self.asset = asset
        self.quantity = quantity
        self.price = price
        if discounts is None: discounts={}
        self.discounts = discounts

    @property
    def real_value(self):
        return abs(self.quantity) * self.real_price

    @property
    def real_price(self):
        return self.price + math.copysign(
                                self.total_discounts / self.quantity,
                                self.quantity
                            )

    @property
    def total_discounts(self):
        return sum(self.discounts.values())

    @property
    def volume(self):
        return abs(self.quantity) * self.price


class OperationContainer:
    """A container for operations.

    A OperationContainer is used to group operations, like operations
    that occurred on the same date, and then perform tasks on them. It
    can:

    - Separate the daytrades and the common operations of a group of
      operations that occurred on the same date by using the method:
      self.identify_daytrades_and_common_operations()

    - Rate a group of taxes proportionally for all daytrades and common
      operations, if any, by using the method:
      self.rate_discounts_by_common_operations_and_daytrades()

    Attributes:
        date: A string 'YYYY-mm-dd' representing the date of the
            operations on the container.
        operations: A list of Operation instances.
        discounts: A dict with discount names and values to be deducted
            from the operations.
        daytrades: a dict of Daytrade objects, indexed by the daytrade
            asset.
        common_operations: a dict of Operation objects, indexed by the
            daytrade asset.
    """

    def __init__(self, date=None, operations=None, discounts=None):
        self.date = date
        if operations is None: operations=[]
        if discounts is None: discounts = {}
        self.operations = operations
        self.discounts = discounts
        self.daytrades = {}
        self.common_operations = {}

    @property
    def total_discount_value(self):
        """Return the sum of values in the container discounts dict."""
        return sum(self.discounts.values())

    @property
    def volume(self):
        """Return the total volume of the operations in the container."""
        return sum(operation.volume for operation in self.operations)

    def rate_discounts_by_daytrades_and_common_operations(self):
        """Rate the TradeContainer discounts by its operations.

        This method sums all discounts on the self.discounts dict. The
        total discount value is then rated proportionally by the
        daytrades and common operations based on their volume.
        """
        for operation in self.common_operations.values():
            self.rate_discounts_by_operation(operation)
        for daytrade in self.daytrades.values():
            self.rate_discounts_by_operation(daytrade.buy)
            self.rate_discounts_by_operation(daytrade.sale)

    def rate_discounts_by_operation(self, operation):
        """Rate the discounts of the container for one operation.

        The rate is based on the container volume and the operation
        volume.
        """
        percent = operation.volume / self.volume * 100
        for key, value in self.discounts.items():
            operation.discounts[key] = value * percent / 100

    def identify_daytrades_and_common_operations(self):
        """Separate operations into daytrades and common operations.

        The original operations list remains untouched. After the
        execution of this method, the container daytrades list and
        common_operations list will be filled with the daytrades
        and common operations found in the container operations list,
        if any.
        """
        operations = copy.deepcopy(self.operations)

        for i, operation_a in enumerate(operations):
            for operation_b in \
                    [
                        op for op in operations[i:] if daytrade_condition(
                                                            op, operation_a
                                                        )
                    ]:
                self.extract_daytrade(operation_a, operation_b)

            if operation_a.quantity != 0:
                self.append_to_common_operations(operation_a)

    def extract_daytrade(self, operation_a, operation_b):
        """Extract the daytrade part of two operations."""

        # Find what is the purchase and what is the sale
        purchase, sale = find_purchase_and_sale(operation_a, operation_b)

        # Find the daytraded quantity; the daytraded
        # quantity is always the smallest absolute quantity
        daytrade_quantity = min([abs(purchase.quantity), abs(sale.quantity)])

        # Update the operations that originated the
        # daytrade with the new quantity after the
        # daytraded part has been extracted; One of
        # the operations will always have zero
        # quantity after this, being fully consumed
        # by the daytrade. The other operation may or
        # may not end with zero quantity.
        purchase.quantity -= daytrade_quantity
        sale.quantity += daytrade_quantity

        # Now that we know everything we need to know
        # about the daytrade, we create the Daytrade object
        daytrade = Daytrade(
            self.date,
            purchase.asset,
            daytrade_quantity,
            purchase.price,
            sale.price
        )

        # If this container already have a Daytrade
        # with this asset, we merge this daytrade
        # with the daytrade in self.daytrades -
        # in the end, there is only one daytrade per
        # asset per OperationContainer.
        if daytrade.asset in self.daytrades:
            self.merge_operations(
                self.daytrades[daytrade.asset].buy,
                daytrade.buy
            )
            self.merge_operations(
                self.daytrades[daytrade.asset].sale,
                daytrade.sale
            )
            self.daytrades[daytrade.asset].quantity += daytrade.quantity
        else:
            self.daytrades[daytrade.asset] = daytrade

    def append_to_common_operations(self, operation):
        """Append a operation to the common operations list."""
        if operation.asset in self.common_operations:
            self.merge_operations(
                self.common_operations[operation.asset],
                operation
            )
        else:
            self.common_operations[operation.asset] = operation

    def merge_operations(self, existing_operation, operation):
        """Merge one operation with another operation."""
        existing_operation.price = average_price(
                                        existing_operation.quantity,
                                        existing_operation.price,
                                        operation.quantity,
                                        operation.price
                                    )
        existing_operation.quantity += operation.quantity


class Daytrade:
    """A daytrade operation.

    Daytrades are operations of purchase and sale of the same asset on
    the same date.

    Attributes:
        asset: An asset instance, the asset that is being traded.
        quantity: The traded quantity of the asset.
        buy: A Operation instance representing the purchase of the
            asset.
        sale: A Operation instance representing the sale of the asset.
    """

    # TODO docstring explaining the creation of the
    #       purchase and sale operations
    def __init__(self, date, asset, quantity, buy_price, sale_price):
        self.date = date
        self.asset = asset
        self.quantity = quantity
        self.buy = Operation(
            date=date,
            asset=asset,
            quantity=quantity,
            price=buy_price
        )
        self.sale = Operation(
            date=date,
            asset=asset,
            quantity=quantity*-1,
            price=sale_price
        )

    @property
    def result(self):
        return self.sale.real_value - self.buy.real_value


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
        # asset's accumulated quantity, then there was a result.
        else:

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
        self.accumulate(
            operation.quantity,
            operation.real_price,
            date=operation.date
        )
