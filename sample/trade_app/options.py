"""options: Options plugin for the trade module.

trade: Financial Application Framework
http://trade.readthedocs.org/
https://github.com/rochars/trade
License: MIT

This plugin is an example of vanilla call and put operations on the trade module.

With this plugin you can:
- Create calls and puts that references underlying assets
- Create exercise operations that change both the option and underlying
  asset position on the portfolio

It provides:
- Option, a subclass of Asset
- Exercise, a subclass of Operation
- the fetch_exercises() task for the OperationContainer
- the fetch_exercise_operations() task for the Portfolio

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

from trade.occurrences import Asset, Operation
from trade.utils import merge_operations


class Option(Asset):
    """Represents a vanilla option.

    Represents both calls and puts.

    This class can be used for cal and put operations or as a base
    for classes that represent exotic options.

    Attributes:
        name: A string representing the name of the asset.
        symbol: A string representing the symbol of the asset.
        expiration_date: A string 'YYYY-mm-dd' representing the
            expiration date of the asset, if any.
        underlying_assets: A dict of Assets representing the
            underlying assets of this asset and the ratio to which
            the asset relates to the Option. It looks like this:
            {Asset: float}
    """

    def exercise(self, quantity, price, premium=0):
        """Exercises the option.

        If a premium is informed, then it will be considered on the
        underlying asset cost.

        Returns a list of operations:
            - one operation with zero value representing the option
              being consumed by the exercise;
            - operations representing the purchase or sale of its
              underlying assets
        """
        operations = []

        # Create an operation to consume
        # the option on the portfolio.
        option_consuming = Operation(
            quantity=abs(quantity)*-1,
            price=0,
            subject=self
        )
        # this operation should not create
        # any results, just update the
        # quantity and price in the accumulator.
        option_consuming.update_results = False
        operations.append(option_consuming)

        # Create an operation to represent
        # the purchase or sale of the
        # underlying asset. If the option has
        # no underlying asset, then the only
        # operation created will be option
        # consuming operation.
        for underlying_asset, ratio in self.underlying_assets.items():
            operations.append(
                Operation(
                    quantity=quantity * ratio,
                    price=price + premium,
                    subject=underlying_asset
                )
            )
        return operations


class Exercise(Operation):
    """An option exercise operation.

    An exercise will likely change the state of both the derivative and
    its underlyings assets.
    """

    update_position = False
    update_container = False

    def update_portfolio(self, portfolio):
        """A Portfolio task.

        Fetch the operations in a exercise operations and  get the premium
        of the option that is being exercised.

        It searches on the Portfolio object for an Accumulator of the option
        and then use the accumulator cost as the premium to be included
        on the exercise operation price.
        """
        self.fetch_operations(portfolio)
        for operation in self.operations:
            portfolio.accumulate(operation)

    def update_accumulator(self, accumulator):
        """Exercise operations should not update the accumulator.

        Its its underlying operations that should update the
        accumulator.
        """
        pass

    def fetch_operations(self, portfolio=None):
        """Fetch the operations created by the exercise.

        If a portfolio is informed, then the premium of the option
        will be considered.

        An exercise creates multiple operations:
        - one operation to consume the option that it being exercised
        - operations to represent the sale or the purchase of each
            of its underlying assets, if any.
        """
        if portfolio:
            self.operations = self.subject.exercise(
                self.quantity,
                self.price,
                portfolio.subjects[self.subject.symbol].state['price']
            )
        else:
            self.operations = self.subject.exercise(
                self.quantity,
                self.price,
            )
        for operation in self.operations:
            operation.date = self.date


def fetch_exercises(container):
    """An OperationContainer task.

    Fetch all exercise operations on the container into a single
    exercise (by asset) on the container positions dictionary under
    the key 'exercises'.
    """
    if 'positions' not in container.context:
        container.context['positions'] = {}
    for operation in container.operations:
        if isinstance(operation, Exercise):
            if 'exercises' not in container.context['positions']:
                container.context['positions']['exercises'] = {}
            symbol = operation.subject.symbol
            if symbol in container.context['positions']['exercises'].keys():
                merge_operations(
                    container.context['positions']['exercises'][symbol],
                    operation
                )
            else:
                container.context['positions']['exercises'][symbol] = operation
