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


class TaxManager:
    """The base TaxManager.

    A TaxManager object reads an operation and returns the
    correspondent rates for that operation. Since rates (and also the
    way they are applied) may vary greatly from one context to another,
    this class just implements a dummy interface for the rate discovery
    process, always returning a empty dictionary of rates.

    Every OperationContainer object has a reference to this class.
    If your app need to apply fees to your Operation objects, then you
    should extend this class and inform the new TaxManager to your
    OperationContainer:

        operation_container_object.tax_manger = your_tax_manager_object

    The OperationContainer always access his TaxManager class when
    fetch_positions() is called. Behind the scenes the container
    calls this method from the TaxManager class:

        tax_manager.get_rates_for_operation(operation, operation_type)

    After identifying the positions for every position present on the container.
    """

    @staticmethod
    def get_rates_for_operation(operation, operation_type):
        return {}
