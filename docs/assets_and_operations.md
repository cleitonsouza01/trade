# Assets and Operations

Assets and Operations are the base of the trade module.


## Assets
An asset represents anything that can be traded.

A asset can have a name and a expiration date indicating when the
asset should cease to exist.

Creating Asset objects:
```python
import trade
asset = trade.Asset()
other_asset = trade.Asset('other asset')
even_other_asset = trade.Asset('even other asset', expiration_date='2015-12-31')
```

Check the API docs for more on this.


## Operations
An operation represents the purchase or sale of an asset.

Operations have a reference a to an Asset object, and also quantity and a price. They may also have a date representing the date the operation occurred.

Creating Operation objects:
```python
import trade
asset = trade.Asset()
operation = Operation(
    asset=asset
    quantity=10
    price=1.4
    date='2015-09-25'
)
```

Check the API docs for more on this.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
