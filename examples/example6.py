import trade
import trade.plugins

# create some assets
asset = trade.Asset(symbol='GOOGL')

purchase = trade.Operation(
                asset=asset,
                quantity=10,
                price=50.4,
                date='2015-10-01'
            )
# create the sale operation selling 5 stocks
sale = trade.Operation(
                asset=asset,
                quantity=-5,
                price=52.39,
                date='2015-10-01'
            )

# Create the operation container and append
# the task to identify daytrades
container = trade.OperationContainer()
container.tasks.append(trade.plugins.fetch_daytrades)

# Append all operations on the OperationContainer
# operations attribute, which is a list.
container.operations.append(purchase)
container.operations.append(sale)

# Run the container default method to fetch the positions
# resulting from this opeations:
container.fetch_positions()

# create the portfolio
portfolio = trade.Portfolio()

# Accumulate every operation on the container positions.
for position in container.positions['operations'].values():
    portfolio.accumulate(position)
for position in container.positions['daytrades'].values():
    portfolio.accumulate(position)

print(portfolio.assets['GOOGL'].results)
