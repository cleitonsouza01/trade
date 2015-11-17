"""JSON interface example with Options and Exercise operations.

http://trade.readthedocs.org/
https://github.com/rochars/trade
License: MIT

Copyright (c) 2015 Rafael da Silva Rocha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import trade
import json

interface = trade.TradeJSON()

json_input = '''{
    "subjects": {
        "ASSET": {
            "type": "Asset",
            "name": "Some Asset"
        },
        "OPTION": {
            "type": "Option",
            "name": "Some Option",
            "expiration_date": "2016-12-23",
            "underlying_assets": {"ASSET": 1}
        }
    },
    "occurrences": [
        {
            "type": "Operation",
            "subject": "OPTION",
            "date": "2015-01-01",
            "quantity": 10,
            "price": 1
        },
        {
            "type": "Exercise",
            "subject": "OPTION",
            "date": "2015-01-03",
            "quantity": 10,
            "price": 4
        }
    ],
    "initial state": {}
}'''

json_output = json.dumps(
    json.loads(interface.get_trade_results(json_input)),
    sort_keys=True,
    indent=2,
    separators=(',', ': ')
)

print(json_output)
