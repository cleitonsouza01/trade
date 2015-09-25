# Events

Events can change the quantity, the price and the results stored in
the accumulator. Every event must inherit from the accumulator.Event
base class and have this method:
```python
update_portfolio(quantity, price, results)
    # do stuff here...
    return quantity, price
```
that implements the logic for the change in the portfolio.

Events are passed to trade.Accumulator objects by the accumulate_event
method.

An event subclass representing a stock split could look like this:

```python
class StockSplit(Event):

    def __init__(self, name, factor):
        self.factor = factor
        self.name = name

    def update_portfolio(self, quantity, price, results):
        quantity = quantity * self.factor
        price = price / self.factor
        return quantity, price
```

Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
