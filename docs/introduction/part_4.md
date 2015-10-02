# trade: Tools For Stock Trading Applications.

## Part 4: Pre-processing operations: Daytrades
Now that we understand how to pre-process operations before accumulating
them on our portfolio, lets pre-process the operations to identify some
daytrades.

We will use the OperationContainer class to group some Operations and then
use the daytrades plugin that comes with the trade framework to identify
the daytrades and "extract" them from the Operation objects listed on the
OperationContainer.

Then we will accumulate the daytrades and the resulting common operations
on our Portfolio. Daytrades can be accumulated just like normal operations.

So now you can create operations, pre-process them and then accumulate them
on your portfolio like this:

```python
import trade

# create some assets
asset = trade.Asset(symbol='AAPL')
other_asset = trade.Asset(name='GOOGL')

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

```

But this is a simple case; real world operations can be much more complex than
that. On example of a more complex operation is a daytrade.

A daytrade is the operations of purchase and sale of the same asset on the same
day. So this would be a daytrade:

```python
import trade

# create the asset
asset = trade.Asset(symbol='ATVI')

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
                quantity=-10,
                price=52.39,
                date='2015-10-01'
            )
```

Daytrades are often treated very differently from common operations. Their
results usually are taxed differently, among other things. Sometimes they
are charged with different brokerage commissions, too.

To make things more complicated, this is also a daytrade in some contexts:

```python
import trade

# create the asset
asset = trade.Asset(symbol='ATVI')

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
                date='2015-10-01'
            )
```

Were out of this two operations we have a daytrade of 5 stocks being purchased
by 50.4 and sold by 52.39, and also a common purchase operation of 5 stocks for
50.4. In some stock markets around the world the purchase operation would be
taxed with two different rates; one relative to the purchase of 5 stocks in a
common operation, and other related to the daytrade purchase of 5 stocks.

If your context involves daytrades then you need to identify them before
passing the operations to the OperationContainer. For this the trade framework
comes pre-packed with a plugin to identify and process daytrades.

It is also a nice way of getting started using plugins; the trade module comes
pre-packed with a series of plugins, and you can create your own plugins or use
third-party plugins to suit your needs.

While all of this may have sounded complicated, to identify daytrades in the
trade module you just have to append a task to the operation container:

```python
import trade
import trade.plugins

# Create the operation container
container = trade.OperationContainer()

# Append the new task
container.tasks.append(trade.plugins.fetch_daytrades)
```

And now your container will identify all daytrades among your operations.
Daytrades create different positions on the OperationContainer positions
dictionary; they are indexed under the 'daytrades' key, and the Operations
are not Operation objects, but Daytrade objects. But you can treat them
the same way you treat opeations.

Using the previous example it would look like this:

```python
import trade
import trade.plugins

# create some assets
asset = trade.Asset(symbol='ATVI')

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
# resulting from this operations:
container.fetch_positions()

# create the portfolio
portfolio = trade.Portfolio()

# Accumulate every operation on the container positions.
for position in container.positions['common operations'].values():
    portfolio.accumulate(position)
for position in container.positions['daytrades'].values():
    portfolio.accumulate(position)

print(portfolio.assets['ATVI'].results)
#> {'daytrades': 9.949999999999989, 'trades': 0}
```


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
