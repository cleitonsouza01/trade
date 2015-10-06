from __future__ import absolute_import
from __future__ import print_function

import trade

# create the asset that we are going to trade
asset = trade.Asset(name='Google Inc', symbol='GOOGL')

# create the accumulator to accumulate trades with the asset
accumulator = trade.Accumulator(asset)


print(accumulator.asset.name)
#>> Some asset

print(accumulator.quantity)
#>> 0

print(accumulator.price)
#>> 0

print(accumulator.results)
#>> {'trades': 0}


# create a trade operation buying the asset
purchase = trade.Operation(
                asset=asset,
                quantity=10,
                price=650.73,
                date='2015-09-23'
            )

# accumulate the trade
accumulator.accumulate_occurrence(purchase)


print(accumulator.quantity)
#>> 10

print(accumulator.price)
#>> 650.73

print(accumulator.results)
#>> {'daytrades': 0, 'trades': 0}


# create a new trade operation selling the asset
sale = trade.Operation(
            asset=asset,
            quantity=-5,
            price=656.77,
            date='2015-09-24'
        )

# accumulate the new trade
accumulator.accumulate_occurrence(sale)


print(accumulator.quantity)
#>> 5

print(accumulator.price)
#>> 650.73

print(accumulator.results)
#>> {'daytrades': 0, 'trades': 30.199999999999818}
