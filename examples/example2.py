from __future__ import  print_function

import trade

# create the asset that we are going to trade
asset = 'Euro'

# create the accumulator to accumulate trades with the asset
accumulator = trade.Accumulator(asset)


print(accumulator.asset)
#>> Euro

print(accumulator.quantity)
#>> 0

print(accumulator.price)
#>> 0

print(accumulator.results)
#>> {'trades': 0}


# accumulate trade data
accumulator.accumulate(quantity=10, price=2, date='2015-09-22')


print(accumulator.quantity)
#>> 10

print(accumulator.price)
#>> 2.0

print(accumulator.results)
#>> {'trades': 0}


# accumulate more trade
accumulator.accumulate(quantity=-5, price=3, date='2015-09-23')


print(accumulator.quantity)
#>> 5

print(accumulator.price)
#>> 2.0

print(accumulator.results)
#>> {'trades': 5.0}
