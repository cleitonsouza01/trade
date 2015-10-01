# trade

trade is a Python module with functions and classes for the development
of investment applications in Python. It provides basic notions of assets,
operations, daytrades, cost deduction, asset accumulation and taxes.


## Classes available:

+ [trade.Asset](trade.asset)  
  Representing assets.
+ [trade.Derivative](trade.asset)  
  A base class for derivatives.
+ [trade.Operation](trade.operation)  
  Representing operations with assets.
+ [trade.OperationContainer](trade.operation_container)  
  To identify daytrades, prorate comissions and apply taxes to operations.
+ [trade.Portfolio](trade.portfolio)  
  To represent a portfolio of assets using a series of Accumulator objects.
+ [trade.TaxManager](trade.tax_manager)  
  To get the right taxes for the operations on the container.
+ [trade.Accumulator](trade.accumulator)  
  To accumulate the assets and calculate the result from the trades.
+ [trade.Event](trade.event)  
  To change the asset's quantity and price on the accumulator.


## Functions available:

### Utils:
+ [trade.average_price(quantity_1, price_1, quantity_2, price_2)](trade.utils)
+ [trade.same_sign(x, y)](trade.utils)


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
+ [trade.plugins.events](trade.plugins.events)
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

Check each module doc for more information.


## Modules in this package:

+ [trade.accumulator](trade.accumulator) (Accumulator)
+ [trade.event](trade.event) (Event)
+ [trade.asset](trade.asset) (Asset, Derivative)
+ [trade.operation](trade.operation) (Operation)
+ [trade.operation_container](trade.operation_container) (OperationContainer)
+ [trade.tax_manager](trade.tax_manager) (TaxManager)
+ [trade.utils](trade.utils) (all the functions)
+ [trade.plugins](plugins) (the default plugins: daytrades, options, events)


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
