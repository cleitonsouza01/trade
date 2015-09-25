# trade.utils

This module contains functions that execute common tasks.
You can use them by just:

```python
import trade
trade.average_price(x,y)
```

and so on.


## trade.utils.daytrade_condition(operation_a, operation_b):
Check if the two operations configure a daytrade.
Returns True if the operations are a daytrade; False otherwise.


## trade.utils.average_price(quantity_1, price_1, quantity_2, price_2):
Calculate the average price between two positions.  
A position is the quantity of an asset and its average price.
Returns the calculated average price.


## trade.utils.same_sign(x, y):
Check if two numbers have the same sign.  
Return True if they have the same sign,  
False if they don't have the same sign,
and None if x or y are not numbers.


## find_purchase_and_sale(operation_a, operation_b):
Given two operations, find which is a purchase and which is a sale.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
