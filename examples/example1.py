import trade

# create the asset that we are going to trade
asset = trade.Asset('Euro')

# create the accumulator to accumulate trades with the asset
accumulator = trade.AssetAccumulator(asset)


print accumulator.asset.name
#>> Euro

print accumulator.quantity
#>> 0

print accumulator.price
#>> 0

print accumulator.results
#>> {'trade': 0}


# create a trade buying the asset
trade = trade.Trade(asset=asset, quantity=10, price=2, date='2015-09-22')

# accumulate the trade
accumulator.accumulate_trade(trade)
#accumulator.accumulate(trade.quantity, trade.price, date=trade.date)


print accumulator.quantity
#>> 10

print accumulator.price
#>> 2.0

print accumulator.results
#>> {'trade': 0}


# create a new trade selling the asset
trade = trade.Trade(asset=asset, quantity=-5, price=3, date='2015-09-23')

# accumulate the new trade
accumulator.accumulate_trade(trade)
#accumulator.accumulate(trade.quantity, trade.price, date=trade.date)


print accumulator.quantity
#>> 5

print accumulator.price
#>> 2.0

print accumulator.results
#>> {'trade': 5.0}
