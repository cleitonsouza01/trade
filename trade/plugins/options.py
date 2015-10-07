"""options: Options plugin for the trade module.

This plugin provides Options functionalities to the trade module.

With this plugin you can:
- Create option assets that references underlying assets
- Create exercise operations that change both the option and underlying
  asset position on the portfolio

It provides:
- Option, a subclass of trade.Derivative
- Exercise, a subclass of trade.Operation
- the fetch_exercises() task to the OperationContainer
- the get_exercise_premium() task to the Portfolio

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

from ..trade import Asset, Operation
from ..utils import merge_operations


class Option(Asset):
    """Represents a vanilla option.

    Represents both calls and puts.

    This class can be used for common option operations or as a base
    for classes that represent exotic options.

    Attributes:
        name: A string representing the name of the asset.
        symbol: A string representing the symbol of the asset.
        expiration_date: A string 'YYYY-mm-dd' representing the
            expiration date of the asset, if any.
        underlying_assets: A dict of Asset objects representing the
            underlying assets of this asset and the ratio to which
            the asset relates to the Option. It looks like this:
            {Asset: float}
    """

    def __init__(
            self,
            name=None,
            symbol=None,
            expiration_date=None,
            underlying_assets=None
        ):
        super(Option, self).__init__(name, symbol, expiration_date)
        if underlying_assets is None:
            underlying_assets = {}
        self.underlying_assets = underlying_assets

    def exercise(self, quantity, price, premium=0):
        """Exercises the option.

        If a premium is informed, then it will be considered on the
        underlying asset operation price.

        Returns two operations:
            - one operation with zero value representing the option
              being consumed by the exercise;
            - one operation representing the purchase or sale of the
              underlying asset
        """
        # Create an operation to consume
        # the option on the portfolio
        operations = [
            Operation(
                quantity=abs(quantity)*-1,
                price=0,
                asset=self
            )
        ]
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
                    asset=underlying_asset
                )
            )
        return operations


class Exercise(Operation):
    """An exercise operation.

    Exercise operations are operations that involve more than one
    asset, usually a derivative like a Option and an underlying asset.

    An exercise will likely change the accumulated quantity of both the
    derivative and its underlyings assets.
    """

    # In a exercise operation it is the underlying
    # operations that will change the position on
    # the portfolio
    accumulate_underlying_operations = True

    def fetch_operations(self, portfolio=None):
        """Fetch the operations created by this exercise.

        If a portfolio is informed, then the premium of the option
        will be considered.

        An exercise creates multiple operations:
        - One operation to consume the option that it being exercised
        - One operation to represent the sale or the purchase of each
            of its underlying assets, if any.
        """
        if portfolio:
            self.operations = self.asset.exercise(
                self.quantity,
                self.price,
                portfolio.assets[self.asset.symbol].price
            )
        else:
            self.operations = self.asset.exercise(
                self.quantity,
                self.price,
            )
        for operation in self.operations:
            operation.date = self.date


def fetch_exercises(container):
    """An OperationContainer task.

    After this task, all operations created by Exercise objects
    will be on the container positions under the key 'exercises'.
    """
    for operation in container.operations:
        if isinstance(operation, Exercise):
            if 'exercises' not in container.positions:
                container.positions['exercises'] = {}
            operation.fetch_operations()
            for operation in operation.operations:
                symbol = operation.asset.symbol
                if symbol in container.positions['exercises'].keys():
                    merge_operations(
                        container.positions['exercises'][symbol],
                        operation
                    )
                else:
                    container.positions['exercises'][symbol] = operation


def fetch_exercise_operations(operation, portfolio):
    """A Portfolio task.

    Fetch the operations in a exercise operations and  get the premium
    of the option that is being exercised.

    It searchs on the Portfolio object for an Accumulator of the option
    and then use the accumulator price as the premium to be included
    on the exercise operation price.
    """
    if isinstance(operation, Exercise):
        operation.fetch_operations(portfolio)
