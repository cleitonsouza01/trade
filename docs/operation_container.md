# The Operation Container
A container for operations.

The OperationContainer was designed to fetch the positions resulting from a
group of operations. The operations are informed "raw", and the container is
then used to perform tasks like identify daytrades, prorate commissions and
so on.

After the OperationContainer performs its tasks, its operations are ready
to be accumulated on the Portfolio.

The OperationContainer behavior can be changed via plugins. The trade module
provides plugins for daytrade identification and option exercises, among other
things.


## Commissions
The container prorates fixed commissions by its operations based on their volume.

### How commissions work in the trade module
Commissions have their raw value deducted or added to Operations.

Read more about this in [Commissions and Rates](./commissions_and_rates).  
Read more about this in the [API docs](./api/trade.operation_container).


## Rates
By default all OperationContainer objects have a reference to a TaxManager
object. This default tax manager will always return an empty dictionary.
If you need to apply volume-based rates to your operations, you must
read this: [Commissions and Rates](./commissions_and_rates)

### How rates work in the trade module
Rates are represented as percentages, and their actual value is calculated
based on the operation volume (quantity * price).

Read more about this in [Commissions and Rates](./commissions_and_rates).  
Read more about this in the [API docs](./api/trade.operation_container).


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
