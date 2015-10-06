"""trade: Tools For Stock Trading Applications.

trade is Python framework to ease the development of investment
management applications. It is focused in, but not limited to,
stock exchange markets.

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
from __future__ import division

from abc import ABCMeta, abstractmethod
import math
import copy

from .utils import average_price, same_sign, merge_operations


class Asset(object):
    """An asset represents anything that can be traded.

    This class can represent both main assets and derivatives.

    Attributes:
        name: A string representing the name of the asset.
        symbol: A string representing the symbol of the asset.
        expiration_date: A string 'YYYY-mm-dd' representing the
            expiration date of the asset, if any.
        underlying_assets: A list of Asset objects representing the
            underlying assets of this asset, it any.
        ratio: A number representing the ratio to which whis asset
            relates to its underlying assets.
    """

    def __init__(
            self,
            name=None,
            symbol=None,
            expiration_date=None,
            underlying_assets=None,
            ratio=1
        ):
        self.name = name
        self.symbol = symbol
        self.expiration_date = expiration_date
        if underlying_assets is None:
            underlying_assets = []
        self.underlying_assets = underlying_assets
        self.ratio = ratio


class Occurrence(object):
    """An occurrence with an asset in a date."""

    __metaclass__ = ABCMeta

    def __init__(self, asset, date):
        self.asset = asset
        self.date = date

    @abstractmethod
    def update_container(self, container):
        """Should udpate the quantity, price and/or results."""
        raise NotImplementedError


class Portfolio(object):
    """A portfolio of assets.

    A portfolio is a collection of Accumulator objects.
    It can receive Operation objects and update the corresponding
    accumulators.

    Attributes:
        assets: A dict {Asset.symbol: Accumulator}.
        tasks: The tasks the portfolio will execute when accumulating.
    """

    def __init__(self):
        self.assets = {}
        self.tasks = []

    def accumulate(self, operation):
        """Accumulate an operation on its corresponding accumulator."""
        self.run_tasks(operation)
        symbol = operation.asset.symbol
        if operation.accumulate_underlying_operations:
            for underlying_operation in operation.operations:
                self.accumulate(underlying_operation)
        else:
            if symbol not in self.assets:
                self.assets[symbol] = Accumulator(operation.asset)
            self.assets[symbol].accumulate_occurrence(operation)

    def run_tasks(self, operation):
        """Execute the defined tasks on the Operation.

        Any function listed in self.tasks will be executed.
        This runs before the call to Accumulator.accumulate().
        """
        for task in self.tasks:
            task(operation, self)


class Accumulator(object):
    """An accumulator of quantity @ some average price.

    It can accumulate a series of operations and events with an Asset
    and update its quantity, average price and results based on the
    occurrences it accumulates.

    Attributes:
        asset: An asset instance, the asset whose data are being
            accumulated.
        date: A string 'YYYY-mm-dd' representing the date of the last
            status change of the accumulator.
        quantity: The asset's accumulated quantity.
        price: The asset's average price for the quantity accumulated.
        results: A dict with the total results from the operations
            accumulated. It follows the format:
            {
                'result name': result_value,
                ...
            }
        logging: A boolean indicating if the accumulator should log
            the data passed to the methods accumulate_occurrences() and
            accumulate_occurrence().
        log: A dict with all the operations performed with the asset,
            provided that self.logging is True.
    """

    def __init__(self, asset=None, logging=False):
        """Creates a instance of the accumulator.

        Logging by default is set to False; the accumulator will not
        log any operation, just accumulate the quantity and calculate
        the average price and results related to the asset after each
        call to accumulate_occurrence() and accumulate_occurrence().
        """
        self.asset = asset
        self.date = None
        self.quantity = 0
        self.price = 0
        self.results = {}
        self.logging = logging
        self.log = {}

    def accumulate_occurrence(self, occurrence):
        """Accumulates operation data to the existing position."""
        occurrence.update_container(self)
        if self.logging:
            self.log_occurrence(occurrence)

    def log_occurrence(self, operation):
        """Log Operation, Daytrade and Event objects.

        If logging, this method is called behind the scenes every
        time the methods accumulate_occurrence() or accumulate_occurrence()
        are called. The occurrences are logged like this:
        {
            'YYYY-mm-dd': {
                'position': {
                    'quantity': float
                    'price': float
                }
                'occurrences': [operation, ...],
            },
            ...
        }
        """
        if operation.date not in self.log:
            self.log[operation.date] = {'occurrences': []}
        self.log[operation.date]['position'] = {
            'quantity': self.quantity,
            'price': self.price,
        }
        self.log[operation.date]['occurrences'].append(operation)


class Operation(Occurrence):
    """An operation represents the purchase or the sale of an asset.

    Attributes:
        date: A string 'YYYY-mm-dd', the date the operation occurred.
        asset: An Asset instance, the asset that is being traded.
        quantity: A number representing the quantity being traded.
            Positive quantities represent a purchase.
            Negative quantities represent a sale.
        price: The raw unitary price of the asset being traded.
        commissions: A dict of discounts. String keys and float values
            representing the name of the discounts and the values
            to be deducted added to the the operation value.
        fees: A dict of fees. string keys and float values
            representing the names of the fees and the values of the
            fees to be applied to the operation. Fee values are
            always represented as a percentage. Fees are applied
            based on the volume of the operation.
        update_position: A boolean indication if the operation should
            update the asset position or not.
        accumulate_underlying_operations: A boolean indicating if the
            operation's underlying operations should be accumulated
            or ignored by the Accumulator.
        Operations: A list of underlying operations that the operation
            may have.
    """

    # By default all Operations can
    # update a portfolio position.
    update_position = True

    # By default underlying operations
    # should not be accumulated.
    accumulate_underlying_operations = False

    # An operation may contain
    # multiple underlying operations.
    operations = None

    def __init__(
            self,
            quantity=0,
            price=0,
            date=None,
            asset=None
        ):
        super(Operation, self).__init__(asset, date)
        self.quantity = quantity
        self.price = price
        self.commissions = {}
        self.fees = {}
        self.raw_results = {}

    @property
    def results(self):
        """Return the results associated with the operation."""
        return self.raw_results

    @property
    def real_value(self):
        """Returns the quantity * the real price of the operation."""
        return self.quantity * self.real_price

    @property
    def real_price(self):
        """Returns the real price of the operation.

        The real price is the price with all commissions and fees
        already deducted or added.
        """
        return self.price + math.copysign(
            self.total_commissions_and_fees / self.quantity,
            self.quantity
        )

    @property
    def total_commissions_and_fees(self):
        """Returns the sum of all commissions and fees."""
        return self.total_commissions + self.total_fees_value

    @property
    def total_commissions(self):
        """Return the sum of all commissions of this operation."""
        return sum(self.commissions.values())

    @property
    def volume(self):
        """Returns the quantity of the operation * its raw price."""
        return abs(self.quantity) * self.price

    @property
    def total_fees_value(self):
        """Returns the total fee value for this operation."""
        return sum(
            [self.volume * value / 100  for value in self.fees.values()]
        )

    def update_container(self, container):
        """Update the accumulator status with the operation data."""

        # Operations may update the posions themselves,
        # or maybe its their underlying operations that
        # should update the position. This is determined
        # by the accumulate_underlying_operations
        # attribute on the Operation object.
        if self.accumulate_underlying_operations:

            # If its the underlying operations that should
            # update the position, then we iterate through
            # all underlying operations and let each one
            # of them update the accumulator's position.
            for underlying_operation in self.operations:
                underlying_operation.update_positions(container)

        # If its not the underlying_operations that should
        # update the position, them we try to use the operation
        # itself to update the accumulator's position.
        else:
            self.update_positions(container)

        # add whatever result was informed with or generated
        # by this operation to the accumulator results dict
        for key, value in self.results.items():
            if key not in container.results:
                container.results[key] = 0
            container.results[key] += value

    def update_positions(self, container):
        """Update the position of the accumulator with an Operation."""

        # Here we check if the operation asset is the same
        # asset of this Accumulator object; the accumulator
        # only accumulates operations that trade its asset.
        # We also check if the operation should update the
        # position; if all this conditions are met, then
        # the position is updated.
        update_position_condition = (
            self.asset == container.asset and
            self.update_position and
            self.quantity
        )
        if update_position_condition:

            # Define the new accumualtor quantity
            new_quantity = container.quantity + self.quantity

            # if the quantity of the operation has the same sign
            # of the accumulated quantity then we need to
            # find out the new average price of the asset
            if same_sign(container.quantity, self.quantity):
                container.price = average_price(
                    container.quantity,
                    container.price,
                    self.quantity,
                    self.real_price
                )

            # If the traded quantity has an opposite sign of the
            # asset's accumulated quantity and the accumulated
            # quantity is not zero, then there was a result.
            elif container.quantity != 0:

                # check if we are trading more than what
                # we have on our portfolio; if yes,
                # the result will be calculated based
                # only on what was traded (the rest create
                # a new position)
                if abs(self.quantity) > abs(container.quantity):
                    result_quantity = container.quantity * -1

                # If we're not trading more than what we have,
                # then use the operation quantity to calculate
                # the result
                else:
                    result_quantity = self.quantity

                # calculate the result of this operation and add
                # the new result to the accumulated results
                results = \
                    result_quantity * container.price - \
                    result_quantity * self.real_price
                if results:
                    self.results['trades'] = results

                # If the new accumulated quantity has a different
                # sign of the old accumulated quantity then the
                # average price is now the price of the operation
                # If the new accumulated quantity is of the same sign
                # of the old accumulated quantity, the average of price
                # will not change.
                if not same_sign(container.quantity, new_quantity):
                    container.price = self.real_price

            # If the accumulated quantity was zero then
            # there was no result and the new average price
            # is the price of the operation
            else:
                container.price = self.real_price

            # update the accumulator quantity
            # with the new quantity
            container.quantity = new_quantity

            # If the accumulator is empty
            # the price is set back to zero
            if not container.quantity:
                container.price = 0


class OperationContainer(object):
    """A container for operations.

    An OperationContainer is used to group operations that occurred on
    the same date and then perform tasks on them.

    The main task task of the OperationContainer is to fetch the
    resulting positions from a group of Operations.

    This is achieved by calling this method:

        fetch_positions()

    Every time fetch_positions() is called the OperationContainer
    execute this tasks behind the scenes:

    - Execute all tasks defined in self.tasks. By default, no task is
      listed. Tasks are functions like this:

            def some_task(container)

      that receive an OperationContainer object and perform some work
      on the container data.

    - Create positions in self.positions for all operations in
      the container. Positions are all the operations with the same
      asset grouped in a single operation.

    - Prorate the commissions, if any, proportionally for all positions
      by calling:

        prorate_commissions()

    - Find the fees, if any, for the positions by calling:

        find_fees_for_positions()

    Attributes:
        date: A string 'YYYY-mm-dd' representing the date of the
            operations on the container.
        operations: A list of Operation instances.
        commissions: A dict with discount names and values to be
            deducted from the operations.
        positions: a dict of positions with this format:
            self.positions = {
                'position type': {
                    Asset.symbol: Operation,
                    ...
                },
                ...
            }
        tasks: a list of functions. The functions will
            be called in the order they are defined in this list when
            fetch_positions() is called. Every listed function must
            receive a OperationContainer object. They are like this:
                def some_task(container):
                    #do some stuff with container...
            The functions may change the Operation objects in
            self.operations, if needed (like when you separate
            daytrades from other operations).
    """

    volume = 0

    def __init__(self, operations=None, commissions=None):
        if operations is None:
            operations = []
        if commissions is None:
            commissions = {}
        self.operations = operations
        self.commissions = commissions
        self.trading_fees = TradingFees
        self.positions = {}
        self.tasks = []

    @property
    def total_commission_value(self):
        """Returns the sum of the values of all commissions."""
        return sum(self.commissions.values())

    def fetch_positions(self):
        """Fetch the positions resulting from the operations.

        This method executes all the methods defined in self.tasks
        in the order they are listed.

        Then it reads the self.operations list and add any remaining
        operation to the self.positions.

        And finally it checks if there are any fees to be applied
        to the positions.
        """
        self.volume = sum(operation.volume for operation in self.operations)

        raw_operations = copy.deepcopy(self.operations)

        # Execute all defined tasks
        for task in self.tasks:
            task(self)

        # fetch the positions from the remaining operations
        for operation in self.operations:
            if operation.quantity != 0:
                self.add_to_position_operations(operation)

        # prorate the commission for the operations
        self.prorate_commissions()

        # Add fees to the operations
        self.find_trading_fees_for_positions()

        self.operations = raw_operations

    def add_to_position_operations(self, operation):
        """Adds an operation to the common operations list."""
        if 'operations' not in self.positions:
            self.positions['operations'] = {}
        if operation.asset.symbol in self.positions['operations']:
            merge_operations(
                self.positions['operations'][operation.asset.symbol],
                operation
            )
        else:
            self.positions['operations'][operation.asset.symbol] = operation

    def prorate_commissions(self):
        """Prorates the container's commissions by its operations.

        This method sum the discounts in the commissions dict of the
        container. The total discount value is then prorated by the
        daytrades and common operations based on their volume.
        """
        for position_value in self.positions.values():
            for position in position_value.values():
                if position.operations:
                    for operation in position.operations:
                        self.prorate_commissions_by_position(operation)
                else:
                    self.prorate_commissions_by_position(position)

    def prorate_commissions_by_position(self, operation):
        """Prorates the commissions of the container for one operation.

        The ratio is based on the container volume and the volume of
        the operation.
        """
        if operation.volume != 0 and self.volume != 0:
            percent = operation.volume / self.volume * 100
            for key, value in self.commissions.items():
                operation.commissions[key] = value * percent / 100

    def find_trading_fees_for_positions(self):
        """Finds the fees for all positions in the container."""
        for position_type, position_value in self.positions.items():
            for position in position_value.values():
                if position.operations:
                    for operation in position.operations:
                        operation.fees = self.trading_fees.get_fees(
                            operation, position_type
                        )
                else:
                    position.fees = self.trading_fees.get_fees(
                        position, position_type
                    )


class TradingFees(object):
    """Responsible for finding fees for an operation.

    A TradingFees class returns the correspondent percentual fee for
    an Operation. This base TaxManager implements a dummy interface
    that will return a empty set of fees every time it is called.

    Every OperationContainer has a reference to this class. If you
    need to implement fees in your application you must create your
    own TradingFees implementation and then replace the reference in
    the OperationContainer object by doing this:

        container.trading_fees = YourTradingFees

    Your TradingFees implementation must obey this class interface.
    """

    __metaclass__ = ABCMeta

    @classmethod
    @abstractmethod
    def get_fees(cls, operation=None, operation_type=None):
        """Returns a set of fees (percentages) for a given operation."""
        return {}
