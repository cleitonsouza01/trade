# trade: Tools For Stock Trading Applications.

## Part 1: Creating operations
This part of the tutorial shows how to create simple purchase and
sale operations.

So now you have the trade module installed, and you can create assets:

```python
import trade
asset = trade.Asset(symbol='GOOGL')
```

Assets are the base of the trade module. Everything will revolve around them;
they represent anything that can be traded. An asset may be created with many
attributes, but for now we will only give'em a name.

Operations are the acts of purchase or sale of an asset. A purchase operation
can be created like this:

```python
import trade

# create the asset
asset = trade.Asset(symbol='GOOGL')

# create the operation
operation = trade.Operation(
    asset=asset,
    quantity=10,
    price=50.4,
    date='2015-10-01'
)
```

Notice that the quantity is a positive value; it means that this is a purchase
operation.

A sale operation would look like this:
```python
import trade

# create the asset
asset = trade.Asset(symbol='GOOGL')

# create the operation
operation = trade.Operation(
    asset=asset,
    quantity=-10,
    price=52.39,
    date='2015-10-01'
)
```

Notice the negative value on the quantity. Negative quantity values are used
to represent a sale operation.

Now that you can create purchase and sale operations, you can move on to
the next part of the tutorial: [Part 2: Accumulating assets](part_2).


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
