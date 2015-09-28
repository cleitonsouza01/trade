# The Operation Container
A container for operations.

The OperationContainer was designed to execute tasks on groups of
operations. Its common uses are:

- To group all operations that happened on the same date
- To identify the daytrades among the operations
- Prorate commissions and other costs by all the operations
- Find the taxes to be applied to all the operations
- To group all daytrades and common operations with the same asset on a single
operation, if any, and on a single daytrade, if any.

## Commissions
The container prorates commissions by its operations based on their volume.

Read more about this in [Commissions and Taxes](./commissions_and_fees).  
Read more about this in the [API docs](./api/trade.operation_container).


## Fees
By default all OperationContainer objects have a reference to a TaxManager
object. This default tax manager will always return an empty dictionary of fees.
If you need to apply fees to your operations, you must read this: [Commissions and Fees](./commissions_and_fees)


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
