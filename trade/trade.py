"""trade

trade: Financial Application Framework
http://trade.readthedocs.org/
https://github.com/rochars/trade
License: MIT

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

import copy


class OperationContainer(object):
    """A container for operations."""

    def __init__(self, operations, tasks):
        self.operations = operations
        self.tasks = tasks
        self.context = {}

    def fetch_positions(self):
        """Run the tasks.

        This method executes all the methods defined in self.tasks
        in the order that they are listed.
        """

        #TODO must not be necessary
        raw_operations = copy.deepcopy(self.operations)

        for task in self.tasks:
            task(self)

        #TODO must not be necessary
        self.operations = raw_operations
