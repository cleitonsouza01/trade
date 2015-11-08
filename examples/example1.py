"""Example of the use of Accumulators"""

from __future__ import absolute_import
from __future__ import print_function

import trade

# create the asset that we are going to trade
asset = trade.Asset(name='Google Inc', symbol='GOOGL')

# create the accumulator to accumulate trades with the asset
accumulator = trade.Accumulator(asset)


print(accumulator.subject.name)
#>> Some asset

print(accumulator.state['quantity'])
#>> 0

print(accumulator.state['price'])
#>> 0

print(accumulator.state['results'])
#>> {}


# create a trade operation buying the asset
purchase = trade.Operation(
    subject=asset,
    quantity=10,
    price=650.73,
    date='2015-09-23'
)

# accumulate the trade
accumulator.accumulate(purchase)


print(accumulator.state['quantity'])
#>> 10

print(accumulator.state['price'])
#>> 650.73

print(accumulator.state['results'])
#>> {}


# create a new trade operation selling the asset
sale = trade.Operation(
    subject=asset,
    quantity=-5,
    price=656.77,
    date='2015-09-24'
)

# accumulate the new trade
accumulator.accumulate(sale)


print(accumulator.state['quantity'])
#>> 5

print(accumulator.state['price'])
#>> 650.73

print(accumulator.state['results'])
#>> {'trades': 30.199999999999818}
