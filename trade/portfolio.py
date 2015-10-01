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

from .accumulator import Accumulator


class Portfolio:
    """A portfolio of assets.

    A portfolio is a collection of Accumulator objects.
    It can receive Operation objects and update the corresponding
    accumulators.
    """

    def __init__(self):

        self.assets = {}
        """A dict {Asset: Accumulator}"""

        self.accumulate_tasks = []

    def accumulate(self, operation):
        """Accumulate an operation on its corresponding accumulator."""

        if operation.accumulate_underlying_operations:

            #print(operation.operations)

            self.execute_accumulate_tasks(operation)
            #operation.fetch_operations()

            #print(operation.operations)

            for underlying_operation in operation.operations:
                self.accumulate(underlying_operation)
        else:
            if operation.asset not in self.assets:
                self.assets[operation.asset] = Accumulator(operation.asset)

            self.execute_accumulate_tasks(operation)

            self.assets[operation.asset].accumulate_operation(operation)

    def execute_accumulate_tasks(self, operation):
        for task in self.accumulate_tasks:
            task(operation, self)
