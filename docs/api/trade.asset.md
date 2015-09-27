# trade.asset

This module contains the class definitions of Asset and Derivative.
You can use them by just:

```python
import trade
asset = trade.Asset()
```


## trade.operation.Asset
An asset represents anything that can be traded.

Asset objects can be created with or without a name.

### Attributes:
+ name: A string representing the name of the asset.
+ expiration_date: A string 'YYYY-mm-dd' representing the expiration date of the asset, if any.

### Methods:

#### _ _ init _ _ (self, name='', expiration_date=None):
Asset objects can be created empty or with name and expiration date.

#### _ _ deepcopy _ _ (self, memo)
Assets always return a reference to themselves when being copied, so they
are never really copied.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
