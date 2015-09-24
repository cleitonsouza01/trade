# The Operation Container
A container for operations.

An OperationContainer is used to group operations, like operations
that occurred on the same date, and then perform tasks on them. It
can:

- Separate the daytrades and the common operations of a group of
  operations that occurred on the same date by using the method:

    - identify_daytrades_and_common_operations()

- Prorate a group of taxes proportionally for all daytrades and
  common operations, if any, by using the method:

    - prorate_comissions_by_daytrades_and_common_operations()

## Attributes:
+ date: A string 'YYYY-mm-dd' representing the date of the operations on the container.
+ operations: A list of Operation instances.
+ comissions: A dict with discount names and values to be deducted from the operations.
+ daytrades: a dict of Daytrade objects, indexed by the daytrade asset.
+ common_operations: a dict of Operation objects, indexed by the operation asset.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
