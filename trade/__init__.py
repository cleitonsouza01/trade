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

from .asset import Asset, Option, Derivative
from .operation import Operation, Daytrade, Exercise
from .accumulator import Accumulator
from .event import Event, StockSplit, ReverseStockSplit
from .tax_manager import TaxManager
from .operation_container import OperationContainer
from .container_tasks import (
    get_operations_from_exercises,
    identify_daytrades_and_common_operations,
    prorate_commissions,
    find_rates_for_positions,
    prorate_commissions_by_operation,
    add_to_common_operations,
)


from .utils import daytrade_condition, average_price, same_sign


__author__ = 'rocha.rafaelsilva@gmail.com'
__version__ = '0.1.0'
