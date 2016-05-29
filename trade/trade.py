"""trade: Financial Application Framework

http://trade.readthedocs.org/
https://github.com/rochars/trade
License: MIT

Copyright (c) 2016 Rafael da Silva Rocha

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
from abc import ABCMeta

from . utils import (
    average_price,
    same_sign,
    merge_operations,
    find_purchase_and_sale,
    daytrade_condition
)
from accumulator import Occurrence, Subject


class Asset(Subject):
    """An asset represents anything that can be traded."""

    default_state = {
        'quantity': 0,
        'price': 0,
        'results': {}
    }

    def __init__(self, symbol=None, name=None, expiration_date=None, **kwargs):
        super(Asset, self).__init__(symbol, name, expiration_date)
        self.underlying_assets = kwargs.get('underlying_assets', {})


class Event(Occurrence):
    """An occurrence that changes the state of one or more assets.

    This is a base class for events.

    Attributes:
        date: A string 'YYYY-mm-dd', the date the event occurred.
        asset: The target asset of the event.
        factor: the factor of the change on the asset state.
    """

    __metaclass__ = ABCMeta

    def __init__(self, asset, date, factor):
        super(Event, self).__init__(asset, date)
        self.factor = factor


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
        """Returns the results associated with the operation."""
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
        """Returns the sum of all commissions of this operation."""
        return sum(self.commissions.values())

    @property
    def volume(self):
        """Returns the quantity of the operation * its raw price."""
        return abs(self.quantity) * self.price

    def update_accumulator(self, accumulator):
        """Updates the accumulator with the operation data."""
        self.update_positions(accumulator)
        if self.update_results:
            self.update_accumulator_results(accumulator)

    def update_accumulator_results(self, accumulator):
        """Updates the results stored in the accumulator."""
        for key, value in self.results.items():
            if key not in accumulator.state['results']:
                accumulator.state['results'][key] = 0
            accumulator.state['results'][key] += value

    def update_positions(self, accumulator):
        """Updates the state of the asset with the operation data."""
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


class Daytrade(Operation):
    """A daytrade operation.

    Daytrades are operations of purchase and sale of an asset on
    the same date.

    Attributes:
        asset: An asset instance, the asset that is being traded.
        quantity: The traded quantity of the asset.
        purchase: A Operation object representing the purchase of the
            asset.
        sale: A Operation object representing the sale of the asset.
        update_position: Set to False, as daytrades don't change the
            portfolio position; they just create results.
    """

    update_position = False

    def __init__(self, operation_a, operation_b):
        """Creates the daytrade object.

        Based on the informed values this method creates 2 operations:
        - a purchase operation
        - a sale operation

        Both operations can be treated like any other operation when it
        comes to taxes and the prorate of commissions.
        """
        super(Daytrade, self).__init__(
            date=operation_a.date,
            subject=operation_a.subject,
        )
        purchase, sale = find_purchase_and_sale(operation_a, operation_b)
        self.extract_daytrade(purchase, sale)

        # Purchase is 0, Sale is 1
        self.operations = [
            Operation(
                date=purchase.date,
                subject=purchase.subject,
                quantity=self.quantity,
                price=purchase.price
            ),
            Operation(
                date=sale.date,
                subject=sale.subject,
                quantity=self.quantity*-1,
                price=sale.price
            )
        ]

    @property
    def results(self):
        """Returns the profit or the loss generated by the day trade."""
        return {
            'daytrades': abs(self.operations[1].real_value) - \
                                        abs(self.operations[0].real_value)
        }

    def update_accumulator(self, accumulator):
        """Updates the accumulator state with the day trade result."""
        self.update_accumulator_results(accumulator)

    def extract_daytrade(self, purchase, sale):
        """Extracts the daytraded quantity from 2 operations."""
        # Find the daytraded quantity; the daytraded
        # quantity is always the smallest absolute quantity
        self.quantity = min([purchase.quantity, abs(sale.quantity)])

        # Update the operations that originated the
        # daytrade with the new quantity after the
        # daytraded part has been extracted; One of
        # the operations will always have zero
        # quantity after this, being fully consumed
        # by the daytrade. The other operation may or
        # may not end with zero quantity.
        purchase.quantity -= self.quantity
        sale.quantity += self.quantity

    def append_to_positions(self, container):
        """Saves a Daytrade object in the container.

        If there is already a day trade with the same asset on the
        container, then the day trades are merged.
        """
        if 'daytrades' not in container.positions:
            container.positions['daytrades'] = {}

        # If the container already have
        # a daytrade position with this asset,
        # then we must merge this daytrade
        # with the existing daytrade
        if self.subject.symbol in container.positions['daytrades']:
            self.merge_underlying(container, 0)
            self.merge_underlying(container, 1)

            # Update the daytraded quantity with the
            # quantity of this daytrade
            container.positions['daytrades'][self.subject.symbol].quantity +=\
                self.quantity

        # If this is the first found daytrade
        # with this asset on the container, then
        # place this daytrade on the container
        else:
            container.positions['daytrades'][self.subject.symbol] = self

    def merge_underlying(self, container, operation_index):
        """Merges one day trade underlying operation."""
        merge_operations(
            container.positions['daytrades'][self.subject.symbol]\
                .operations[operation_index],
            self.operations[operation_index]
        )


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


def fetch_daytrades(container):
    """An OperationContainer task.

    Fetches the daytrades from the OperationContainer operations.

    The daytrades are placed on the container positions under the
    'daytrades' key, inexed by the Daytrade asset's symbol.
    """
    for i, operation_a in enumerate(container.operations):
        for operation_b in [
                x for x in container.operations[i:] if\
                    daytrade_condition(x, operation_a)
            ]:
            Daytrade(operation_a, operation_b).append_to_positions(container)
