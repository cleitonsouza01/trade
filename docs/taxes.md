# Taxes

Working with trade data will most likely involve working with taxes.
The trade module provides a standard, context-free way of dealing with
taxes, so you application may extend the trade module functionality to
suit you needs.

If your context does not involve taxes you may ignore this section of the
documentation and leave everything the way it is. If your application need
to calculate taxes for your operations, this will be intersting to you.

Taxes may vary greatly from one context to another, both in value and in
form of application. The trade lib provides a "dummy" TaxManager object
that can be extended to implement the right taxes for your context.


## The Defaults

By default every OperationContainer object have a reference to an
instance of the dummy TaxManager object. As mentioned above, this object
by do not implement any tax logic; it just returns a empty set of
taxes everytime it is called.

So, when you call fetch_positions() on you OperationContainer, what happens
by default is this for every common operation inside the
OperationContainer:

operation.taxes = self.tax_manager.get_taxes_for_operation(operation)

And this for every daytrade inside the container:

daytrade.purchase.taxes = \
    self.tax_manager.get_taxes_for_daytrade(daytrade.purchase)
daytrade.sale.taxes = \
    self.tax_manager.get_taxes_for_daytrade(daytrade.sale)

Where the tax_manager if returning {} all the cases. If your application
don't need to calculate taxe, you may just leave everything the way it is.


## Your own taxes

To change the default behavior, you need to create your own TaxManager
class. While this may sound like a daunting task, it can be actually
pretty simple - actually, it will be as complex as the tax rules for
your context are.

An example of a TaxManager class that returns 1% tax for every common
operation and 2% tax for everydaytrade:

class MyTaxManager:

    def get_taxes_for_operation(self, operation):
        return {'name of the tax': 1}

    def get_taxes_for_daytrade(self, operation):
        return {'name of the daytrade tax': 2}

All you need is to change the object in the OperationContainer for your
own tax manager:

my_container = OperationContainer()

my_tax_manager = MyTaxManager()
my_container.tax_manager = my_tax_manager

And your now all your daytrades will be taxed by 2%, while all your common
operations will be taxed by 1%.


Check the API docs for more on this.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
