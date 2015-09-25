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
    """A base TaxManager.

    A TaxManager object reads an operation and returns the
    correspondent percentual taxes for that operation. Since taxes
    (and also the way they are applyed) may vary greatly from one
    context to another, this class only implements a dumb interface
    for the tax discovery process, always returning a empty dict of
    taxes.

    Every OperationContainer object have a reference to an instance
    of this TaxManager. If your app need to apply taxes to your
    Operation objects, extend this class and inform the new TaxManager
    to your OperationContainer by

        operation_container_object.tax_manger = your_tax_manager_object

    The OperationContainer will always access the TaxManager when
    fetch_positions() is called. Behind the scenes the container will
    call this methods from the TaxManager object:

        tax_manager.get_taxes_for_operation(operation)
        tax_manager.get_taxes_for_daytrade(operation)

    for every operation and daytrade present on the container
    position dict. These taxes will then be considered when calculating
    the results and average price resulting from the operations.
    """

    def get_taxes_for_operation(self, operation):
        return {}

    def get_taxes_for_daytrade(self, operation):
        return {}
