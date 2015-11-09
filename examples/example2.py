"""JSON interface example"""

import trade

interface = trade.TradeJSON()

json_input = '''{
    "subjects": {
        "GOOG": {
            "type": "Asset",
            "name": "Google Inc",
            "expiration_date": "2019-01-01"
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
            "subject": "GOOG",
            "date": "2015-01-01",
            "quantity": 10,
            "price": 650.11,
            "commissions": {},
            "raw_results": {},
            "operations": []
        }
    ],
    "initial state": {
        "AAPL": {
            "date": "2015-11-09",
            "quantity": 92,
            "price": 31.21,
            "results": {"trades": 5000.72}
        }
    }
}'''

json_output = interface.get_trade_results(json_input)

print(json_output)
#>> {
#    "GOOG": {
#        "2015-01-01": {
#            "quantity": 10,
#            "price": 650.11,
#            "results": {}
#        }
#    },
#    "AAPL": {
#        "2015-11-09": {
#            "quantity": 92,
#            "price": 31.21,
#            "results": {"trades": 5000.72}
#        }
#    }
#}
