# Comissions And Taxes

## Comissions

"Comissions" in the trade module refer to any kind of cost related to an
operation, like commissions charged by an brokerage company per operation,
or any other cost associated with an operation or with a group of operations.

Comissions are considered by the trade module when calculating results and
the average price of assets. You may inform comissions directly on Operation
objects:

```python
comissions = {
    'brokerage': 0.5,
    'other comission': 2
}
operation = trade.Operation(
    date='2015-09-18',
    asset=some_asset,
    quantity=20,
    price=10,
    comissions=comissions
)
```
Or you may inform comissions to the OperationContainer, and let it prorate
the comissions by the operations for you:

```python
commissions = {
    'some discount': 1,
}
container = trade.OperationContainer(comissions=commissions)
container.prorate_comissions_by_daytrades_and_common_operations()
```

By default the method "prorate_comissions_by_daytrades_and_common_operations()"
is called behind the scenes every time the fetch_positions() method is called.

## Taxes

Working with trade data will most likely involve working with taxes.
The trade module provides a standard, context-free way of dealing with
taxes, so your application may extend the trade module functionality to
suit your needs.

If your context does not involve taxes you may ignore this section of the
documentation and leave everything the way it is. If your application need
to calculate taxes for your operations, this will be intersting to you.

Taxes may vary greatly from one context to another, both in value and in
form of application. The trade lib provides a "dummy" TaxManager object
that can be extended to implement the right taxes for your context.


### The Defaults

By default every OperationContainer object have a reference to an
instance of the dummy TaxManager object. As mentioned above, this object
does not implement any tax logic; it just returns a empty set of
taxes everytime it is called.

So, when you call fetch_positions() on your OperationContainer, what happens
by default is this for every common operation inside the
OperationContainer:

```python
operation.taxes = tax_manager.get_taxes_for_operation(operation)
```

And this for every daytrade inside the container:

```python
daytrade.purchase.taxes = tax_manager.get_taxes_for_daytrade(daytrade.purchase)
daytrade.sale.taxes = tax_manager.get_taxes_for_daytrade(daytrade.sale)
```

Where the tax_manager is returning {} in all the cases. If your application
doesn't need to calculate taxes, you may just leave everything the way it is.


### Your own taxes

To change the default behavior, you need to create your own TaxManager
class. While this may sound like a daunting task, it can be actually
pretty simple - actually, it will be as complex as the tax rules for
your context are.

An example of a TaxManager class that returns 1% tax for every common
operation and 2% tax for every daytrade:

```python
class MyTaxManager:

    def get_taxes_for_operation(self, operation):
        return {'name of the tax': 1}

    def get_taxes_for_daytrade(self, operation):
        return {'name of the daytrade tax': 2}
```

All you need is to change the object in the OperationContainer for your
own tax manager:

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
