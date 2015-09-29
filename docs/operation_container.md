# The Operation Container
A container for operations.

The OperationContainer was designed to execute tasks on groups of
operations. Its common uses are:

- To group all operations that happened on the same date
- To identify the daytrades among the operations
- Prorate commissions and other costs by all the operations
- Find rates for the operations, if needed
- To group all daytrades and common operations with the same asset on a single
operation, if any, and on a single daytrade, if any.

## Commissions
The container prorates fixed commissions by its operations based on their volume.

### How commissions work in the trade module
text...

Read more about this in [Commissions and Rates](./commissions_and_rates).  
Read more about this in the [API docs](./api/trade.operation_container).


## Rates
By default all OperationContainer objects have a reference to a TaxManager
object. This default tax manager will always return an empty dictionary.
If you need to apply volume-based percentual fees to your operations, you must
read this: [Commissions and Rates](./commissions_and_rates)

### How rates work in the trade module
text...

Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
