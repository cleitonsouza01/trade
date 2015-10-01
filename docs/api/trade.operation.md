# trade.operation

This module contains the class definitions of Operation.
You can use it by just:

```python
import trade
operation = trade.Operation(args...)
```


## trade.operation.Operation
An operation represents the purchase or the sale of an asset.

### Attributes:  
+ date: A string 'YYYY-mm-dd', the date the operation occurred.
+ asset: An Asset instance, the asset that is being traded.
+ quantity: A number representing the quantity being traded.
    - Positive quantities represent a purchase.
    - Negative quantities represent a sale.
+ price: The raw unitary price of the asset being traded.
+ comissions: A dict of discounts. String keys and float values
  representing the name of the discounts and the values
  to be deducted from the operation.
+ rates: A dict of rates. string keys and float values
  representing the names of the fees and the values of the
  fees to be applied to the operation. Rate values are always
  represented as a percentage. Rates are applied based on the
  volume of the operation.

### Properties:

#### real_value(self):
    """Returns the quantity * the real price of the operation.

#### real_price(self):
Returns the real price of the operation.

The real price is the price with all commissions and rates
already deducted or added.

#### total_commissions(self):
Return the sum of all commissions and rates included in this operation.

#### total_commissions(self):
Return the sum of all commissions included in this operation.

#### volume(self):
Returns the quantity of the operation * its raw price.

#### total_rates_value(self):
Returns the total rate value for this operation.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
