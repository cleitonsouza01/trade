# trade.operation_container

This module contains the class definitions of the OperationContainer.
The OperationContainer is used to group operations and then perform
tasks on them.


## trade.operation_container.OperationContainer
A container for operations.

An OperationContainer is used to group operations, like operations
that occurred on the same date, and then perform tasks on them.

This is achieved by calling this method:

    * fetch_positions()

The tasks executed on fetch_positions are defined on the attribute
"fetch_positions_tasks", a list of functions that receive a OperationContainer
instance as argument.

The default tasks the trade module provides for fetch_positions() are:

- Get the operations that option exercises have created by calling the method:

    * get_operations_from_exercises(container)

- Separate the daytrades and the common operations of a group of
  operations that occurred on the same date by calling the method:

    * identify_daytrades_and_common_operations(container)

- Prorate a group of commissions proportionally for all daytrades and
  common operations, if any, by calling the method:

    * prorate_comissions(container)

- Find the the rates for the resulting positions, if needed, by calling
  the method:

    * find_rates_for_positions(container)

You can append any function to the OperationContainer fetch_positions_tasks
as long as it receives an OperationContainer instance as argument.

### Attributes:
+ date: A string 'YYYY-mm-dd' representing the date of the operations on the container.
+ operations: A list of Operation instances.
+ commissions: A dict with discount names and values to be deducted from the operations.
+ daytrades: a dict of Daytrade objects, indexed by the daytrade asset.
+ common_operations: a dict of Operation objects, indexed by the operation asset.
+ fetch_positions_tasks: a list of OperationContainer methods.  
  The methods will be called in the order they are defined in this list when
  fetch_positions() is called. A default setup could look like this:
  self.fetch_positions_tasks = [  
      get_operations_from_exercises,  
      identify_daytrades_and_common_operations,  
      prorate_commissions,  
      find_rates_for_positions,  
  ]

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

#### merge_operations(self, existing_operation, operation):
Merges one operation with another operation.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
