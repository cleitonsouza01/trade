import trade

# create the asset that we are going to trade
asset = trade.Asset('Euro')

# create the accumulator to accumulate trades with the asset
accumulator = trade.Accumulator(asset)


print accumulator.asset.name
#>> Euro

print accumulator.quantity
#>> 0

print accumulator.price
#>> 0

print accumulator.results
#>> {'trades': 0}


# create a trade buying the asset
purchase = trade.Trade(asset=asset, quantity=10, price=2, date='2015-09-22')

# accumulate the trade
accumulator.accumulate_trade(purchase)


print accumulator.quantity
#>> 10

print accumulator.price
#>> 2.0

print accumulator.results
#>> {'trades': 0}


# create a new trade selling the asset
sale = trade.Trade(asset=asset, quantity=-5, price=3, date='2015-09-23')

# accumulate the new trade
accumulator.accumulate_trade(sale)


print accumulator.quantity
#>> 5

print accumulator.price
#>> 2.0

print accumulator.results
#>> {'trades': 5.0}
