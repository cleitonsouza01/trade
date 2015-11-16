"""trade: Tools For Trade Management Applications.

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

import math
import copy

from .utils import average_price, same_sign, merge_operations
from accumulator import Occurrence, Subject


class Asset(Subject):
    """An asset represents anything that can be traded."""

    default_state = {
        'quantity': 0,
        'price': 0,
        'results': {}
    }


class Operation(Occurrence):
    """An Operation represents the purchase or sale of an asset.

    Attributes:
        date: A string 'YYYY-mm-dd', the date the operation occurred.
        subject: An Asset instance, the asset that is being traded.
        quantity: A number representing the quantity being traded.
            Positive quantities represent a purchase.
            Negative quantities represent a sale.
        price: The raw unitary price of the asset being traded.
        commissions: A dict of discounts. String keys and float values
            representing the name of the discounts and the values
            to be deducted added to the the operation value.
        operations: A list of underlying occurrences that the
            might may have.
        update_position: A boolean indication if the operation should
            update the position of the accumulator or not.
        update_results: A boolean indication if the operation should
            update the results of the accumulator or not.
    """

    # By default every operation
    # updates the accumulator position
    update_position = True

    # By default every operation
    # updates the accumulator results
    update_results = True

    # By default every operation
    # updates the OperationContainer
    # positions
    update_container = True

    def __init__(self, subject=None, date=None, **kwargs):
        super(Operation, self).__init__(subject, date)
        self.quantity = kwargs.get('quantity', 0)
        self.price = kwargs.get('price', 0)
        self.commissions = kwargs.get('commissions', {})
        self.raw_results = kwargs.get('raw_results', {})
        self.operations = kwargs.get('operations', [])

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

        The real price is the price with all commission and costs
        already deducted or added.
        """
        return self.price + math.copysign(
            self.total_commissions / self.quantity,
            self.quantity
        )

    @property
    def total_commissions(self):
        """Return the sum of all commissions of this operation."""
        return sum(self.commissions.values())

    @property
    def volume(self):
        """Returns the quantity of the operation * its raw price."""
        return abs(self.quantity) * self.price

    def update_accumulator(self, accumulator):
        """Update the accumulator status with the operation data."""
        self.update_positions(accumulator)
        if self.update_results:
            self.update_accumulator_results(accumulator)

    def update_accumulator_results(self, accumulator):
        """Update the results stored in the accumulator."""
        for key, value in self.results.items():
            if key not in accumulator.state['results']:
                accumulator.state['results'][key] = 0
            accumulator.state['results'][key] += value

    def update_positions(self, accumulator):
        """Update the position of the asset with the Operation data."""
        # Here we check if the operation asset is the same
        # asset of this Accumulator object; the accumulator
        # only accumulates operations that trade its asset.
        # We also check if the operation should update the
        # position; if all this conditions are met, then
        # the position is updated.
        update_position_condition = (
            self.subject.symbol == accumulator.subject.symbol and
            self.quantity
        )
        if update_position_condition:
            # Define the new accumualtor quantity
            new_quantity = accumulator.state['quantity'] + self.quantity

            # if the quantity of the operation has the same sign
            # of the accumulated quantity then we need to
            # find out the new average price of the asset
            if same_sign(accumulator.state['quantity'], self.quantity):
                accumulator.state['price'] = average_price(
                    accumulator.state['quantity'],
                    accumulator.state['price'],
                    self.quantity,
                    self.real_price
                )

            # If the traded quantity has an opposite sign of the
            # asset's accumulated quantity and the accumulated
            # quantity is not zero, then there was a result.
            elif accumulator.state['quantity'] != 0:

                # check if we are trading more than what
                # we have on our portfolio; if yes,
                # the result will be calculated based
                # only on what was traded (the rest create
                # a new position)
                if abs(self.quantity) > abs(accumulator.state['quantity']):
                    result_quantity = accumulator.state['quantity'] * -1

                # If we're not trading more than what we have,
                # then use the operation quantity to calculate
                # the result
                else:
                    result_quantity = self.quantity

                # calculate the result of this operation and add
                # the new result to the accumulated results
                results = \
                    result_quantity * accumulator.state['price'] - \
                    result_quantity * self.real_price
                if results:
                    self.results['trades'] = results

                # If the new accumulated quantity has a different
                # sign of the old accumulated quantity then the
                # average price is now the price of the operation
                # If the new accumulated quantity is of the same sign
                # of the old accumulated quantity, the average of price
                # will not change.
                if not same_sign(accumulator.state['quantity'], new_quantity):
                    accumulator.state['price'] = self.real_price

            # If the accumulated quantity was zero then
            # there was no result and the new average price
            # is the price of the operation
            else:
                accumulator.state['price'] = self.real_price

            # update the accumulator quantity
            # with the new quantity
            accumulator.state['quantity'] = new_quantity

            # If the accumulator is empty
            # the price is set back to zero
            if not accumulator.state['quantity']:
                accumulator.state['price'] = 0


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

    Attributes:
        date: A string 'YYYY-mm-dd' representing the date of the
            operations on the container.
        operations: A list of Operation instances.
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

    def __init__(self, operations=None, tasks=None):
        if operations is None:
            operations = []
        self.operations = operations
        self.positions = {}
        if tasks is None:
            tasks = []
        self.tasks = tasks
        self.volume = 0

    def fetch_positions(self):
        """Fetch the positions resulting from the operations.

        This method executes all the methods defined in self.tasks
        in the order they are listed.

        Then it reads the self.operations list and add any remaining
        operation to the self.positions.
        """

        # Find the volume of the container (the sum
        # of the volume of all of its operations)
        self.volume = sum(operation.volume for operation in self.operations)

        raw_operations = copy.deepcopy(self.operations)

        # Execute all defined tasks
        for task in self.tasks:
            task(self)

        # fetch the positions from the remaining operations
        for operation in self.operations:
            if operation.quantity != 0 and operation.update_container:
                self.add_to_position_operations(operation)

        self.operations = raw_operations

    def add_to_position_operations(self, operation):
        """Adds an operation to the common operations list."""
        if 'operations' not in self.positions:
            self.positions['operations'] = {}
        if operation.subject.symbol in self.positions['operations']:
            merge_operations(
                self.positions['operations'][operation.subject.symbol],
                operation
            )
        else:
            self.positions['operations'][operation.subject.symbol] = operation
