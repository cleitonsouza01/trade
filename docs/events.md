# Events

Events can change the quantity, the price and the results of an asset
stored in the accumulator. Every event must inherit from the
accumulator.Event base class and have a method with this signature:

```python
update_portfolio(quantity, price, results)
    # do stuff here...
    return quantity, price
```

that implements the logic for the change in the portfolio.

Events must have an "asset" attribute with reference to an Asset
instance and a date 'YYYY-mm-dd' attribute. The accumulator uses
this information to correctly apply the event.

Events are passed to trade.Accumulator objects by the accumulate_event
method.

An event subclass representing a stock split could look like this:

```python
class StockSplit(Event):

    def __init__(self, asset, date, factor):
        self.asset = asset
        self.date = date
        self.factor = factor

    def update_portfolio(self, quantity, price, results):
        quantity = quantity * self.factor
        price = price / self.factor
        return quantity, price
```

Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
