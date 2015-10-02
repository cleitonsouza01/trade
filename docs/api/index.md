# trade
http://github.com/rochars/trade  
http://trade.readthedocs.org  

trade is a Python module with functions and classes for the development
of investment applications in Python. It provides notions of assets,
operations, daytrades, cost deduction, asset accumulation, rates and more.


## Classes available:

+ [trade.Asset](trade)  
  Representing assets.
+ [trade.Derivative](trade)  
  A base class for derivatives.
+ [trade.Operation](trade)  
  Representing operations with assets.
+ [trade.OperationContainer](trade)  
  To identify daytrades, prorate comissions and apply taxes to operations.
+ [trade.Portfolio](trade)  
  To represent a portfolio of assets using a series of Accumulator objects.
+ [trade.TaxManager](trade)  
  To get the right taxes for the operations on the container.
+ [trade.Accumulator](trade)  
  To accumulate the assets and calculate the result from the trades.
+ [trade.Event](trade)  
  To change the asset's quantity and price on the accumulator.


## Functions available:

+ [trade.average_price()](trade)
+ [trade.same_sign()](trade)


## Default plugins:

The trade module comes pre-packed with some plugins that add
functionalities related to common stock market operations.

You may use this plugins in your project or use them as a base
to create your own plugins.

+ [trade.plugins.options](plugins/trade.plugins.options)
  with classes for Options and Exercises and tasks for the
  OperationContainer and Portfolio.
+ [trade.plugins.daytrades](plugins/trade.plugins.daytrades)
  with the Daytrade class, a task for the OperationContainer
  and some helper functions.
+ [trade.plugins.events](plugins/trade.plugins.events)
  with classes representing stock splits, reverse stock splits and
  bonus shares.


## Basic example

```python
import trade

# create the asset and the operation
asset = trade.Asset(name='some asset')
operation = trade.Operation(
                date='2015-09-18',
                asset=asset,
                quantity=20,
                price=10
            )

# create a container with some
# commissions associated with it
commissions = {
    'some commission': 1,
    'other commission': 3,
}
container = trade.OperationContainer(
                operations=[operation],
                commissions=commissions
            )

# identify common operations and daytrades
# and prorate the comissions
container.fetch_positions()

# create an accumulator for the asset
accumulator = trade.Accumulator(asset)

# accumulate the operation
operation = container.common_operations[asset]
accumulator.accumulate_operation(operation)

print(accumulator.quantity)
#>>20

print(accumulator.price)
#>>10.2
# the original price (10) plus the commissions
# the OperationContainer prorated (default taxes are zero)

print(accumulator.price * accumulator.quantity)
#>>204
# 200 from the raw operation
# (20 quantity * 10 unitary price)
# + 4 from the total commissions
```


## Modules in this package:

+ [trade.trade](trade)
+ [trade.plugins](plugins)


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
