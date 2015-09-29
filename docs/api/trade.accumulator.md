# trade.accumulator

## trade.accumulator.Accumulator
An accumulator of quantity @ some average price.

### Attributes:
+ asset: An asset instance, the asset whose data are being accumulated.
+ date: A string 'YYYY-mm-dd' representing the date of the last status change of the accumulator.
+ quantity: The asset's accumulated quantity.
+ price: The asset's average price for the quantity accumulated.
+ results: A dict with the total results from the operations accumulated.
+ logging: A boolean indicating if the accumulator should log the calls to the accumulate() method.
+ log: A dict with all the operations performed with the asset, provided that self.logging is True.

if created with logging=True the accumulator will log the every
operation it accumulates.

Results are calculated by the accumulator according to the value
of the operations informed and the current status of the
accumulator (the current quantity and average price of the asset).

### Methods:

#### init (self, asset, initial_status=None, logging=False):
Creates a instance of the accumulator.

A initial status (quantity, average price and results) can be
informed by passing a initial_status like this:
```python
    initial_status = {
        'date': 'YYYY-mm-dd'
        'quantity': float
        'price': float
        'results': {
            'result name': float,
            ...
        }
    }
```
Logging by default is set to False; the accumulator will not log any operation,
just accumulate the quantity and calculate the average price and results related
to the asset after each call to accumulate_operation(), accumulate_daytrade()
and accumulate_event().

If logging is set to True the accumulator will log the data passed on every call
to accumulate_operation(), accumulate_daytrade() and accumulate_event().

#### log_occurrence(self, occurrence):
Log Operation, Daytrade and Event objects.

If logging, this method is called behind the scenes every
time the method accumulate() is called. The occurrences are
logged like this:
```python
    self.log = {
        '2017-09-19': {
            'position': {
                'quantity': float
                'price': float
            }
            'occurrences': [Operation, ...],
        },
        ...
    }
```
#### accumulate_operation(self, operation):
Accumulates operation data to the existing position.

The accumulator takes care of adding any custom results already
present on the operation "results' attribute to the total
results of the stock in the accumulator.

#### accumulate_daytrade(self, daytrade):
Accumulates a Daytrade operation.

#### accumulate_event(self, event):
Receives a Event subclass instance and lets it do its work.

An event can change the quantity, price and results stored in
the accumulator.

The way it changes this information is up to the event object;
each Event subclass must implement a method like this:
```python
update_portfolio(quantity, price, results)
    # do stuff here...
    return quantity, price
```
that have the logic for the change in the accumulator's
quantity, price and results.


## trade.accumulator.Event
A portfolio-changing event.

Events can change the quantity, the price and the results stored in
the accumulator. This is a base class for Events; every event must
inherit from this class and have a method like this:

```python
    update_portfolio(quantity, price, results)
        # do stuff here...
        return quantity, price
```
that implements the logic for the change in the portfolio.



Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
