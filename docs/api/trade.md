# trade

trade: Financial Application Framework
Copyright (c) 2016 Rafael da Silva Rocha  
https://github.com/rochars/trade  
http://trade.readthedocs.org


## OperationContainer(object)
A container for operations.

An OperationContainer is used to group operations that occurred on
the same date and then perform tasks on them.

This is achieved by calling this method:
- fetch_positions()


### Attributes:
+ date: A string 'YYYY-mm-dd' representing the date of the operations on the container.
+ operations: A list of Operation instances.
+ tasks: a list of functions. The functions will be called in the order they are defined in this list when fetch_positions() is called. Every listed function must receive a OperationContainer object. The functions may change the Operation objects in self.operations, if needed (like when you separate day trades from other operations).

### Methods:

#### def fetch_positions(self)
Fetch the positions resulting from the operations.

This method executes all the methods defined in self.tasks
in the order they are listed.


## License
Copyright (c) 2016 Rafael da Silva Rocha

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
