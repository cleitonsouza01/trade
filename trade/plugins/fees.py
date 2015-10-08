"""Trading fees.

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

from abc import ABCMeta, abstractmethod


def find_trading_fees_for_positions(container):
    """Finds the fees for all positions in the container."""
    for position_type, position_value in container.positions.items():
        for position in position_value.values():
            if position.operations:
                for operation in position.operations:
                    operation.commissions.update(
                        container.trading_fees.get_fees(
                            operation, position_type
                        )
                    )
            else:
                position.commissions.update(
                    container.trading_fees.get_fees(
                        position, position_type
                    )
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
