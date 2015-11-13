# options
Copyright (c) 2015 Rafael da Silva Rocha  
https://github.com/rochars/trade  
https://python-trade.appspot.com

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


## Option(Asset):
Represents a vanilla option.

Represents both calls and puts.

This class can be used for common option operations or as a base
for classes that represent exotic options.

### Attributes:
+ name: A string representing the name of the asset.
+ symbol: A string representing the symbol of the asset.
+ expiration_date: A string 'YYYY-mm-dd' representing the expiration date of the asset, if any.
+ underlying_assets: A dict of Asset objects representing the underlying assets of this asset and the ratio to which the asset relates to the Option. It looks like this: {Asset: float}

### Methods:

#### exercise(self, quantity, price, date, premium=0):
Exercises the option.

If a premium is informed, then it will be considered on the
underlying asset operation price.

Returns a list of operations:
    - one operation with zero value representing the option
      being consumed by the exercise;
    - operations representing the purchase or sale of its
      underlying assets



## Exercise(Operation):
An exercise operation.

Exercise operations are operations that involve more than one
asset, usually a derivative like a Option and one or more underlying assets.

An exercise will likely change the state of both the derivative and its
underlying assets.

### Attributes:
+ update_position set to False.
+ update_container set to False.

### Methods:

#### update_portfolio(self, portfolio)
A Portfolio task.

Fetch the operations in a exercise operations and  get the premium
of the option that is being exercised.

It searches on the Portfolio object for an Accumulator of the option
and then use the accumulator price as the premium to be included
on the exercise operation price.

#### update_accumulator(self, accumulator)
Exercise operations should not update the accumulator.
Its its underlying operations that should update the
accumulator.

#### fetch_operations(self, portfolio=None)
Fetch the operations created by this exercise.

If a portfolio is informed, then the premium of the option
will be considered.

An exercise creates multiple operations:
- one operation to consume the option that it being exercised
- operations to represent the sale or the purchase of each of its underlying assets, if any.


## fetch_exercises(container)
An OperationContainer task.

Fetch all exercise operations on the container into a single
exercise (by asset) on the container positions dictionary under
the key 'exercises'.


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
