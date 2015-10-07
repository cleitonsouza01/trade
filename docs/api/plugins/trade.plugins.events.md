# trade.plugins.events

events: A default set of events for the trade module.

This plugin provides a standard set of events for the trade module.
Events are subclasses of trade.Occurrence. They are passed to
Accumulator and Porfolio objects to change asset accumulation data.

It contains the definitions of:
- Event
- StockSplit
- ReverseStockSplit
- BonusShares

Events can be accumulated by Portfolio objects just like any other
occurrence. Just like any other Occurrence subclass, each event must
for implement a update_container() method that receives a
trade.Accumulator object. This method will contain the logic for the
update on the accumulator data.



## Classes


### Event(Occurrence)
An occurrence that change one or more asset's position.

This is a base class for Events. Events can change the quantity,
the price and the results stored on a asset accumulator.

#### Attributes:
+ date: A string 'YYYY-mm-dd', the date the event occurred.
+ asset: The target asset of the event.



### StockSplit(Event)
A stock split.

This class represents both stock splits and reverse stock splits.
Stock splits are represented by values greater than 1.
Reverse stock splits are represented by values between 0 and 1.

#### Methods:

##### update_container(self, accumulator)
Performs a split or a reverse split on the stock.


### class BonusShares(Event)
Bonus shares.

#### Methods:

##### update_container(self, accumulator)
Add stocks received as bonus shares do the accumulator.



Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
