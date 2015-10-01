# trade.portfolio


## trade.portfolio.Portfolio
A portfolio of assets.

A portfolio is a collection of Accumulator objects.
It can receive Operation objects and update the corresponding
accumulators.

### Attributes:
    assets: A dict {Asset: Accumulator}.
    tasks: The tasks the portfolio will execute when accumulating.

### Methods

#### accumulate(self, operation):
Accumulate an operation on its corresponding accumulator.

#### run_tasks(self, operation):
Execute the defined tasks on the Operation.

Any function defined in self.tasks will be executed.
This runs before the call to Accumulator.accumulate().


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
