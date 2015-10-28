# trade.plugins
http://github.com/rochars/trade  
http://trade.readthedocs.org

The trade module comes pre-packed with some plugins that add
functionalities related to common exchange market operations.

You may use this plugins in your project or use them as a base
to create your own plugins.



## Modules in this package:

+ [plugins.options](options)
  with classes for Options and Exercises and tasks for the
  OperationContainer and Portfolio.
+ [plugins.daytrades](daytrades)
  with the Daytrade class, a task for the OperationContainer
  and some helper functions.
+ [plugins.events](events)
  with classes to represent stock splits, reverse stock splits
  and bonus shares, and their base class.
+ [plugins.prorate](prorate)
  Commissions pro rata on the OperationContainer.



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
