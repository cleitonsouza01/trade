# trade

trade is a Python module with functions and classes for the development
of investment applications in Python. It provides basic notions of assets,
operations, daytrades, cost deduction, asset accumulation and taxes.

## Classes available:
+ [trade.Asset](trade.asset)  
  Representing assets.
+ [trade.Derivative](trade.asset)  
  A base class for derivatives.
+ [trade.Option](trade.asset)  
  Representing call and put options, a type of derivative.
+ [trade.Operation](trade.operation)  
  Representing operations with assets.
+ [trade.Daytrade](trade.operation)  
  Representing daytrade operations.
+ [trade.Exercise](trade.operation)  
  Representing option exercise operations.
+ [trade.OperationContainer](trade.operation_container)  
  To identify daytrades, prorate comissions and apply taxes to operations.
+ [trade.TaxManager](trade.tax_manager)  
  To get the right taxes for the operations on the container.
+ [trade.Accumulator](trade.accumulator)  
  To accumulate the assets and calculate the result from the trades.
+ [trade.Event](trade.event)  
  To change the asset's quantity and price on the accumulator.

## Functions available:

### Utils:
+ [trade.daytrade_condition(operation_a, operation_b)](trade.utils)
+ [trade.average_price(quantity_1, price_1, quantity_2, price_2)](trade.utils)
+ [trade.same_sign(x, y)](trade.utils)
+ [trade.find_purchase_and_sale(operation_a, operation_b)](trade.utils)

### Container tasks functions:
+ [prorate_comissions(operation_container)](trade.container_tasks):
+ [identify_daytrades_and_common_operations(operation_container)](trade.container_tasks)
+ [find_rates_for_positions(operation_container)](trade.container_tasks)
+ [get_operations_from_exercises(operation_container)](trade.container_tasks)
+ [extract_daytrade(operation_container, operation_a, operation_b)](trade.container_tasks)
+ [prorate_comissions_by_operation(operation_container, operation)](trade.container_tasks)
+ [add_to_common_operations(operation_container, operation)](trade.container_tasks)


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

# define the tasks the container will
# execute on fetch_positions()
container.tasks = [
    trade.identify_daytrades_and_common_operations,
    trade.prorate_commissions
]

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
+ [trade.asset](trade.asset) (Asset, Derivative, Option)
+ [trade.operation](trade.operation) (Operation, Daytrade, Exercise)
+ [trade.operation_container](trade.operation_container) (OperationContainer)
+ [trade.tax_manager](trade.tax_manager) (TaxManager)
+ [trade.utils](trade.utils) (all the utils)
+ [trade.container_tasks](trade.container_tasks) (all OperationContainer tasks)


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
