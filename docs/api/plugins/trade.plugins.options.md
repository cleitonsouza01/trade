# trade.plugins.options

options: Options plugin for the trade module.

This plugin provides Options functionalities to the trade module.

With this plugin you can:
- Create option assets that references underlying assets
- Create exercise operations that change both the option and underlying
  asset position on the portfolio

It provides:
- Option, a subclass of trade.Derivative
- Exercise, a subclass of trade.Operation
- the fetch_exercises() task to the OperationContainer
- the fetch_exercise_operations() task to the Portfolio



## Classes


### Option(trade.Asset):
Represents a vanilla option.

Represents both calls and puts.

This class can be used for common option operations or as a base
for classes that represent exotic options.

#### Attributes:
+ name: A string representing the name of the asset.
+ symbol: A string representing the symbol of the asset.
+ expiration_date: A string 'YYYY-mm-dd' representing the expiration date of the asset, if any.
+ underlying_assets: A dict of Asset objects representing the underlying assets of this asset and the ratio to which the asset relates to the Option. It looks like this: {Asset: float}

#### Methods:

##### exercise(self, quantity, price, date, premium=0):
Exercises the option.

If a premium is informed, then it will be considered on the
underlying asset operation price.

Returns a list of operations:
    - one operation with zero value representing the option
      being consumed by the exercise;
    - operations representing the purchase or sale of its
      underlying assets



### Exercise(trade.Occurrence):
An exercise operation.

Exercise operations are operations that involve more than one
asset, usually a derivative like a Option and an underlying asset.

An exercise will likely change the accumulated quantity of both the
derivative and its underlyings assets.

#### Attributes:

##### accumulate_underlying_operations
In a exercise operation it is the underlying
operations that will change the position on
the portfolio, not the operation itself

#### Methods:

##### fetch_operations(self, portfolio=None):
Fetch the operations created by this exercise.

If a portfolio is informed, then the premium of the option
will be considered.

An exercise creates multiple operations:
- one operation to consume the option that it being exercised
- operations to represent the sale or the purchase of each of its underlying assets, if any.



## OperationContainer tasks:

### fetch_exercises(container):
After this task, all operations created by Exercise objects
will be on the container positions under the key 'exercises'.



## Portfolio tasks:

### fetch_exercise_operations(operation, portfolio):
A Portfolio task.

Fetch the operations in a exercise operations and  get the premium
of the option that is being exercised.

It searches on the Portfolio object for an Accumulator of the option
and then use the accumulator price as the premium to be included
on the exercise operation price.



Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
