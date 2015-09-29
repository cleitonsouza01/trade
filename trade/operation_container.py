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

from .operation import Daytrade, Operation
from .tax_manager import TaxManager
from .utils import (
    average_price, daytrade_condition, find_purchase_and_sale
)


class OperationContainer:
    """A container for operations.

    An OperationContainer is used to group operations, like operations
    that occurred on the same date, and then perform tasks on them.

    The main task task that the OperationContainer can perform is to
    identify the resulting positions from a group of operations. The
    resulting positions are all operations separated as daytrades and
    common operations, with all common operations and daytrades with
    the same asset grouped into a single operation or a single
    daytrade.

    The resulting common operations and daytrades contains the
    OperationContiner commissions prorated by their volumes, and also
    any fees the OperationContainer TaxManager finds for them.

    This is achieved by calling this method:

        fetch_positions()

    Every time fetch_positions() is called the OperationContainer
    execute this tasks behind the scenes:

    - Separate the daytrades and the common operations of a group of
      operations that occurred on the same date by using the method:

        identify_daytrades_and_common_operations()

    - Prorate a group of commissions proportionally for all daytrades
      and common operations, if any, by using the method:

        prorate_commissions()

    - Find the appliable rates for the resulting positions by calling
      this method:

        find_rates_for_positions()

    Attributes:
        date: A string 'YYYY-mm-dd' representing the date of the
            operations on the container.
        operations: A list of Operation instances.
        commissions: A dict with discount names and values to be
            deducted from the operations.
        daytrades: a dict of Daytrade objects, indexed by the daytrade
            asset.
        common_operations: a dict of Operation objects, indexed by the
            operation asset.
        fetch_positions_tasks: a list of OperationContainer methods.
            The methods will be called in the order they are defined
            in this list when fetch_positions() is called. The default
            fetch_positions_tasks list is this:
                [
                    self.get_operations_from_exercises,
                    self.identify_daytrades_and_common_operations,
                    self.prorate_commissions,
                    self.find_rates_for_positions,
                ]
    """

    def __init__(self,
                date=None,
                operations=None,
                exercises=None,
                commissions=None,
                tax_manager=TaxManager()
            ):
        self.date = date
        if operations is None: operations=[]
        if exercises is None: exercises=[]
        if commissions is None: commissions = {}
        self.operations = operations
        self.exercises = exercises
        self.commissions = commissions
        self.daytrades = {}
        self.common_operations = {}
        self.exercise_operations = {}
        self.tax_manager = tax_manager

        # Here we define the default methods to be
        # executed when fetch_positions() is called,
        # and also their order of execution; you may
        # append other methods to this list, or
        # re-create this list in a different order or
        # with different methods to suit your needs.
        self.fetch_positions_tasks = [

            # This method get the resulting operations
            # that are created by an option exercise;
            self.get_operations_from_exercises,

            # This method separates daytrades from operations
            # that are not daytrades, and group them;
            # Operations originated from exercises are by default
            # not considered
            self.identify_daytrades_and_common_operations,

            # This method prorates all values on the
            # container commissions dictionary by all the
            # trades on the container, based on their volume
            self.prorate_commissions,

            # This method should return any rates that
            # need to be applied to the daytrades and
            # common operations (aka the container positions)
            self.find_rates_for_positions,
        ]

    @property
    def total_commission_value(self):
        """Returns the sum of values of all commissions."""
        return sum(self.commissions.values())

    @property
    def volume(self):
        """Returns the total volume of the operations in the container."""
        return sum(operation.volume for operation in self.operations)

    def fetch_positions(self):
        """Fetch the positions resulting from the operations.

        This method executes all the methods defined on the
        fetch_positions_tasks attribute in the order they are
        listed.
        """
        for task in self.fetch_positions_tasks:
            task()

    def get_operations_from_exercises(self):
        for exercise in self.exercises:
            for operation in exercise.get_operations():
                if operation.asset in self.exercise_operations.keys():
                    self.merge_operations(
                        self.exercise_operations[operation.asset],
                        operation
                    )
                else:
                    self.exercise_operations[operation.asset] = operation

    def prorate_commissions(self):
        """Prorates the container's commissions by its operations.

        This method sum the discounts in the commissions dict of the
        container. The total discount value is then prorated by the
        daytrades and common operations based on their volume.
        """
        for operation in self.common_operations.values():
            self.prorate_commissions_by_operation(operation)
        for daytrade in self.daytrades.values():
            self.prorate_commissions_by_operation(daytrade.purchase)
            self.prorate_commissions_by_operation(daytrade.sale)

    def prorate_commissions_by_operation(self, operation):
        """Prorates the commissions of the container for one operation.

        The ratio is based on the container volume and the volume of
        the operation.
        """
        percent = operation.volume / self.volume * 100
        for key, value in self.commissions.items():
            operation.commissions[key] = value * percent / 100

    def identify_daytrades_and_common_operations(self):
        """Separates operations into daytrades and common operations.

        After this process, the attributes 'daytrades' and
        'common_operations'  will be filled with the daytrades
        and common operations found in the container operations list,
        if any. The original operations list remains untouched.
        """
        operations = copy.deepcopy(self.operations)

        for i, operation_a in enumerate(operations):
            for operation_b in \
                    [
                        op for op in operations[i:] if daytrade_condition(
                                                            op, operation_a
                                                        )
                    ]:
                if operation_b.quantity != 0 and operation_a.quantity != 0:
                    self.extract_daytrade(operation_a, operation_b)

            if operation_a.quantity != 0:
                self.add_to_common_operations(operation_a)

    def extract_daytrade(self, operation_a, operation_b):
        """Extracts the daytrade part of two operations."""

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
                self.daytrades[daytrade.asset].purchase,
                daytrade.purchase
            )
            self.merge_operations(
                self.daytrades[daytrade.asset].sale,
                daytrade.sale
            )
            self.daytrades[daytrade.asset].quantity += daytrade.quantity
        else:
            self.daytrades[daytrade.asset] = daytrade

    def add_to_common_operations(self, operation):
        """Adds an operation to the common operations list."""
        if operation.asset in self.common_operations:
            self.merge_operations(
                self.common_operations[operation.asset],
                operation
            )
        else:
            self.common_operations[operation.asset] = operation

    def merge_operations(self, existing_operation, operation):
        """Merges one operation with another operation."""
        existing_operation.price = average_price(
                                        existing_operation.quantity,
                                        existing_operation.price,
                                        operation.quantity,
                                        operation.price
                                    )
        existing_operation.quantity += operation.quantity

    def find_rates_for_positions(self):
        """Finds the rates for all daytrades and common operations."""
        for asset, daytrade in self.daytrades.items():
            daytrade.purchase.rates = \
                self.tax_manager.get_rates_for_daytrade(daytrade.purchase)
            daytrade.sale.rates = \
                self.tax_manager.get_rates_for_daytrade(daytrade.sale)
        for asset, operation in self.common_operations.items():
            operation.rates = \
                self.tax_manager.get_rates_for_operation(operation)
