# trade 0.2.6
Copyright (c) 2015 Rafael da Silva Rocha  
https://github.com/rochars/trade  
https://python-trade.appspot.com

## Modules in this package:
+ [daytrades](daytrades)
+ [events](events)
+ [options](options)
+ [prorate](prorate)
+ [trade_json](trade_json)
+ [trade](trade)
+ [utils](utils)

### trade:
+ [Asset](trade)  
  An asset represents anything that can be traded.
+ [Operation](trade)  
  An Operation represents the purchase or sale of an asset.
+ [OperationContainer](trade)  
  A container for operations.

### daytrades:
+ [Daytrade](daytrades)  
  Representing day trades.
+ [fetch_daytrades](daytrades)  
  An OperationContainer task.
+ [daytrade_condition](daytrades)  
  Checks if two operations are day trades.
+ [find_purchase_and_sale](daytrades)  
  Find which operation is a purchase and which is a sale.

### events:
+ [Event](events)  
  An occurrence that change the state of one or more assets.
+ [StockSplit](events)  
  Representing both stock splits and reverse stock splits.
+ [BonusShares](events)  
  Representing bonus shares.

### options:
+ [Option](options)  
  Represents a vanilla option.
+ [Exercise](options)  
  An option exercise operation.
+ [fetch_exercises](options)  
  An OperationContainer task.

### prorate:
+ [prorate_commissions](prorate)  
  Prorates the container's commissions by its operations.
+ [prorate_commissions_by_position](prorate)  
  Prorates the commissions of the container for one position.

### trade_json:
+ [TradeJSON](trade_json)  
  trade module JSON interface.

### utils:
+ [merge_operations()](utils)
  Merges two operations.
+ [average_price()](utils)
  Calculates the average price between two asset states.
+ [same_sign()](utils)
  Checks if two numbers have the same sign.


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
