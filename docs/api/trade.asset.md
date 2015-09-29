# trade.asset

This module contains the class definitions of Asset, Derivative and Option.
You can use them by just:

```python
import trade
asset = trade.Asset()
```


## trade.asset.Asset
An asset represents anything that can be traded.

### Attributes:
+ name: A string representing the name of the asset.
+ symbol: A string representing the symbol of the asset.
+ expiration_date: A string 'YYYY-mm-dd' representing the expiration date of the asset, if any.

### Methods:

#### _ _ init _ _ (self, name=None, symbol=None, expiration_date=None):

#### _ _ deepcopy _ _ (self, memo)
Assets always return a reference to themselves when being copied, so they
are never really copied.


## trade.asset.Derivative(Asset):
A derivative is a asset which derives from one or more assets.

Derivatives have all the asset attributes and can be traded like
normal assets.

This is a base class for derivatives.

### Attributes:
+ name: A string representing the name of the asset.
+ symbol: A string representing the symbol of the asset.
+ expiration_date: A string 'YYYY-mm-dd' representing the expiration date of the derivative, if any.
+ underlying_assets: A list of Asset objects representing the underlying assets of this derivative.
+ ratio: By default the ratio is 1, so 1 derivative = 1 underlying asset.


## trade.asset.Option(Derivative):
Represents an Option.
This class represents both calls and puts.

### Methods:

#### exercise(self, quantity, price, date):
Exercises the option.

Returns two operations:
- one operation with zero value representing the option being consumed by the exercise;
- one operation representing the purchase or sale of the underlying asset


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
