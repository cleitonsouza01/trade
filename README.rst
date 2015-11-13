trade: Tools For Trade Management Applications |Live Demo|
==========================================================

| Copyright (c) 2015 Rafael da Silva Rocha
| http://trade.readthedocs.org
| https://python-trade.appspot.com

--------------

|Build| |Windows Build| |Coverage Status| |Code Climate| |Python Versions|


What problem does it solve?
---------------------------
trade calculates the results of investments. You inform a series of assets, a
series of operations with those assets, and trade tells the money you
invested in each asset, the profits from buying and selling each asset, and
more. It is focused in, but not limited to, stock exchange operations.

trade is still in early development, but you can already try it `live`_!


Installation
------------

The trade module can be installed with pip:

    $ pip install trade

To check if everything went OK, open the Python console and import the module:

.. code:: python

    import trade
    asset = trade.Asset(symbol='AMZN')


Quickstart
----------

A basic example of the trade module in action:

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
                "name": "Apple, Inc.",
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
            },
            {
                "type": "Operation",
                "subject": "GOOG",
                "date": "2015-11-10",
                "quantity": -5,
                "price": 724.98,
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
    #$ {
    #  "assets": {
    #    "AAPL": {
    #      "states": {
    #        "2015-10-09": {
    #          "price": 119.27,
    #          "quantity": 92,
    #          "results": {
    #            "trades": 5021.7200000000003
    #          }
    #        },
    #        "2015-11-10": {
    #          "price": 119.35627450980392,
    #          "quantity": 102,
    #          "results": {
    #            "trades": 5021.7200000000003
    #          }
    #        }
    #      },
    #      "totals": {
    #        "daytrades": 0,
    #        "operations": 1,
    #        "purchases": 1,
    #        "results": {
    #          "trades": 5021.7200000000003
    #        },
    #        "sales": 0
    #      }
    #    },
    #    "GOOG": {
    #      "states": {
    #        "2015-11-10": {
    #          "price": 724.88999999999999,
    #          "quantity": 5,
    #          "results": {
    #            "daytrades": 0.45000000000027285
    #          }
    #        }
    #      },
    #      "totals": {
    #        "daytrades": 1,
    #        "operations": 2,
    #        "purchases": 1,
    #        "results": {
    #          "daytrades": 0.45000000000027285
    #        },
    #        "sales": 1
    #      }
    #    }
    #  },
    #  "totals": {
    #    "daytrades": 1,
    #    "operations": 3,
    #    "purchases": {
    #      "operations": 2,
    #      "volume": 8450.3999999999996
    #    },
    #    "results": {
    #      "daytrades": 0.45000000000027285,
    #      "trades": 5021.7200000000003
    #    },
    #    "sales": {
    #      "operations": 1,
    #      "volume": 3624.9000000000001
    #    }
    #  }
    #}


Compatibility
-------------

trade is compatible with Python 2.7, 3.3, 3.4 and 3.5.


Version
-------

The current version is 0.2.6 alpha.


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
.. _accumulator: https://github.com/rochars/accumulator
.. _live: https://python-trade.appspot.com
.. |Build| image:: https://img.shields.io/travis/rochars/trade.svg?label=unix%20build
   :target: https://travis-ci.org/rochars/trade
.. |Windows Build| image:: https://img.shields.io/appveyor/ci/rochars/trade.svg?label=windows%20build
   :target: https://ci.appveyor.com/project/rochars/trade
.. |Coverage Status| image:: https://coveralls.io/repos/rochars/trade/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/rochars/trade?branch=master
.. |Code Climate| image:: https://codeclimate.com/github/rochars/trade/badges/gpa.png
   :target: https://codeclimate.com/github/rochars/trade
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/trade.png
   :target: https://pypi.python.org/pypi/trade/
.. |Live Demo| image:: https://img.shields.io/badge/try-live%20demo-blue.png
   :target: https://python-trade.appspot.com/
.. |Downloads| image:: https://img.shields.io/pypi/dm/trade.png
   :target: https://pypi.python.org/pypi/trade/
.. |Documentation| image:: https://readthedocs.org/projects/trade/badge/
   :target: http://trade.readthedocs.org/en/latest/
.. |License| image:: https://img.shields.io/pypi/l/trade.png
   :target: https://opensource.org/licenses/MIT
.. |Codacy| image:: https://img.shields.io/codacy/56eea28216b74e5eabb1a7ec858e9a6e.svg
   :target: https://www.codacy.com/app/rocha-rafaelsilva/trade/dashboard
.. |Requirements| image:: https://requires.io/github/rochars/trade/requirements.svg?branch=master
   :target: https://requires.io/github/rochars/trade/requirements/?branch=master)
