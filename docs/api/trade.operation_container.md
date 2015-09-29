# trade.operation_container

This module contains the class definitions of the OperationContainer.
The OperationContainer is used to group operations and then perform
tasks on them.


## trade.operation_container.OperationContainer
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

    * fetch_positions()

The tasks executed on fetch_positions are defined on the attribute
"fetch_positions_tasks", a list of OperatioContainer methods.

The default behavior of fetch_positions() is this:

- Get the operations that option exercises have created by calling the method:

    * get_operations_from_exercises()

- Separate the daytrades and the common operations of a group of
  operations that occurred on the same date by calling the method:

    * identify_daytrades_and_common_operations()

- Prorate a group of commissions proportionally for all daytrades and
  common operations, if any, by calling the method:

    * prorate_comissions()

- Find the the rates for the resulting positions, if needed, by calling
  the method:

    * find_rates_for_positions()

You can, however, append more methods to fetch_positions_tasks, so
fetch_positions() will execute also any other method you want; you may
also change the order the methods are executed, or even define a completely
new list of methods that you created to fit the needs of your application.

### Attributes:
+ date: A string 'YYYY-mm-dd' representing the date of the operations on the container.
+ operations: A list of Operation instances.
+ commissions: A dict with discount names and values to be deducted from the operations.
+ daytrades: a dict of Daytrade objects, indexed by the daytrade asset.
+ common_operations: a dict of Operation objects, indexed by the operation asset.
+ fetch_positions_tasks: a list of OperationContainer methods.  
  The methods will be called in the order they are defined in this list when
  fetch_positions() is called. The default fetch_positions_tasks list is this:
  ```python
    [
        self.get_operations_from_exercises,
        self.identify_daytrades_and_common_operations,
        self.prorate_commissions,
        self.find_rates_for_positions,
    ]
  ```

### Properties

#### total_comission_value(self):
Returns the sum of values of all commissions.

#### volume(self):
Returns the total volume of the operations in the container.

### Methods

#### fetch_positions(self):
Fetch the positions resulting from the operations.

This method executes all the methods defined on the
fetch_positions_tasks attribute in the order they are
listed.

#### prorate_comissions(self):
Prorates the container's commissions by its operations.

This method sum the discounts in the commissions dict of the
container. The total discount value is then prorated by the
daytrades and common operations based on their volume.

#### prorate_comissions_by_operation(self, operation):
Prorates the commissions of the container for one operation.

The ratio is based on the container volume and the volume of
the operation.

#### identify_daytrades_and_common_operations(self):
Separates operations into daytrades and common operations.

After this process, the attributes 'daytrades' and
'common_operations'  will be filled with the daytrades
and common operations found in the container operations list,
if any. The original operations list remains untouched.

#### extract_daytrade(self, operation_a, operation_b):
Extracts the daytrade part of two operations.

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
Adds an operation to the common operations list.

#### merge_operations(self, existing_operation, operation):
Merges one operation with another operation.

#### find_rates_for_positions(self):
Gets the rates for every position on the container.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
