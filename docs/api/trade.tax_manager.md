# trade.tax_manager

## trade.tax_manager.TaxManager
The base TaxManager.

A TaxManager object reads an operation and returns the correspondent rates for
that operation. Since rates (and also the way they are applied) may vary greatly
from one context to another, this class just implements a dummy interface for
the rate discovery process, always returning a empty dictionary of rates.

Every OperationContainer object has a reference to this class.
If your app need to apply fees to your Operation objects,
then you should extend this class and inform the new TaxManager to your
OperationContainer:

    operation_container_object.tax_manger = your_tax_manager_object

The OperationContainer always access his TaxManager when
fetch_positions() is called. Behind the scenes the container
calls this method from the TaxManager class:

    tax_manager.get_rates_for_operation(operation, operation_type)

After identifying the positions for every position present on the container.

### Methods:

#### staticmethod get_rates_for_operation(self, operation, operation_type):
Return a empty dictionary.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
