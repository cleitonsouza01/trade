# trade
http://github.com/rochars/trade  
http://trade.readthedocs.org  

This module contains the definitions of all default classes and functions of
the trade framework. You can use them by just:

```python
import trade
asset = trade.Asset(symbol='GOOGL')
```


## trade.Asset
An asset represents anything that can be traded.

### Attributes:
+ name: A string representing the name of the asset.
+ symbol: A string representing the symbol of the asset.
+ expiration_date: A string 'YYYY-mm-dd' representing the expiration date of the asset, if any.
+ underlying_assets: A list of Asset objects representing the underlying assets of the asset.
+ ratio: By default the ratio is 1, so 1 asset = 1 underlying asset.

### Methods:

#### _ _ init _ _ (self, name=None, symbol=None, expiration_date=None):


## trade.Event
A portfolio-changing event.

Events can change the quantity, the price and the results stored in
the accumulator. This is a base class for Events; every event must
inherit from this class and have a method like this:

```python
    update_container(self, accumulator)
        # do stuff here...
```

that implements the logic for the change in the accumulator.


## trade.Operation
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


## trade.OperationContainer
A container for operations.

An OperationContainer is used to group operations, like operations
that occurred on the same date, and then perform tasks on them.

The main task task that the OperationContainer can perform is to
identify the resulting positions from a group of operations. The
resulting positions are all operations separated as daytrades and
common operations, with all common operations and daytrades with
the same asset grouped into a single operation or a single
daytrade.

The resulting common operations and daytrades contains the
OperationContiner commissions prorated by their volumes, and also
any rates the OperationContainer TaxManager finds for them.

This is achieved by calling this method:

    fetch_positions()

Every time fetch_positions() is called the OperationContainer
execute this tasks behind the scenes:

- Execute all tasks defined in self.tasks.

- Create positions in self.positions for all operations in
  self.operations.

- Prorate the commissions, if any, proportionally for all positions
  by calling:

    prorate_commissions()

- Find the fees, if any, for the resulting positions by calling:

    find_fees_for_positions()

### Attributes:
+ date: A string 'YYYY-mm-dd' representing the date of the operations on the container.
+ operations: A list of Operation instances.
+ commissions: A dict with discount names and values to be deducted from the operations.
+ positions: a dict of positions with this format:
  self.positions = {  
      'position type': {  
          Asset.symbol: Operation,  
          ...  
      },  
      ...  
  }
+ tasks: a list of functions. The functions will
  be called in the order they are defined in this list when
  fetch_positions() is called. Every listed function must
  receive a OperationContainer object. They are like this:

  def some_task(container):  
      #do some stuff with container...  

  The functions may change the Operation objects in
  self.operations, if needed (like when you separate
  daytrades from other operations).

### Properties

#### total_comission_value(self):
Returns the sum of values of all commissions.

#### volume(self):
Returns the total volume of the operations in the container.

### Methods

#### fetch_positions(self):
Fetch the positions resulting from the operations.

This method executes all the methods defined on the
tasks attribute in the order they are
listed.

#### merge_operations(self, existing_operation, operation):
Merges one operation with another operation.

#### add_to_common_operations(self, operation):
Adds an operation to the common operations list.

#### prorate_commissions_by_positions(self, operation):
Prorates the commissions of the container for one operation.

The ratio is based on the container volume and the volume of
the operation.

#### prorate_commissions(self):
Prorates the container's commissions by its operations.

This method sum the discounts in the commissions dict of the
container. The total discount value is then prorated by the
daytrades and common operations based on their volume.

#### find_rates_for_positions(self):
Finds the rates for all daytrades and common operations.



## trade.Accumulator
An accumulator of quantity @ some average price.

### Attributes:
+ asset: An asset instance, the asset whose data are being accumulated.
+ date: A string 'YYYY-mm-dd' representing the date of the last status change of the accumulator.
+ quantity: The asset's accumulated quantity.
+ price: The asset's average price for the quantity accumulated.
+ results: A dict with the total results from the operations accumulated.
+ logging: A boolean indicating if the accumulator should log the calls to the accumulate() method.
+ log: A dict with all the operations performed with the asset, provided that self.logging is True.

if created with logging=True the accumulator will log the every
operation it accumulates.

Results are calculated by the accumulator according to the value
of the operations informed and the current status of the
accumulator (the current quantity and average price of the asset).

A initial status (quantity, price and results) of the asset can be set on the
accumulator by simply accumulating an Operation representing the status.

### Methods:

#### init (self, asset, logging=False):
Creates a instance of the accumulator.

Logging by default is set to False; the accumulator will not log any operation,
just accumulate the quantity and calculate the average price and results related
to the asset after each call to accumulate_operation() and accumulate_event().

If logging is set to True the accumulator will log the data passed on every call
to accumulate_operation() and accumulate_event().

#### log_occurrence(self, occurrence):
Log Operation and Event objects.

If logging, this method is called behind the scenes every
time the method accumulate() is called. The occurrences are
logged like this:
```python
    self.log = {
        '2017-09-19': {
            'position': {
                'quantity': float
                'price': float
            }
            'occurrences': [Operation, ...],
        },
        ...
    }
```
#### accumulate_operation(self, operation):
Accumulates operation data to the existing position.

The accumulator takes care of adding any custom results already
present on the operation results attribute to the total
results of the stock in the accumulator.

#### accumulate_event(self, event):
Receives a Event subclass instance and lets it do its work.

An event can change the quantity, price and results stored in
the accumulator.

The way it changes this information is up to the event object;
each Event subclass must implement a method like this:

```python
update_container(self, accumulator)
    # do stuff here...
```

that have the logic for the change in the accumulator's
quantity, price and results.



## trade.Portfolio
A portfolio of assets.

A portfolio is a collection of Accumulator objects.
It can receive Operation objects and update the corresponding
accumulators.

### Attributes:
+ assets: A dict {Asset.symbol: Accumulator}.
+ tasks: The tasks the portfolio will execute when accumulating.

### Methods

#### accumulate(self, operation):
Accumulate an operation on its corresponding accumulator.

#### run_tasks(self, operation):
Execute the defined tasks on the Operation.

Any function defined in self.tasks will be executed.
This runs before the call to Accumulator.accumulate().



## trade.TradingFees
A base class for identifying fees for operations.

A TradingFees class reads an operation and returns the correspondent fees for
that operation. Since fees (and also the way they are applied) may vary greatly
from one context to another, this class just implements a dummy interface for
the fee discovery process, always returning a empty dictionary of fee.

Every OperationContainer object has a reference to this class.
If your app need to apply fees to your Operation objects, then you should
extend this class and inform the new TaxManager to your OperationContainer:

    operation_container.trading_fees = YourTradingFeesClass

The OperationContainer always access his TaxManager when
fetch_positions() is called. Behind the scenes the container
calls this method from the TradingFees class:

    tax_manager.get_fees(operation, operation_type)

After identifying the positions for every position present on the container.

### Methods:

#### staticmethod get_fees(self, operation, operation_type):
Return a empty dictionary.



## trade.utils.average_price(quantity_1, price_1, quantity_2, price_2):
Calculates the average price between two positions.
A position is the quantity of an asset and its average price.  
Returns the calculated average price.



## trade.utils.same_sign(x, y):
Checks if two numbers have the same sign.  
Return True if they have the same sign,  
False if they don't have the same sign,
and None if x or y are not numbers.



## License
Copyright (c) 2015 Rafael da Silva Rocha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
