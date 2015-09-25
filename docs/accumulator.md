# The Accumulator
An accumulator of quantity @ some average price.

if created with log_operations=True the accumulator will log the
data and the results of every operation it accumulate.

Results are calculated by the accumulator according to the value
of the operations informed and the current status of the
accumulator (the current quantity and average price of the asset).

The method accumulate() can take a optional param 'results', a dict
with other results to be included in the accumulator results dict
and on the operation log.

## Attributes:
+ asset: An asset instance, the asset whose data are being
    accumulated.
+ date: A string 'YYYY-mm-dd' representing the date of the last
    status change of the accumulator.
+ quantity: The asset's accumulated quantity.
+ price: The asset's average price for the quantity accumulated.
+ results: A dict with the total results from the operations
    accumulated.
+ logging: A boolean indicating if the accumulator should log
    the calls to the accumulate() method.
+ log: A dict with all the operations performed with the asset,
    provided that self.logging is True.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
