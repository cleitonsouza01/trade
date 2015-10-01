# trade.plugins.options

This plugin provides options functionality to the trade module.
It has classes for Options and Exercises, as well as
OperationContainer and Portfolio tasks.


## Classes

### Option(Derivative):
Represents an Option.
This class represents both calls and puts.

#### exercise(self, quantity, price, date, premium=0):
Exercises the option.

If a premium if informed, then it will be considered on the
underlying asset operation price.

Returns two operations:
    - one operation with zero value representing the option
      being consumed by the exercise;
    - one operation representing the purchase or sale of the
      underlying asset


### Exercise(Operation):
An exercise operation.

Exercise operations are operations that involve more than one
asset, usually a derivative like a Option and an underlying asset.

An exercise will change both the accumulated quantity of the
derivative and of the underlying asset.

Attributes:
- accumulate_underlying_operations = Set to true

#### fetch_operations(self, portfolio=None):
Returns the operations created by this exercise.

If a portfolio is informed, then the premium of the option
will be considered.

An exercise creates two operations:
- One operation to consume the option that it being exercised
- One operation to represent the sale or the purchase of the asset


## OperationContainer tasks:

### fetch_exercises(container):
After this task, all operations created by Exercise objects
will be on the container positions under the key 'exercises'.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
