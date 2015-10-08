"""Operations.

This module provides the default funciontalities related to purchase
and sale operations of assets for the trade module.

It is part of the trade framework core, but implemented just like a
plugin.

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
from __future__ import division

from abc import ABCMeta, abstractmethod
import math
import copy

from .utils import average_price, same_sign, merge_operations

from .trade import Occurrence


class Operation(Occurrence):
    """An operation represents the purchase or the sale of an asset.

    Attributes:
        date: A string 'YYYY-mm-dd', the date the operation occurred.
        asset: An Asset instance, the asset that is being traded.
        quantity: A number representing the quantity being traded.
            Positive quantities represent a purchase.
            Negative quantities represent a sale.
        price: The raw unitary price of the asset being traded.
        commissions: A dict of discounts. String keys and float values
            representing the name of the discounts and the values
            to be deducted added to the the operation value.
        fees: A dict of fees. string keys and float values
            representing the names of the fees and the values of the
            fees to be applied to the operation. Fee values are
            always represented as a percentage. Fees are applied
            based on the volume of the operation.
        update_position: A boolean indication if the operation should
            update the position of the accumulator or not.
        update_results: A boolean indication if the operation should
            update the results of the accumulator or not.
        operations: A list of underlying occurrences that the
            might may have.
    """

    # By default every operation update
    # accumulator position; this can be
    # changed on-spot if needed
    update_position = True

    # By default every operation update
    # accumulator results; this can be
    # changed on-spot if needed
    update_results = True

    def __init__(self, asset=None, date=None, quantity=0, price=0):
        super(Operation, self).__init__(asset, date)
        self.quantity = quantity
        self.price = price
        self.commissions = {}
        self.fees = {}
        self.raw_results = {}
        self.operations = []

    @property
    def results(self):
        """Return the results associated with the operation."""
        return self.raw_results

    @property
    def real_value(self):
        """Returns the quantity * the real price of the operation."""
        return self.quantity * self.real_price

    @property
    def real_price(self):
        """Returns the real price of the operation.

        The real price is the price with all commissions and fees
        already deducted or added.
        """
        return self.price + math.copysign(
            self.total_commissions_and_fees / self.quantity,
            self.quantity
        )

    @property
    def total_commissions_and_fees(self):
        """Returns the sum of all commissions and fees."""
        return self.total_commissions + self.total_fees_value

    @property
    def total_commissions(self):
        """Return the sum of all commissions of this operation."""
        return sum(self.commissions.values())

    @property
    def volume(self):
        """Returns the quantity of the operation * its raw price."""
        return abs(self.quantity) * self.price

    @property
    def total_fees_value(self):
        """Returns the total fee value for this operation."""
        return sum(
            [self.volume * value / 100  for value in self.fees.values()]
        )

    def update_accumulator(self, accumulator):
        """Update the accumulator status with the operation data."""
        # Update the state of the accumulator with
        # this operation data
        self.update_positions(accumulator)

        # Add whatever result was informed with or generated
        # by this operation to the accumulator results dict
        if self.update_results:
            self.update_accumulator_results(accumulator)

    def update_accumulator_results(self, accumulator):
        """Update the results stored in the accumulator."""
        if 'results' not in accumulator.data:
            accumulator.data['results'] = {}
        for key, value in self.results.items():
            if key not in accumulator.data['results']:
                accumulator.data['results'][key] = 0
            accumulator.data['results'][key] += value

    def update_positions(self, accumulator):
        """Update the position of the asset with the Operation data."""

        # Here we check if the operation asset is the same
        # asset of this Accumulator object; the accumulator
        # only accumulates operations that trade its asset.
        # We also check if the operation should update the
        # position; if all this conditions are met, then
        # the position is updated.
        update_position_condition = (
            self.asset.symbol == accumulator.asset.symbol and
            self.quantity
        )
        if update_position_condition:

            # Assure the accumulator data dict
            # has the needed keys
            if 'quantity' not in accumulator.data:
                accumulator.data['quantity'] = 0
            if 'price' not in accumulator.data:
                accumulator.data['price'] = 0

            # Define the new accumualtor quantity
            new_quantity = accumulator.data['quantity'] + self.quantity

            # if the quantity of the operation has the same sign
            # of the accumulated quantity then we need to
            # find out the new average price of the asset
            if same_sign(accumulator.data['quantity'], self.quantity):
                accumulator.data['price'] = average_price(
                    accumulator.data['quantity'],
                    accumulator.data['price'],
                    self.quantity,
                    self.real_price
                )

            # If the traded quantity has an opposite sign of the
            # asset's accumulated quantity and the accumulated
            # quantity is not zero, then there was a result.
            elif accumulator.data['quantity'] != 0:

                # check if we are trading more than what
                # we have on our portfolio; if yes,
                # the result will be calculated based
                # only on what was traded (the rest create
                # a new position)
                if abs(self.quantity) > abs(accumulator.data['quantity']):
                    result_quantity = accumulator.data['quantity'] * -1

                # If we're not trading more than what we have,
                # then use the operation quantity to calculate
                # the result
                else:
                    result_quantity = self.quantity

                # calculate the result of this operation and add
                # the new result to the accumulated results
                results = \
                    result_quantity * accumulator.data['price'] - \
                    result_quantity * self.real_price
                if results:
                    self.results['trades'] = results

                # If the new accumulated quantity has a different
                # sign of the old accumulated quantity then the
                # average price is now the price of the operation
                # If the new accumulated quantity is of the same sign
                # of the old accumulated quantity, the average of price
                # will not change.
                if not same_sign(accumulator.data['quantity'], new_quantity):
                    accumulator.data['price'] = self.real_price

            # If the accumulated quantity was zero then
            # there was no result and the new average price
            # is the price of the operation
            else:
                accumulator.data['price'] = self.real_price

            # update the accumulator quantity
            # with the new quantity
            accumulator.data['quantity'] = new_quantity

            # If the accumulator is empty
            # the price is set back to zero
            if not accumulator.data['quantity']:
                accumulator.data['price'] = 0


class OperationContainer(object):
    """A container for operations.

    An OperationContainer is used to group operations that occurred on
    the same date and then perform tasks on them.

    The main task task of the OperationContainer is to fetch the
    resulting positions from a group of Operations.

    This is achieved by calling this method:

        fetch_positions()

    Every time fetch_positions() is called the OperationContainer
    execute this tasks behind the scenes:

    - Execute all tasks defined in self.tasks. By default, no task is
      listed. Tasks are functions like this:

            def some_task(container)

      that receive an OperationContainer object and perform some work
      on the container data.

    - Create positions in self.positions for all operations in
      the container. Positions are all the operations with the same
      asset grouped in a single operation.

    - Prorate the commissions, if any, proportionally for all positions
      by calling:

        prorate_commissions()

    - Find the fees, if any, for the positions by calling:

        find_fees_for_positions()

    Attributes:
        date: A string 'YYYY-mm-dd' representing the date of the
            operations on the container.
        operations: A list of Operation instances.
        commissions: A dict with discount names and values to be
            deducted from the operations.
        positions: a dict of positions with this format:
            self.positions = {
                'position type': {
                    Asset.symbol: Operation,
                    ...
                },
                ...
            }
        tasks: a list of functions. The functions will
            be called in the order they are defined in this list when
            fetch_positions() is called. Every listed function must
            receive a OperationContainer object. They are like this:
                def some_task(container):
                    #do some stuff with container...
            The functions may change the Operation objects in
            self.operations, if needed (like when you separate
            daytrades from other operations).
    """

    volume = 0

    def __init__(self, operations=None, commissions=None):
        if operations is None:
            operations = []
        if commissions is None:
            commissions = {}
        self.operations = operations
        self.commissions = commissions
        self.trading_fees = TradingFees
        self.positions = {}
        self.tasks = []

    @property
    def total_commission_value(self):
        """Returns the sum of the values of all commissions."""
        return sum(self.commissions.values())

    def fetch_positions(self):
        """Fetch the positions resulting from the operations.

        This method executes all the methods defined in self.tasks
        in the order they are listed.

        Then it reads the self.operations list and add any remaining
        operation to the self.positions.

        And finally it checks if there are any fees to be applied
        to the positions.
        """
        self.volume = sum(operation.volume for operation in self.operations)

        raw_operations = copy.deepcopy(self.operations)

        # Execute all defined tasks
        for task in self.tasks:
            task(self)

        # fetch the positions from the remaining operations
        for operation in self.operations:
            if operation.quantity != 0:
                self.add_to_position_operations(operation)

        # Add fees to the operations
        self.find_trading_fees_for_positions()

        self.operations = raw_operations

    def add_to_position_operations(self, operation):
        """Adds an operation to the common operations list."""
        if 'operations' not in self.positions:
            self.positions['operations'] = {}
        if operation.asset.symbol in self.positions['operations']:
            merge_operations(
                self.positions['operations'][operation.asset.symbol],
                operation
            )
        else:
            self.positions['operations'][operation.asset.symbol] = operation

    def find_trading_fees_for_positions(self):
        """Finds the fees for all positions in the container."""
        for position_type, position_value in self.positions.items():
            for position in position_value.values():
                if position.operations:
                    for operation in position.operations:
                        operation.fees = self.trading_fees.get_fees(
                            operation, position_type
                        )
                else:
                    position.fees = self.trading_fees.get_fees(
                        position, position_type
                    )


class TradingFees(object):
    """Responsible for finding fees for an operation.

    A TradingFees class returns the correspondent percentual fee for
    an Operation. This base TaxManager implements a dummy interface
    that will return a empty set of fees every time it is called.

    Every OperationContainer has a reference to this class. If you
    need to implement fees in your application you must create your
    own TradingFees implementation and then replace the reference in
    the OperationContainer object by doing this:

        container.trading_fees = YourTradingFees

    Your TradingFees implementation must obey this class interface.
    """

    __metaclass__ = ABCMeta

    @classmethod
    @abstractmethod
    def get_fees(cls, operation=None, operation_type=None):
        """Returns a set of fees (percentages) for a given operation."""
        return {}
