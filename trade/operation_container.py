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
        self.exercise_operations: a dict of Operation objects, indexed
            by the operation asset. The operations are operations
            created by option exercises.
        fetch_positions_tasks: a list of OperationContainer methods.
            The methods will be called in the order they are defined
            in this list when fetch_positions() is called.
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

        self.fetch_positions_tasks = []
        """Methods to be executed when fetch_positions() is called.

        A default setup could look like this:
        self.fetch_positions_tasks = [
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
        return sum(operation.volume for operation in self.operations)

    def fetch_positions(self):
        """Fetch the positions resulting from the operations.

        This method executes all the methods defined on the
        fetch_positions_tasks attribute in the order they are
        listed.
        """
        for task in self.fetch_positions_tasks:
            task(self)

    def merge_operations(container, existing_operation, operation):
        """Merges one operation with another operation."""
        existing_operation.price = average_price(
                                        existing_operation.quantity,
                                        existing_operation.price,
                                        operation.quantity,
                                        operation.price
                                    )
        existing_operation.quantity += operation.quantity
