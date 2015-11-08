# trade: Tools For Stock Trading Applications.

## Part 3: Pre-processing operations: The Operation Container
Now that we can create operations and accumulate their results on our
portfolio, let's do some pre-processing on the operations before we
accumulate them.

We will use the OperationContainer class to group some Operations, perform
some tasks on them, and then accumulate the changed operations on our
portfolio.

So now we can create operations and accumulate then on a Portfolio like this:

```python
import trade

# create the asset
asset = trade.Asset(symbol='GOOGL')

# create the purchase operation buying 10 stocks
purchase = trade.Operation(
    subject=asset,
    quantity=10,
    price=50.4,
    date='2015-10-01'
)
# create the sale operation selling 5 stocks
sale = trade.Operation(
    subject=asset,
    quantity=-5,
    price=52.39,
    date='2015-10-02'
)

# Create the portfolio object
portfolio = trade.Portfolio()

# Accumulate the operations on the portfolio
portfolio.accumulate(sale)
portfolio.accumulate(purchase)
```

But in many cases you need to perform certain tasks on the operations before
accumulating them on your portfolio. You usually have brokerage commissions,
rates and operating costs that you need to apply to your operations. You may
also need to identify certain types of operations and process them differently,
like daytrades and operations like option exercises.

That's where the OperationContainer comes; it is used to group operations that
happened on the same date, and them perform tasks on them.

After these tasks are performed, all operations with the same asset are grouped
in a single operation. This is called a position. A position, in this context,
is just an Operation object that have the sum of all quantities traded on that
day with that asset, and the average price of all operations.

It would look like this:

```python
import trade

# create some assets
asset = trade.Asset(symbol='GOOGL')
other_asset = trade.Asset(symbol='AAPL')

# create the purchase operation buying 10 stocks
purchase = trade.Operation(
    subject=asset,
    quantity=10,
    price=10,
    date='2015-10-01'
)
# create another purchase operation, again buying 10 stocks,
# but with a different price
other_purchase = trade.Operation(
    subject=asset,
    quantity=10,
    price=20,
    date='2015-10-01'
)
# create a purchase operation buying 10 stocks
# of some other asset
other_asset_purchase = trade.Operation(
    subject=other_asset,
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
```

When fetch_positions() is called the OperationContainer executes all
the tasks that it is programmed to. By default it just executes 1 task:
to group all operations with the same asset on a single operation.

The generated positions will be stored on the OperationContainer
positions attribute, a dictionary indexed by the type of position. By default
the operation container identifies all operations as 'operations', so
the positions attribute now would look like this:

{
    'operations': {...}
}

On the value indexed by 'operations' there is another dictionary, this
one indexed by Asset objects. Each item in this dictionary represents one
Operation with an Asset. It is something like this:

{
    'operations':  {
        <Asset.symbol>: <Operation>,
        ...
    }
}

So, after the previous example, after fetch_positions() is called, if we
check our OperationContainer object positions we would see this:

```python

# Check each position
print(container.positions['operations']['GOOGL'].subject.symbol)
#> GOOGL
print(container.positions['operations']['GOOGL'].quantity)
#> 20
print(container.positions['operations']['GOOGL'].price)
#> 15

print(container.positions['operations']['AAPL'].subject.symbol)
#> AAPL
print(container.positions['operations']['AAPL'].quantity)
#> 10
print(container.positions['operations']['AAPL'].price)
#> 10
```

The OperationContainer can be extended with plugins to perform other tasks
before fetching the positions. This plugins can create new kings of positions
and also execute custom tasks on the operations, like identifying daytrades,
which is the next part of this tutorial.

Now that we can pre-process operations before accumulating them, we can move
on to the next part of this tutorial:
[Pre-processing operations: Daytrades](part_4).



## License
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
