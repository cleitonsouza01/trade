# trade: Tools For Stock Trading Applications.

## Introduction
trade is Python framework to ease the creation of investment management
applications. It is focused in, but not limited to, stock exchange markets.

What trade does is to provide a simple interface for defining operations
with assets and then calculate the result of those operations, automatically
creating a portfolio of the assets you trade.


### [Installing](part0.md)
This part of the tutorial shows how to install the trade framework.
If your already have trade installed you can skip this part.


### [Part 1: Creating operations](part01.md)
This part of the tutorial shows how to create simple purchase and
sale operations.


### [Part 2: Accumulating assets](part02.md)
Now that we can create operations, let's create a series of operations
and let the trade module calculate the resulting position of the asset.

We will use the Portfolio class to accumulate the operations and create
our portfolio.


### [Part 3: Pre-processing operations: The Operation Container](part03.md)
Now that we can create operations and accumulate their results on our
portfolio, let's do some pre-processing on the operations before we
accumulate them.

We will use the OperationContainer class to group some Operations, perform
some tasks on them, and then accumulate the changed operations on our
portfolio.


### [Part 4: Pre-processing operations: Daytrades](part04.md)
Now that we understand how to pre-process operations before accumulating
them on our portfolio, lets pre-process the operations to identify some
daytrades.

We will use the OperationContainer class to group some Operations and then
use the daytrades plugin that comes with the trade module to identify
the daytrades and "extract" them from the Operation objects.

Then we will accumulate the daytrades and the resulting common operations
on our Portfolio. Daytrades can be accumulated just like a normal operation.



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
