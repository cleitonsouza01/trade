# The Operation Container
A container for operations.

The OperationContainer was designed to execute tasks on groups of
operations. Its common use is to:

- To group all operations that happened on the same date
- Identify the daytrades among the operations
- Prorate commissions and other costs by all the operations
- Find the taxes to be applied to all the operations
- To group all daytrades and common operations with the same asset on a single
operation, if any, and on a single daytrade, if any.

## Commissions
The container prorates commissions by its operations based on their volume.

Read more about this in [Commissions and Taxes](./commissions_and_taxes).  
Read more about this in the [API docs](./api/trade.operation_container).


## Taxes
By default all OperationContainer objects have a reference to a TaxManager
object. This default tax manager will always return an empty dictionary of taxes.
If you need to apply taxes to your operations, you must read this: [Commissions and Taxes](./commissions_and_taxes)


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
