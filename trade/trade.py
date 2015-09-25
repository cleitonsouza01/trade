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
import copy

from .tax_manager import TaxManager
from .utils import (
    average_price, daytrade_condition, same_sign, find_purchase_and_sale
)


class Asset:
    """An asset represents anything that can be traded.

    Attributes:
        name: A string representing the name of the asset.
        expiration_date: A string 'YYYY-mm-dd' representing the
            expiration date of the asset, if any.
    """

    def __init__(self, name='', expiration_date=None):
        self.name = name
        self.expiration_date = expiration_date

    def __deepcopy__(self, memo):
        return self


class Operation:
    """An operation represents the purchase or sale of an asset.

    Attributes:
        date: A string 'YYYY-mm-dd', the date the operation occurred.
        asset: An Asset instance, the asset that is being traded.
        quantity: A number representing the quantity being traded.
        price: The raw unitary price of the asset being traded.
        comissions: A dict of discounts. String keys and float values
            representing the name of the discounts and the values
            to be deducted from the operation.
        taxes: A dict of taxes. string keys and float values
            representing the name of the taxes and the percentual
            values of the taxes to be applyed to the operation.
            Taxes are applyed based on the volume of the operation.
    """

    def __init__(self, quantity, price,
                    date=None, asset=None, comissions=None, taxes=None):
        self.date = date
        self.asset = asset
        self.quantity = quantity
        self.price = price
        if comissions is None: comissions={}
        if taxes is None: taxes={}
        self.comissions = comissions
        self.taxes = taxes

    #FIXME nao pode ser abs()!!!!!!
    @property
    def real_value(self):
        """Return the quantity * the real price of the operation."""
        return abs(self.quantity) * self.real_price

    @property
    def real_price(self):
        """Return the real price of the operation.

        The real price is the price with all comissions and taxes
        already deducted or added.
        """
        return self.price + math.copysign(
                                self.total_comission / self.quantity,
                                self.quantity
                            ) + math.copysign(
                                    self.total_tax_value / self.quantity,
                                    self.quantity
                                )

    @property
    def total_comission(self):
        """Return the sum of all comissions included in this operation."""
        return sum(self.comissions.values())

    @property
    def volume(self):
        """Return the quantity of the operation * its raw price."""
        return abs(self.quantity) * self.price

    @property
    def total_tax_value(self):
        tax_value = 0
        for value in self.taxes.values():
            tax_value += self.volume * value / 100
        return tax_value


class Daytrade:
    """A daytrade operation.

    Daytrades are operations of purchase and sale of an Asset on
    the same date.

    Attributes:
        asset: An asset instance, the asset that is being traded.
        quantity: The traded quantity of the asset.
        buy: A Operation instance representing the purchase of the
            asset.
        sale: A Operation instance representing the sale of the asset.
    """

    # TODO docstring explaining the creation of the
    #       purchase and sale operations
    def __init__(self, date, asset, quantity, buy_price, sale_price):
        self.date = date
        self.asset = asset
        self.quantity = quantity
        self.purchase = Operation(
            date=date,
            asset=asset,
            quantity=quantity,
            price=buy_price
        )
        self.sale = Operation(
            date=date,
            asset=asset,
            quantity=quantity*-1,
            price=sale_price
        )

    @property
    def result(self):
        return self.sale.real_value - self.purchase.real_value
