# trade
Copyright (c) 2016 Rafael da Silva Rocha  
https://python-trade.appspot.com  
https://github.com/rochars/trade  
http://trade.readthedocs.org


## Asset(Subject)
An asset represents anything that can be traded.

### Class Attributes:
+ default_state: { 'quantity': 0, 'price': 0, 'results': {} }


## Operation(Occurrence)
+ date: A string 'YYYY-mm-dd', the date the operation occurred.
+ subject: An Asset instance, the asset that is being traded.
+ quantity: A number representing the quantity being traded. Positive quantities represent a purchase. Negative quantities represent a sale.
+ price: The raw unitary price of the asset being traded.
+ commissions: A dict of discounts. String keys and float values representing the name of the discounts and the values to be deducted added to the the operation value.
+ operations: A list of underlying occurrences that the might may have.
+ update_position: A boolean indication if the operation should update the position of the accumulator or not. By default set to True.
+ update_results: A boolean indication if the operation should update the results of the accumulator or not. By default set to True.
+ update_container: A boolean indication if the operation should update the state of the container. By default set to True.

### Attributes:
+ subject: An Asset object.
+ date: A string 'YYYY-mm-dd'

### Properties:
+ results: Return the results associated with the operation.
+ real_value: Returns the quantity * the real price of the operation.
+ real_price: Returns the real price of the operation. The real price is the price with all commission and costs already deducted or added.
+ total_commissions: Return the sum of all commissions of this operation.
+ volume: Returns the quantity of the operation * its raw price.

### Methods:

#### update_accumulator(self, accumulator)
Update the accumulator status with the operation data.

#### update_accumulator_results(self, accumulator)
Update the results stored in the accumulator.

#### update_positions(self, accumulator)
Update the position of the asset with the Operation data.


## OperationContainer(object)
A container for operations.

An OperationContainer is used to group operations that occurred on
the same date and then perform tasks on them.

The main task task of the OperationContainer is to fetch the
resulting positions from a group of Operations.

This is achieved by calling this method:
- fetch_positions()

Every time fetch_positions() is called the OperationContainer
execute these tasks:

- Execute all tasks defined in self.tasks. By default, no task is
  listed. Tasks are functions like this:
        def some_task(container)
  that receive an OperationContainer object and perform some work
  on the container data.

- Create positions in self.positions for all operations in
  the container. Positions are all the operations with the same
  asset grouped in a single operation.


### Attributes:
+ date: A string 'YYYY-mm-dd' representing the date of the operations on the container.
+ operations: A list of Operation instances.
+ positions: a dict of positions with this format
+ tasks: a list of functions. The functions will be called in the order they are defined in this list when fetch_positions() is called. Every listed function must receive a OperationContainer object. The functions may change the Operation objects in self.operations, if needed (like when you separate day trades from other operations).

### Methods:

#### def fetch_positions(self)
Fetch the positions resulting from the operations.

This method executes all the methods defined in self.tasks
in the order they are listed.

Then it reads the self.operations list and add any remaining
operation to the self.positions.


#### def add_to_position_operations(self, operation):
Adds an operation to the common operations list.


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
