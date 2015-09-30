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

from .operation import Daytrade, Operation, Exercise
from .tax_manager import TaxManager
from .utils import (
    average_price, daytrade_condition, find_purchase_and_sale
)


# container tasks

def get_operations_from_exercises(container):
    for operation in container.operations:
        if isinstance(operation, Exercise):
            if 'exercises' not in container.positions:
                container.positions['exercises'] = {}
            for operation in operation.get_operations():
                if operation.asset in container.positions['exercises'].keys():
                    container.merge_operations(
                        container.positions['exercises'][operation.asset],
                        operation
                    )
                else:
                    container.positions['exercises'][operation.asset] = \
                                                                    operation


def identify_daytrades_and_common_operations(container):
    """Separates operations into daytrades and common operations.

    After this process, the attributes 'daytrades' and
    'common_operations'  will be filled with the daytrades
    and common operations found in the container operations list,
    if any. The original operations list remains untouched.
    """
    operations = copy.deepcopy(container.operations)

    for i, operation_a in enumerate(operations):
        for operation_b in \
                [
                    op for op in operations[i:] if daytrade_condition(
                                                        op, operation_a
                                                    )
                ]:
            if operation_b.quantity != 0 and operation_a.quantity != 0:
                extract_daytrade(container, operation_a, operation_b)

        if operation_a.quantity != 0:
            add_to_common_operations(container, operation_a)


def prorate_commissions(container):
    """Prorates the container's commissions by its operations.

    This method sum the discounts in the commissions dict of the
    container. The total discount value is then prorated by the
    daytrades and common operations based on their volume.
    """

    for position_type, position_value in container.positions.items():
        for position in position_value.values():
            if position.operations:
                for operation in position.operations:
                    prorate_commissions_by_operation(container, operation)
            else:
                prorate_commissions_by_operation(container, position)


def find_rates_for_positions(container):
    """Finds the rates for all daytrades and common operations."""
    for position_type, position_value in container.positions.items():
        for position in position_value.values():
            if position.operations:
                for operation in position.operations:
                    operation.rates = \
                        container.tax_manager.get_rates_for_operation(
                                                    operation, position_type)
            else:
                position.rates = \
                    container.tax_manager.get_rates_for_operation(
                                                    position, position_type)


def prorate_commissions_by_operation(container, operation):
    """Prorates the commissions of the container for one operation.

    The ratio is based on the container volume and the volume of
    the operation.
    """
    if operation.volume != 0 and container.volume != 0:
        percent = operation.volume / container.volume * 100
        for key, value in container.commissions.items():
            operation.commissions[key] = value * percent / 100


def extract_daytrade(container, operation_a, operation_b):
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
        container.date,
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

    if 'daytrades' not in container.positions:
        container.positions['daytrades'] = {}
    if daytrade.asset in container.positions['daytrades']:
        container.merge_operations(
            container.positions['daytrades'][daytrade.asset].operations[0],
            daytrade.operations[0]
        )
        container.merge_operations(
            container.positions['daytrades'][daytrade.asset].operations[1],
            daytrade.operations[1]
        )
        container.positions['daytrades'][daytrade.asset].quantity += \
                                                            daytrade.quantity
    else:
        container.positions['daytrades'][daytrade.asset] = daytrade


def add_to_common_operations(container, operation):
    """Adds an operation to the common operations list."""
    if 'common operations' not in container.positions:
        container.positions['common operations'] = {}

    if operation.asset in container.positions['common operations']:
        container.merge_operations(
            container.positions['common operations'][operation.asset],
            operation
        )
    else:
        container.positions['common operations'][operation.asset] = operation
