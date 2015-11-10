trade: Tools For Stock Trading Applications.
============================================

| Copyright (c) 2015 Rafael da Silva Rocha
| rocha.rafaelsilva@gmail.com
| http://trade.readthedocs.org
| https://python-trade.appspot.com

--------------

|Build| |Coverage Status| |Code Climate| |Downloads| |Python Versions| |Live Demo|


Installation
------------

The trade module can be installed with pip:

    pip install trade

To check if everything went OK, open the Python console and import the
module:

.. code:: python

    import trade
    asset = trade.Asset(symbol='ATVI')

Example
-------

A basic example of the trade module in action:

.. code:: python

    import trade

    # create the asset that we are going to trade
    asset = trade.Asset(name='Google Inc', symbol='GOOGL')

    # create the accumulator to accumulate trades with the asset
    accumulator = trade.Accumulator(asset)


    print(accumulator.subject.name)
    #>> Google Inc

    print(accumulator.state['quantity'])
    #>> 0

    print(accumulator.state['price'])
    #>> 0

    print(accumulator.state['results'])
    #>> {}


    # create a trade operation buying the asset
    purchase = trade.Operation(
        subject=asset,
        quantity=10,
        price=650.73,
        date='2015-09-23'
    )

    # accumulate the trade
    accumulator.accumulate(purchase)


    print(accumulator.state['quantity'])
    #>> 10

    print(accumulator.state['price'])
    #>> 650.73

    print(accumulator.state['results'])
    #>> {}


    # create a new trade operation selling the asset
    sale = trade.Operation(
        subject=asset,
        quantity=-5,
        price=656.77,
        date='2015-09-24'
    )

    # accumulate the new trade
    accumulator.accumulate(sale)


    print(accumulator.state['quantity'])
    #>> 5

    print(accumulator.state['price'])
    #>> 650.73

    print(accumulator.state['results'])
    #>> {'trades': 30.199999999999818}

Check the `documentation`_ for all the available features.


JSON Interface
--------------

.. code:: python

    import trade
    interface = trade.TradeJSON()

    json_input = '''{
        "subjects": {
            "GOOG": {
                "type": "Asset",
                "name": "Google Inc",
                "expiration_date": ""
            },
            "AAPL": {
                "type": "Asset",
                "name": "Apple Inc.",
                "expiration_date": ""
            }
        },
        "occurrences": [
            {
                "type": "Operation",
                "subject": "AAPL",
                "date": "2015-11-10",
                "quantity": 10,
                "price": 120.15,
                "commissions": {},
                "raw_results": {},
                "operations": []
            },
            {
                "type": "Operation",
                "subject": "GOOG",
                "date": "2015-11-10",
                "quantity": 10,
                "price": 724.89,
                "commissions": {},
                "raw_results": {},
                "operations": []
            }
        ],
        "initial state": {
            "AAPL": {
                "date": "2015-10-09",
                "quantity": 92,
                "price": 119.27,
                "results": {"trades": 5021.72}
            }
        }
    }'''

    json_output = interface.get_trade_results(json_input)

    print(json_output)
    #>> {
    #    "AAPL": {
    #        "2015-10-09": {
    #            "price": 119.27,
    #            "quantity": 92,
    #            "results": {
    #                "trades": 5021.7200000000003
    #            }
    #        },
    #        "2015-11-10": {
    #            "date": "2015-10-09",
    #            "price": 119.35627450980392,
    #            "quantity": 102,
    #            "results": {
    #                "trades": 5021.7200000000003
    #            }
    #        }
    #    },
    #    "GOOG": {
    #        "2015-11-10": {
    #            "price": 724.88999999999999,
    #            "quantity": 10,
    #            "results": {}
    #        }
    #    }
    #}


Compatibility
-------------

trade is compatible with Python 2.7, 3.3, 3.4 and 3.5.

Version
-------

The current version is 0.2.4 alpha.

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
.. |Code Climate| image:: https://codeclimate.com/github/rochars/trade/badges/gpa.png
   :target: https://codeclimate.com/github/rochars/trade
.. |Codacy| image:: https://img.shields.io/codacy/56eea28216b74e5eabb1a7ec858e9a6e.svg
   :target: https://www.codacy.com/app/rocha-rafaelsilva/trade/dashboard
.. |Downloads| image:: https://img.shields.io/pypi/dm/trade.png
   :target: https://pypi.python.org/pypi/trade/
.. |Live Demo| image:: https://img.shields.io/badge/try-live%20demo-blue.png
   :target: https://python-trade.appspot.com/
