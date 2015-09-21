"""trade_tools: Tools To Work With Financial Data.

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

from __future__ import division

import math


class Asset:
	"""An asset.

    An asset represents anything that can be traded.

	Attributes:
        name: A string representing the name of the asset.
	"""

	def __init__(self, name=''):
		self.name = name


class Trade:
	"""A trade.

	A trade represents the purchase or sale of an asset.

	Attributes:
        date: A string 'YYYY-mm-dd' representing the date trade occurred
		asset: An Asset instance, the asset that is being traded.
		quantity: A number representing the quantity being traded.
		price: The raw unitary price of the trade.
		discounts: A dict containing numeric values to be deducted
			from the operation total value.
	"""

	def __init__(self, quantity, price,
					date=None, asset=None, discounts={}):
		self.date = date
		self.asset = asset
		self.quantity = quantity
		self.price = price
		self.discounts = discounts

	@property
	def real_value(self):
		return self.quantity * self.real_price

	@property
	def real_price(self):
		return self.price + math.copysign(
								self.total_discounts / self.quantity,
								self.quantity
							)

	@property
	def total_discounts(self):
		return sum(self.discounts.values())

	@property
	def volume(self):
		return abs(self.quantity) * self.price
