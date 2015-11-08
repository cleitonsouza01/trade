# trade: Tools For Stock Trading Applications.

## Part 2: Accumulating assets
Now that we can create operations, let's create a series of operations
and let the trade module calculate the resulting position of the asset.

We will use the Portfolio class to accumulate the operations and create
our portfolio.

So now we have the trade module installed an can create purchase and
sale operations:

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
```

It is now that the trade module really comes to work. We are going to create
a Portfolio object to hold the operations and calculate their results.

Creating a Portfolio object is simple:

```python
import trade

portfolio = trade.Portfolio()
```

and your're done. Portfolios provide the method accumulate(), which is used
to receive an operation object and update the portfolio information regarding
thar asset. So, considering the sale and purchase operations that we created
before, we could use a Portfolio object to calculate the results of that
Operation and also the how much of the asset we still have in our Portfolio.

It would look like this:

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

Portfolios have a collection of Accumulator objects, one for each asset
the Portfolio accumulates. Every operation is accumulated on its corresponding
accumualtor according to the operation Asset. This process uses a Accumulator
object that we will discuss later. Right now, we can check the results of our
operations by just:

```python

# We informed two operations; one buying 10 stocks of an
# asset in 2015-10-01, and a second operations selling
# 5 stocks of that same asset on 2015-10-02. Now
# we check the asset's quantity on the accumulator:
print(portfolio.subjects['GOOGL'].state['quantity'])
#> 5

# The portfolio also calcultates the average price of the
# assets it is accumulating. In this case, as we just made
# a purchase and a sale, the average price still the same
# price of the purchase.
print(portfolio.subjects['GOOGL'].state['price'])
#> 50.4

# We sold the asset for a higher price than what it was bought;
# this generated a profit. We can check the results relative
# to each asset that is being accumulated on the Portfolio:
print(portfolio.subjects['GOOGL'].state['results'])
#> {'trades': 9.949999999999989}
```

Now that you can create operations and keep your assets on a portfolio, you can
move on to the next part of the tutorial:
[Part 3: Pre-processing operations](part_3).



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
