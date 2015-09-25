# trade.trade

This module contains the class definitions of Asset, Operation,
OperationContainer and Daytrade. These classes are imported on
trade. _ _ init _ _ , so you can use them by just:

```python
import trade
asset = trade.Asset()
```


## trade.trade.Asset
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


## trade.trade.Operation
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


## trade.trade.OperationContainer
A container for operations.

An OperationContainer is used to group operations, like operations
that occurred on the same date, and then perform tasks on them. It
can:

- Separate the daytrades and the common operations of a group of
  operations that occurred on the same date by using the method:

    * identify_daytrades_and_common_operations()

- Prorate a group of taxes proportionally for all daytrades and
  common operations, if any, by using the method:

    * prorate_comissions_by_daytrades_and_common_operations()

### Attributes:
+ date: A string 'YYYY-mm-dd' representing the date of the operations on the container.
+ operations: A list of Operation instances.
+ comissions: A dict with discount names and values to be deducted from the operations.
+ daytrades: a dict of Daytrade objects, indexed by the daytrade asset.
+ common_operations: a dict of Operation objects, indexed by theoperation asset.

### Properties

#### total_comission_value(self):
Return the sum of values in the container comissions dict.

#### volume(self):
Return the total volume of the operations in the container.

### Methods

#### fetch_positions(self):
Fetch the positions resulting from the operations on the OperationContainer.

#### prorate_comissions_by_daytrades_and_common_operations(self):
Prorate the TradeContainer comissions by its operations.  

This method sums all discounts on the comissions dict of the  
accumulator. The total discount value is then prorated by the  
daytrades and common operations based on their volume.  

#### prorate_comissions_by_operation(self, operation):
Prorate the comissions of the container for one operation.  

The ratio is based on the container volume and the operation  
volume.

#### identify_daytrades_and_common_operations(self):
Separate operations into daytrades and common operations.  

The original operations list remains untouched. After the  
execution of this method, the container daytrades list and  
common_operations list will be filled with the daytrades  
and common operations found in the container operations list,  
if any.

#### extract_daytrade(self, operation_a, operation_b):
Extract the daytrade part of two operations.

1. Find what is the purchase and what is the sale
2. Find the daytraded quantity; the daytraded
quantity is always the smallest absolute quantity
3. Update the operations that originated the
daytrade with the new quantity after the
daytraded part has been extracted; One of
the operations will always have zero
quantity after this, being fully consumed
by the daytrade. The other operation may or
may not end with zero quantity.
4. create the Daytrade object
5. If this container already have a Daytrade
with this asset, we merge this daytrade
with the daytrade in self.daytrades -
in the end, there is only one daytrade per
asset per OperationContainer.

#### add_to_common_operations(self, operation):
Add a operation to the common operations list.

#### merge_operations(self, existing_operation, operation):
Merge one operation with another operation.


## trade.trade.Daytrade
A daytrade operation.

Daytrades are operations of purchase and sale of an Asset on
the same date.

### Attributes:
+ asset: An asset instance, the asset that is being traded.
+ quantity: The traded quantity of the asset.
+ buy: A Operation instance representing the purchase of the asset.
+ sale: A Operation instance representing the sale of the asset.

### Properties

#### result


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
