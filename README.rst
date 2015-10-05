trade: Tools For Stock Trading Applications.
============================================

| Copyright (c) 2015 Rafael da Silva Rocha
| rocha.rafaelsilva@gmail.com
| http://rochars.github.io/trade/
| http://trade.readthedocs.org

--------------

|Build| |Coverage Status| |Documentation| |License| |Python Versions|

What is it?
-----------
trade is Python framework to ease the creation of investment management
applications. It is focused in, but not limited to, stock exchange markets.

The trade module provides notions of assets, purchases, sales, daytrades,
cost deduction, rates, options, option exercises, asset accumulation and more.

Installation
------------

The trade module can be installed with pip:

    pip install trade

To check if everything went OK, open the Python console and import the
module:

.. code:: python

    import trade
    asset = trade.Asset(symbol='AAPL')
    print(asset.symbol)
    #>> AAPL

Example
-------

A basic example of the trade module in action:

.. code:: python

    import trade

    # create the asset that we are going to trade
    asset = trade.Asset(name='Google Inc', symbol='GOOGL')

    # create the accumulator to accumulate trades with the asset
    accumulator = trade.Accumulator(asset)


    print(accumulator.asset.name)
    #>> Google Inc

    print(accumulator.quantity)
    #>> 0

    print(accumulator.price)
    #>> 0

    print(accumulator.results)
    #>> {'trades': 0}


    # create a trade operation buying the asset
    purchase = trade.Operation(
        asset=asset,
        quantity=10,
        price=650.73,
        date='2015-09-23'
    )

    # accumulate the trade
    accumulator.accumulate_operation(purchase)


    print(accumulator.quantity)
    #>> 10

    print(accumulator.price)
    #>> 650.73

    print(accumulator.results)
    #>> {'trades': 0}


    # create a new trade operation selling the asset
    sale = trade.Operation(
        asset=asset,
        quantity=-5,
        price=656.77,
        date='2015-09-24'
    )

    # accumulate the new trade
    accumulator.accumulate_operation(sale)


    print(accumulator.quantity)
    #>> 5

    print(accumulator.price)
    #>> 650.73

    print(accumulator.results)
    #>> {'trades': 30.199999999999818}

Operation objects may include rates and commissions that are considered
by the accumulator when it calculates results and average prices.

The Accumulator can also log the accumulated operations and their
results.

Check the `documentation`_ for all the available features.

Compatibility
-------------

trade is compatible with Python 2.7, 3.3, 3.4 and 3.5.

Version
-------

The current version is 0.1.5 alpha.

License
-------

Copyright (c) 2015 Rafael da Silva Rocha

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
“Software”), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

.. _documentation: http://trade.readthedocs.org

.. |Build| image:: https://api.travis-ci.org/rochars/trade.png
   :target: https://travis-ci.org/rochars/trade
.. |Coverage Status| image:: https://coveralls.io/repos/rochars/trade/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/rochars/trade?branch=master
.. |Documentation| image:: https://readthedocs.org/projects/trade/badge/
   :target: http://trade.readthedocs.org/en/latest/
.. |License| image:: https://img.shields.io/pypi/l/trade.png
   :target: https://opensource.org/licenses/MIT
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/trade.png
   :target: https://pypi.python.org/pypi/trade/
