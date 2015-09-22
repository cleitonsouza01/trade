trade_tools: Tools For Stock Trading Applications.
==================================================
Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com

Project repository:  
http://github.com/rochars/trade_tools


What is it?
-----------
trade_tools is a Python package with simple functions and classes for the
development of stock trading apps. It provides basic notions of assets,
trades, daytrades, cost deduction and functions related to processing stock
trading data.

You may use it as a framework to create applications that implement specific
rules of stock markets around the world or use it "as is" in any  application
that requires the notion of buying stuff, selling stuff and  controlling how
much you spent to buy and how much you profited from the trades.


How can I use it?
-----------------
A basic example:

```python
import trade_tools

# create the asset that we are going to trade
asset = trade_tools.Asset('Euro')

# create the accumulator to accumulate trades with the asset
accumulator = trade_tools.AssetAccumulator(asset)


print accumulator.asset.name
#>> Euro

print accumulator.quantity
#>> 0

print accumulator.price
#>> 0

print accumulator.results
#>> {'trade': 0}


# create a trade buying the asset
trade = trade_tools.Trade(asset=asset, quantity=10, price=2, date='2015-09-22')

# accumulate the trade
accumulator.accumulate_trade(trade)


print accumulator.quantity
#>> 10

print accumulator.price
#>> 2.0

print accumulator.results
#>> {'trade': 0}


# create a new trade selling the asset
trade = trade_tools.Trade(asset=asset, quantity=-5, price=3, date='2015-09-23')

# accumulate the new trade
accumulator.accumulate_trade(trade)


print accumulator.quantity
#>> 5

print accumulator.price
#>> 2.0

print accumulator.results
#>> {'trade': 5.0}
```

You may also use only the Accumulator and ignore everything else:
```python
import trade_tools

# create the accumulator to accumulate trades with the asset
accumulator = trade_tools.AssetAccumulator('Euro')


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


# accumulate new trade data
accumulator.accumulate(quantity=-5, price=3, date='2015-09-23')


print accumulator.quantity
#>> 5

print accumulator.price
#>> 2.0

print accumulator.results
#>> {'trade': 5.0}
```

The AssetAccumulator can also log the accumulated trades and their
specific results.

There are more ways of using it and more functionalities, like rating and
applying discounts automatically to a group of trades, separate daytrades
from common trades in a group of trades, calculating the resulting position
from a group of trades and so on. Check the documentation and the examples
for more information on how to use trade_tools.


What about compatibility?
-------------------------
trade_tools is compatible with Python 2.7 and on, including Python 3.x.


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
