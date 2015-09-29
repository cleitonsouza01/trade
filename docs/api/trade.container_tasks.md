# trade.container_tasks

The default tasks (and their helper functions) provided by the trade module
for the OperationContainer fetch_positions() method.


## prorate_commissions(operation_container):
Prorates the container's commissions by its operations.

This method sum the discounts in the commissions dict of the
container. The total discount value is then prorated by the
daytrades and common operations based on their volume.

## prorate_commissions_by_operation(operation_container, operation):
Prorates the commissions of the container for one operation.

The ratio is based on the container volume and the volume of
the operation.

## identify_daytrades_and_common_operations(operation_container):
Separates operations into daytrades and common operations.

After this process, the attributes 'daytrades' and
'common_operations'  will be filled with the daytrades
and common operations found in the container operations list,
if any. The original operations list remains untouched.

## extract_daytrade(operation_container, operation_a, operation_b):
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

## add_to_common_operations(operation_container, operation):
Adds an operation to the common operations list.

## find_rates_for_positions(operation_container):
Gets the rates for every position on the container.

## get_operations_from_exercises(operation_container):



Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
