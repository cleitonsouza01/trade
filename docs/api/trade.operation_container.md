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

    fetch_positions()

Every time fetch_positions() is called the OperationContainer
execute this tasks behind the scenes:

- Execute all tasks defined in self.tasks.

- Create positions in self.positions for all operations in
  self.operations.

- Prorate the commissions, if any, proportionally for all positions
  by calling:

    prorate_commissions()

- Find the rates, if any, for the resulting positions by calling:

    find_rates_for_positions()

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

#### prorate_commissions_by_operation(self, operation):
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


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
