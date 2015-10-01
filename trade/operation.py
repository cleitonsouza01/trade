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
from __future__ import division

import math


class Operation:
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
            to be deducted from the operation.
        commission_rates: A dict of rates. string keys and float values
            representing the names of the rates and the values of the
            rates to be applied to the operation. Rate values are always
            represented as a percentage. Rates are applied based on the
            volume of the operation.
    """

    accumulate_underlying_operations = False

    def __init__(self, quantity, price,
                    date=None,
                    asset=None,
                    commissions=None,
                    rates=None,
                    results=None
                ):
        self.date = date
        self.asset = asset
        self.quantity = quantity
        self.price = price
        if commissions is None: commissions={}
        if rates is None: rates={}
        if results is None: results={'trades': 0} #FIXME compatibility
        self.commissions = commissions
        self.rates = rates
        self.results = results

        self.update_position = True
        """By default all Operations can update a portfolio position."""

        self.operations = []
        """An operation may contain multiple operations."""

    @property
    def real_value(self):
        """Returns the quantity * the real price of the operation."""
        return self.quantity * self.real_price

    @property
    def real_price(self):
        """Returns the real price of the operation.

        The real price is the price with all commissions and rates
        already deducted or added.
        """
        return self.price + math.copysign(
                            self.total_commissions_and_rates / self.quantity,
                            self.quantity
                        )

    @property
    def total_commissions_and_rates(self):
        """Returns the sum of all commissions and rates."""
        return self.total_commissions + self.total_rates_value

    @property
    def total_commissions(self):
        """Return the sum of all commissions of this operation."""
        return sum(self.commissions.values())

    @property
    def volume(self):
        """Returns the quantity of the operation * its raw price."""
        return abs(self.quantity) * self.price

    @property
    def total_rates_value(self):
        """Returns the total rate value for this operation."""
        return sum(
                [self.volume * value / 100  for value in self.rates.values()]
            )
