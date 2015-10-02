import trade

# create the asset
asset = trade.Asset(name='some asset')

# create the purchase operation buying 10 stocks
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
                date='2015-10-02'
            )

# Create the portfolio object
portfolio = trade.Portfolio()

# Accumulate the operations on the portfolio
portfolio.accumulate(sale)
portfolio.accumulate(purchase)

print(portfolio.assets[asset].quantity)
print(portfolio.assets[asset].price)
print(portfolio.assets[asset].results)
