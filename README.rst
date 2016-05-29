trade: Financial Application Framework
======================================

| Copyright (c) 2016 Rafael da Silva Rocha
| https://python-trade.appspot.com
| https://github.com/rochars/trade
| http://trade.readthedocs.org

--------------

|Build| |Windows Build| |Coverage Status| |Code Climate| |Python Versions| |Live Demo|


trade
-----
**trade** is a framework for the development of financial applications. It operates
on the concept of *subjects* and *occurrences*. A *subject* represents anything that
can be traded, while an *occurrence* represents anything that affects one or more
subjects, like a stock exchange operation or a stock split.

It was developed to work with any kind of *subject* and *occurrence* related to
the financial market, and also to work under specific rules of different markets
across the world, by following these principles:

- different subjects may have different attributes
- a subject may relate to none or many other subjects
- an occurrence must involve one or many subjects
- there may be an existing context for any subject
- different occurrences can implement different processes
- an occurrence may update the state of none or many subjects

Extending the framework with market-specific rules and operations should be as
simple as creating new types of subjects and occurrences.

You can try it `live <https://python-trade.appspot.com>`_.

There is an ongoing effort to
`document this project <http://trade.readthedocs.org>`_. Check it out.


In a nutshell
-------------
**trade** works like a service. The user informs the items he have in stock and a series
of subsequent occurrences (purchases, sales, whatsoever) with those or other items.
**trade** then calculates the effects of those occurrences and gives back the
new amounts and costs of the items in stock.


Quickstart
----------

An example of the JSON interface:

.. code:: python

    from trade import trade
    from trade.trade_json import TradeJSON


    interface = TradeJSON(
        [trade.fetch_daytrades],
        {
            'Asset': trade.Asset,
            'Operation': trade.Operation,
        }
    )

    json_input = '''{
        "subjects": {
            "GOOG": {
                "type": "Asset",
                "name": "Google Inc"
            },
            "AAPL": {
                "type": "Asset",
                "name": "Apple, Inc."
            }
        },
        "occurrences": [
            {
                "type": "Operation",
                "subject": "AAPL",
                "date": "2015-11-10",
                "quantity": 10,
                "price": 120.15
            },
            {
                "type": "Operation",
                "subject": "GOOG",
                "date": "2015-11-10",
                "quantity": 10,
                "price": 724.89
            },
            {
                "type": "Operation",
                "subject": "GOOG",
                "date": "2015-11-10",
                "quantity": -5,
                "price": 724.98
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

The current version is 0.2.9 alpha.


Installation
------------

The module can be installed with pip:

    $ pip install trade


License
-------

Copyright (c) 2016 Rafael da Silva Rocha

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
.. |Documentation| image:: https://readthedocs.org/projects/trade/badge/
   :target: http://trade.readthedocs.org/en/latest/
.. |License| image:: https://img.shields.io/pypi/l/trade.png
   :target: https://opensource.org/licenses/MIT
