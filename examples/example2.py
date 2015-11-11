"""JSON interface example"""

import trade
import json

interface = trade.TradeJSON()

json_input = '''{
    "subjects": {
        "GOOG": {
            "type": "Asset",
            "name": "Google Inc",
            "expiration_date": ""
        },
        "ATVI": {
            "type": "Asset",
            "name": "Activision Blizzard, Inc.",
            "expiration_date": ""
        }
    },
    "occurrences": [
        {
            "type": "Operation",
            "subject": "GOOG",
            "date": "2015-01-01",
            "quantity": 10,
            "price": 650.33,
            "commissions": {},
            "raw_results": {},
            "operations": []
        }
    ],
    "initial state": {
        "ATVI": {
            "date": "2014-06-09",
            "quantity": 100,
            "price": 31.21,
            "results": {
                "trades": 1200
            }
        }
    }
}'''

json_output = json.dumps(
    json.loads(interface.get_trade_results(json_input)),
    sort_keys=True,
    indent=2,
    separators=(',', ': ')
)

print(json_output)
#>> {
#    "totals": {
#        "sales": {
#            "volume": 0,
#            "operations": 0
#        },
#        "purchases": {
#            "volume": 6503.3,
#            "operations": 1
#        },
#        "operations": 1,
#        "daytrades": 0,
#        "results": {
#            "trades": 1200
#        }
#    },
#    "assets": {
#        "GOOG": {
#            "totals": {
#                "sales": 0,
#                "purchases": 1,
#                "operations": 1,
#                "daytrades": 0,
#                "results": {}
#            },
#            "states": {
#                "2015-01-01": {
#                    "quantity": 10,
#                    "price": 650.33,
#                    "results": {}
#                }
#            }
#        },
#        "ATVI": {
#            "totals": {
#                "sales": 0,
#                "purchases": 0,
#                "operations": 0,
#                "daytrades": 0,
#                "results": {
#                    "trades": 1200
#                }
#            },
#            "states": {
#                "2014-06-09": {
#                    "quantity": 100,
#                    "price": 31.21,
#                    "results": {
#                        "trades": 1200
#                    }
#                }
#            }
#        }
#    }
#}
