# Comissions And Rates

"Commissions" in the trade module are raw values that are deducted or added
to a trade total value, and also on the unitary price of the asset being traded.

"Rates" in the trade module are percentage values to be applied to an operation
based on its volume. Like commissions, they also change the total value of the
operation and the unitary price of the asset that is being traded.

## Commissions

"Commissions" in the trade module refer to any kind of fixed cost related
to an operation, like commissions charged by an brokerage company per operation,
or any other cost associated with an operation or with a group of operations.

For example, if your online broker charge you $4.50 per operation, you would
add a {'brokerage': 4.5} commission to your operation.

Commissions are always considered as the actual value of the commission; the
value informed as a commission to the Operation or the OperationContainer will
be deducted or included on the cost of the operations.

Commissions are considered by the trade module when calculating results and
the average price of assets. You may inform commissions directly on Operation
objects:

```python
commissions = {
    'brokerage': 0.5,
    'other comission': 2
}
operation = trade.Operation(
    date='2015-09-18',
    asset=some_asset,
    quantity=20,
    price=10,
    commissions=commissions
)
```
Or you may inform commissions to the OperationContainer, and let it prorate
the commissions by the operations for you:

```python
commissions = {
    'some discount': 1,
}
container = trade.OperationContainer(commissions=commissions)
container.prorate_comissions()
```

By default the method "prorate_commissions()"
is called behind the scenes every time the fetch_positions() method is called.

## Rates

"Rates" in the trade module refer to trading fees that are calculated based on
the trade volume. For example, besides paying a brokerage commission, you might
for some reason be charged 0.0325% by the operation volume for every operation
you perform and be charged 0.0250% by every operation that configures a
daytrade.

The trade module provides a standard, context-free way of dealing with this
kind of rate, so your application may extend the trade module functionality
to suit your needs.

If your context does not involve this kind of rates you may ignore this
section of the documentation and leave everything the way it is. If your
application need to calculate taxes for your operations, this will be
interesting to you.

Fees may vary greatly from one context to another, both in value and in
form of application. The trade lib provides a dummy TaxManager object
that can be extended to implement the right fees for your context.


### The Defaults

By default every OperationContainer object have a reference to an instance of
the dummy TaxManager object. As mentioned above, this object does not implement
any rates; it just returns a empty set of rates every time it is called.

So, when you call fetch_positions() on your OperationContainer, what happens
by default is this for every common operation inside the
OperationContainer:

```python
operation.taxes = tax_manager.get_fees_for_operation(operation)
```

And this for every daytrade inside the container:

```python
daytrade.purchase.rates = tax_manager.get_rates_for_daytrade(daytrade.purchase)
daytrade.sale.rates = tax_manager.get_rates_for_daytrade(daytrade.sale)
```

Where the tax_manager is returning {} in all the cases. If your application
doesn't need to calculate rates, you may just leave everything the way it is.


### Your own fees

To change the default behavior, you need to create your own TaxManager
class. While this may sound like a daunting task, it can be actually
pretty simple - actually, it will be as complex as the rules of the
rates you need to apply.

An example of a TaxManager class that returns 1% rate o be applied for every
common operation and 2% rate for every daytrade:

```python
class MyTaxManager:

    def get_rates_for_operation(self, operation):
        return {'name of the rate': 1}

    def get_rates_for_daytrade(self, operation):
        return {'name of the daytrade rate': 2}
```

You may include multiple rates on dictionaries those methods return.

Now all you need is to change the tax manager object in the OperationContainer
for your own tax manager:

```python
my_container = OperationContainer()

my_tax_manager = MyTaxManager()
my_container.tax_manager = my_tax_manager
```

And now all your daytrades will be taxed by 2%, while all your common
operations will be taxed by 1%.


Check the API docs for more on this.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
