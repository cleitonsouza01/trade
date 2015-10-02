# Assets

An asset represents anything that can be traded.

A asset can have a name, a symbol and a expiration date indicating when the
asset should cease to exist.

Creating Asset objects:
```python
import trade

# A real-world stock traded on NASDAQ
real_world_asset = trade.Asset(name='Apple Inc', symbol='AAPL')

```

Check the [API docs](../api) for more on this.


## Options
The trade module comes with a plugin for Options, which are a subclass
of Derivative.

Check the [API docs](../api) for more on this.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
