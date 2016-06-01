"""Tasks for the OperationContainer.

trade: Financial Application Framework
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

from __future__ import division

from . utils import (
    merge_operations,
    daytrade_condition
)
from . occurrences import Daytrade


def find_volume(container):
    """Find the volume of the operations in the container."""
    container.context['volume'] = sum(
        operation.volume for operation in container.operations
    )


def group_positions(container):
    """Group the container operations with the same asset."""
    if 'positions' not in container.context:
        container.context['positions'] = {}
    for operation in container.operations:
        if operation.quantity != 0 and operation.update_container:
            add_to_position_group(container, operation)

def add_to_position_group(container, operation):
    """Adds an operation to the common operations list."""
    if 'operations' not in container.context['positions']:
        container.context['positions']['operations'] = {}
    if operation.subject.symbol in container.context['positions']['operations']:
        merge_operations(
            container.context['positions']\
                ['operations'][operation.subject.symbol],
            operation
        )
    else:
        container.context['positions']\
            ['operations'][operation.subject.symbol] = operation


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


def prorate_commissions(container):
    """Prorates the container's commissions by its operations.

    This method sum the discounts in the commissions dict of the
    container. The total discount value is then prorated by the
    position operations based on their volume.
    """
    if 'positions' in container.context:
        for position_value in container.context['positions'].values():
            for position in position_value.values():
                if position.update_position:
                    prorate_commissions_by_position(container, position)
                else:
                    for operation in position.operations:
                        prorate_commissions_by_position(container, operation)

def prorate_commissions_by_position(container, operation):
    """Prorates the commissions of the container for one position.

    The ratio is based on the container volume and the volume of
    the position operation.
    """
    if 'volume' in container.context:
        if operation.volume != 0 and container.context['volume'] != 0:
            percent = operation.volume / container.context['volume'] * 100
            for key, value in container.commissions.items():
                operation.commissions[key] = value * percent / 100
