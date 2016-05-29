Change Log
==========


0.2.9 (2016-05-29)
---------------------

* Options and events are no longer part of the core framework. An example
  of an app developed on top of the **trade** framework is now on the "sample"
  folder and it contains the old implementations for calls and puts, as well
  as the old events representing stock splits, inplits and bonus shares
* The JSON interface now must be initialized with the types of assets
  that will be present in the json (like "Option", "Asset"), and also with the
  tasks for the OperationContainer to run (check the tests to see how this works).


0.2.8 (2015-11-17)
---------------------

* Prototype for json options and option exercises support
* Faster day trade identification
