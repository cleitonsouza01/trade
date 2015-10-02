# Operations

An operation represents the purchase or sale of an asset.

Operations have a reference a to an Asset object, and also quantity and a price.
The price represents the unitary price of the asset that is being traded.
They may also have a date representing the date the operation occurred.

Operation can include commissions and rates that will be considered on the total
value of the operation and on the unitary price of the asset that is being
traded.

Creating Operation objects:
```python
import trade
operation = trade.Operation(
    asset=trade.Asset(symbol='GOOG')
    quantity=10
    price=1.4
    date='2015-09-25'
)
```

Check the [API docs](../api) for more on this.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
