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

import copy

from .tax_manager import TaxManager
from .utils import average_price


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
    any rates the OperationContainer TaxManager finds for them.

    This is achieved by calling this method:

        fetch_positions()

    Every time fetch_positions() is called the OperationContainer
    execute this tasks behind the scenes:

    - Execute all tasks defined in self.tasks.

    - Create positions in self.positions for all operations in
      self.operations.

    - Prorate the commissions, if any, proportionally for all positions
      by calling:

        prorate_commissions()

    - Find the rates, if any, for the resulting positions by calling:

        find_rates_for_positions()

    Attributes:
        date: A string 'YYYY-mm-dd' representing the date of the
            operations on the container.
        operations: A list of Operation instances.
        commissions: A dict with discount names and values to be
            deducted from the operations.
        positions: a dict of positions with this format:
            self.positions = {
                'position type': {
                    Asset: Operation,
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

    def __init__(self,
                date=None,
                operations=None,
                commissions=None
            ):
        self.date = date
        if operations is None: operations=[]
        if commissions is None: commissions = {}
        self.operations = operations
        self.commissions = commissions
        self.positions = {}

        self.tax_manager = TaxManager

        self.raw_operations = copy.deepcopy(self.operations)

        self.tasks = []
        """Methods to be executed when fetch_positions() is called.

        A default setup could look like this:
        self.tasks = [
            self.get_operations_from_exercises,
            self.identify_daytrades_and_common_operations,
            self.prorate_commissions,
            self.find_rates_for_positions,
        ]
        """

    @property
    def total_commission_value(self):
        """Returns the sum of values of all commissions."""
        return sum(self.commissions.values())

    @property
    def volume(self):
        """Returns the total volume of the operations in the container."""
        return sum(operation.volume for operation in self.raw_operations)

    def fetch_positions(self):
        """Fetch the positions resulting from the operations.

        This method executes all the methods defined on the tasks
        attribute in the order they are listed.
        """

        # Execute all defined tasks
        for task in self.tasks:
            task(self)

        # fetch the positions from the remaining operations
        for operation in self.operations:
            if operation.quantity != 0:
                self.add_to_common_operations(operation)

        # TODO should be configurable
        # prorate any commission for the operations
        self.prorate_commissions()

        # TODO should be configurable
        self.find_rates_for_positions()

    def merge_operations(container, existing_operation, operation):
        """Merges one operation with another operation."""
        existing_operation.price = average_price(
                                        existing_operation.quantity,
                                        existing_operation.price,
                                        operation.quantity,
                                        operation.price
                                    )
        existing_operation.quantity += operation.quantity

    def add_to_common_operations(self, operation):
        """Adds an operation to the common operations list."""
        if 'common operations' not in self.positions:
            self.positions['common operations'] = {}

        if operation.asset in self.positions['common operations']:
            self.merge_operations(
                self.positions['common operations'][operation.asset],
                operation
            )
        else:
            self.positions['common operations'][operation.asset] = operation

    def prorate_commissions_by_operation(self, operation):
        """Prorates the commissions of the container for one operation.

        The ratio is based on the container volume and the volume of
        the operation.
        """
        if operation.volume != 0 and self.volume != 0:
            percent = operation.volume / self.volume * 100
            for key, value in self.commissions.items():
                operation.commissions[key] = value * percent / 100

    def prorate_commissions(self):
        """Prorates the container's commissions by its operations.

        This method sum the discounts in the commissions dict of the
        container. The total discount value is then prorated by the
        daytrades and common operations based on their volume.
        """
        for position_type, position_value in self.positions.items():
            for position in position_value.values():
                if position.operations:
                    for operation in position.operations:
                        self.prorate_commissions_by_operation(operation)
                else:
                    self.prorate_commissions_by_operation(position)

    # FIXME
    def find_rates_for_positions(self):
        """Finds the rates for all daytrades and common operations."""
        for position_type, position_value in self.positions.items():
            for position in position_value.values():
                if position.operations:
                    for operation in position.operations:
                        operation.rates = \
                            self.tax_manager.get_rates_for_operation(
                                operation, position_type
                            )
                else:
                    position.rates = self.tax_manager.get_rates_for_operation(
                                            position, position_type
                                        )
