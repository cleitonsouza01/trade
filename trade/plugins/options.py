"""options: Options plugin for the trade module.

This plugin provides Options functionalities to the trade module.

With this plugin you can:
- Create option assets that points to other (underlying) assets
- Create exercise operations that change both the option and underlying
  asset position on the portfolio

It provides:
- Option, a subclass of asset.Derivative
- Exercise, a subclass of operation.Operation
- the fetch_exercises() task to the OperationContainer
- the get_exercise_premium() task to the Portfolio

-----------------------------------------------------------------------

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

from ..asset import Derivative
from ..operation import Operation


class Option(Derivative):
    """Represents an Option.

    This class represents both calls and puts.
    """

    def exercise(self, quantity, price, date, premium=0):
        """Exercises the option.

        If a premium if informed, then it will be considered on the
        underlying asset operation price.

        Returns two operations:
            - one operation with zero value representing the option
              being consumed by the exercise;
            - one operation representing the purchase or sale of the
              underlying asset
        """
        operations = [
            # Create an operation to consume
            # the option on the portfolio
            Operation(
                quantity=abs(quantity)*-1,
                price=0,
                date=date,
                asset=self
            ),
            # Create an operation to represent
            # the purchase or sale of the
            # underlying asset
            Operation(
                quantity=quantity * self.ratio,
                price=price + premium,
                date=date,
                asset=self.underlying_assets[0]
            )
        ]
        return operations


class Exercise(Operation):
    """An exercise operation.

    Exercise operations are operations that involve more than one
    asset, usually a derivative like a Option and an underlying asset.

    An exercise will change the accumulated quantity of both the
    derivative and the underlying asset.
    """

    accumulate_underlying_operations = True

    def fetch_operations(self, portfolio=None):
        """Returns the operations created by this exercise.

        If a portfolio is informed, then the premium of the option
        will be considered.

        An exercise creates two operations:
        - One operation to consume the option that it being exercised
        - One operation to represent the sale or the purchase of the
            asset
        """
        if portfolio:
            self.operations = self.asset.exercise(
                        self.quantity,
                        self.price,
                        self.date,
                        portfolio.assets[self.asset].price
                    )
        else:
            self.operations = self.asset.exercise(
                        self.quantity,
                        self.price,
                        self.date
                    )


# TODO document better this OperationContainer task
def fetch_exercises(container):
    """OperationContainer task.

    After this task, all operations created by Exercise objects
    will be on the container positions under the key 'exercises'.
    """
    for operation in container.operations:
        if isinstance(operation, Exercise):
            if 'exercises' not in container.positions:
                container.positions['exercises'] = {}
            operation.fetch_operations()
            for operation in operation.operations:
                if operation.asset in container.positions['exercises'].keys():
                    container.merge_operations(
                        container.positions['exercises'][operation.asset],
                        operation
                    )
                else:
                    container.positions['exercises'][operation.asset] = \
                                                                    operation


def get_exercise_premium(operation, portfolio):
    """Get the premium of the option that is being exercised.

    It searchs on the Portfolio object for an Accumulator of the option
    and then use the accumulator price as the premium to be included
    on the exercise operation price.
    """
    if isinstance(operation, Exercise):
        operation.fetch_operations(portfolio)
