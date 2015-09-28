# The Operation Container
A container for operations.

The OperationContainer was designed to execute tasks on groups of
operations. Its common uses are:

- To group all operations that happened on the same date
- To identify the daytrades among the operations
- Prorate fixed commissions and other costs by all the operations
- Find the volume-based commissions for the operations, if needed
- To group all daytrades and common operations with the same asset on a single
operation, if any, and on a single daytrade, if any.

## Fixed Commissions
The container prorates fixed commissions by its operations based on their volume.

Read more about this in [Commissions and Taxes](./commissions_and_fees).  
Read more about this in the [API docs](./api/trade.operation_container).


## Volume-Based Commissions
By default all OperationContainer objects have a reference to a TaxManager
object. This default tax manager will always return an empty dictionary.
If you need to apply volume-based percentual fees to your operations, you must
read this: [Commissions and Fees](./commissions_and_fees)


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
