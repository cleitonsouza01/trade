# Assets and Operations

## Assets
An asset represents anything that can be traded.

### Attributes:
+ name: A string representing the name of the asset.


## Operations
An operation represents the purchase or sale of an asset.  

### Attributes:  
+ date: A string 'YYYY-mm-dd', the date the operation occurred.
+ asset: An Asset instance, the asset that is being traded.
+ quantity: A number representing the quantity being traded.
+ price: The raw unitary price of the asset being traded.
+ comissions: A dict of discounts. String keys and float values representing the name of the discounts and the values to be deducted from the operation.

### Properties:

#### real_value
Return the quantity * the real price of the operation.

#### real_price
Return the real price of the operation.

The real price is the price with all comissions and taxes already deducted or added.

#### total_comission
Return the sum of all comissions included in this operation.

#### volume
Return the quantity of the operation * its raw price.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
