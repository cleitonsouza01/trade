# Assets

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


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
