import trade

# create some assets
asset = trade.Asset(symbol='GOOG')
other_asset = trade.Asset(symbol='AAPL')

# create the purchase operation buying 10 stocks
purchase = trade.Operation(
                asset=asset,
                quantity=10,
                price=10,
                date='2015-10-01'
            )
# create another purchase operation, again buying 10 stocks,
# but with a different price
other_purchase = trade.Operation(
                asset=asset,
                quantity=10,
                price=20,
                date='2015-10-01'
            )
# create a purchase operation buying 10 stocks
# of some other asset
other_asset_purchase = trade.Operation(
                asset=other_asset,
                quantity=10,
                price=10,
                date='2015-10-01'
            )

# Create the operation container
container = trade.OperationContainer()

# Append all operations on the OperationContainer
# operations attribute, which is a list.
container.operations.append(purchase)
container.operations.append(other_purchase)
container.operations.append(other_asset_purchase)

# Run the container default method to fetch the positions
# resulting from this opeations:
container.fetch_positions()

# create the portfolio
portfolio = trade.Portfolio()

# Accumulate every operation on the container positions.
# Attribute
for position in container.positions['common operations'].values():
    portfolio.accumulate(position)

print(portfolio.assets)
