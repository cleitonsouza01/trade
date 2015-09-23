import trade

# create the asset that we are going to trade
asset = 'Euro'

# create the accumulator to accumulate trades with the asset
accumulator = trade.AssetAccumulator(asset)


print accumulator.asset
#>> Euro

print accumulator.quantity
#>> 0

print accumulator.price
#>> 0

print accumulator.results
#>> {'trade': 0}


# accumulate trade data
accumulator.accumulate(quantity=10, price=2, date='2015-09-22')


print accumulator.quantity
#>> 10

print accumulator.price
#>> 2.0

print accumulator.results
#>> {'trade': 0}


# accumulate the new trade
accumulator.accumulate(quantity=-5, price=3, date='2015-09-23')


print accumulator.quantity
#>> 5

print accumulator.price
#>> 2.0

print accumulator.results
#>> {'trade': 5.0}
