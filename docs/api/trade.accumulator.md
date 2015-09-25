# trade.accumulator


## trade.accumulator.Accumulator


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
