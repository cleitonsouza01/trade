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
    that occurred on the same date, and then perform tasks on them. It
    can:

    - Separate the daytrades and the common operations of a group of
      operations that occurred on the same date by using the method:

        identify_daytrades_and_common_operations()

    - Prorate a group of taxes proportionally for all daytrades and
      common operations, if any, by using the method:

        prorate_comissions_by_daytrades_and_common_operations()

    Attributes:
        date: A string 'YYYY-mm-dd' representing the date of the
            operations on the container.
        operations: A list of Operation instances.
        comissions: A dict with discount names and values to be deducted
            from the operations.
        daytrades: a dict of Daytrade objects, indexed by the daytrade
            asset.
        common_operations: a dict of Operation objects, indexed by the
            operation asset.
    """

    def __init__(self,
                date=None,
                operations=None,
                comissions=None,
                tax_manager=TaxManager()
            ):
        self.date = date
        if operations is None: operations=[]
        if comissions is None: comissions = {}
        self.operations = operations
        self.comissions = comissions
        self.daytrades = {}
        self.common_operations = {}
        self.tax_manager = tax_manager

    @property
    def total_comission_value(self):
        """Return the sum of values in the container comissions dict."""
        return sum(self.comissions.values())

    @property
    def volume(self):
        """Return the total volume of the operations in the container."""
        return sum(operation.volume for operation in self.operations)

    def fetch_positions(self):
        """Fetch the positions resulting from the operations.

        Fetching the position is a complex process that needs to be
        better documented. What happens is as follows:

        - Separate all daytrades and common operations;
        - Group all common operations with one asset into a single Operation,
            so in the end you only have one common operation per asset;
        - Group all daytrades with one asset into a single Daytrade,
            so in the end you only have one daytrade per asset;
        - put all common_operations in self.common_operations, a dict
            indexed by the operation's asset name;
        - put all daytrades in self.daytrades, a dict indexed by the
            daytrade's asset name;
        - Prorate all comissions of the container for the common
            operations and the purchase and sale operation of every
            daytrade;
        - Find the taxes to be applyed to every common operation and to
            every purchase and sale operation of every daytrade.

        After this method is executed:

        - the raw operations list of the container remains untouched;
        - the container common_operations list is filled with all
            common operations of the container, with all information
            about comissions and taxes to be applyed to each operation;
        - the container daytrades list is filled with all daytrades
            of the container, with all information about comissions
            and taxes to be applyed to every daytrade's purchase and
            sale operation.
        """
        self.identify_daytrades_and_common_operations()
        self.prorate_comissions_by_daytrades_and_common_operations()
        self.find_taxes_for_positions()

    def prorate_comissions_by_daytrades_and_common_operations(self):
        """Prorate the TradeContainer comissions by its operations.

        This method sums all discounts on the comissions dict of the
        accumulator. The total discount value is then prorated by the
        daytrades and common operations based on their volume.
        """
        for operation in self.common_operations.values():
            self.prorate_comissions_by_operation(operation)
        for daytrade in self.daytrades.values():
            self.prorate_comissions_by_operation(daytrade.purchase)
            self.prorate_comissions_by_operation(daytrade.sale)

    def prorate_comissions_by_operation(self, operation):
        """Prorate the comissions of the container for one operation.

        The ratio is based on the container volume and the operation
        volume.
        """
        percent = operation.volume / self.volume * 100
        for key, value in self.comissions.items():
            operation.comissions[key] = value * percent / 100

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
                if operation_b.quantity != 0 and operation_a.quantity != 0:
                    self.extract_daytrade(operation_a, operation_b)

            if operation_a.quantity != 0:
                self.add_to_common_operations(operation_a)

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
        """Add a operation to the common operations list."""
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

    def find_taxes_for_positions(self):
        """Get the taxes for every position on the container."""
        for asset, daytrade in self.daytrades.items():
            daytrade.purchase.taxes = \
                self.tax_manager.get_taxes_for_daytrade(daytrade.purchase)
            daytrade.sale.taxes = \
                self.tax_manager.get_taxes_for_daytrade(daytrade.sale)
        for asset, operation in self.common_operations.items():
            operation.taxes = \
                self.tax_manager.get_taxes_for_operation(operation)
