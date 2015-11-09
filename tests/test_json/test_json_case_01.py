"""Test the JSON interface with a initial state."""

from __future__ import absolute_import

from .test_json import TestJSON


class TestJSONCase0100(TestJSON):
    """One operation with a initial state."""

    json_input = '''{
        "subjects": {
            "GOOG": {
                "type": "Asset",
                "name": "Google Inc",
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
            "GOOG": {
                "quantity": 100,
                "price": 654.21,
                "results": {"trades": 1200}
            }
        }
    }'''

    json_output = '''{
        "GOOG": {
            "2015-01-01": {
                "quantity": 110,
                "price": 653.8572727272727,
                "results": {"trades": 1200}
            }
        }
    }'''



class TestJSONCase0101(TestJSON):
    """One operation with a initial state of a different asset."""

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
                "results": {"trades": 1200}
            }
        }
    }'''

    json_output = '''{
        "GOOG": {
            "2015-01-01": {
                "quantity": 10,
                "price": 650.33,
                "results": {}
            }
        },
        "ATVI": {
            "2014-06-09": {
                "quantity": 100,
                "price": 31.21,
                "results": {"trades": 1200}
            }
        }
    }'''


class TestJSONCase0102(TestJSON):
    """One operation and multiple initial states."""

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
                "results": {"trades": 1200}
            },
            "AAPL": {
                "date": "2015-11-09",
                "quantity": 92,
                "price": 31.21,
                "results": {"trades": 5000.72}
            }
        }
    }'''

    json_output = '''{
        "GOOG": {
            "2015-01-01": {
                "quantity": 10,
                "price": 650.33,
                "results": {}
            }
        },
        "ATVI": {
            "2014-06-09": {
                "quantity": 100,
                "price": 31.21,
                "results": {"trades": 1200}
            }
        },
        "AAPL": {
            "2015-11-09": {
                "quantity": 92,
                "price": 31.21,
                "results": {"trades": 5000.72}
            }
        }
    }'''


class TestJSONCase0103(TestJSON):
    """One operation and multiple initial states."""

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

    json_output = '''{
        "GOOG": {
            "2015-01-01": {
                "quantity": 10,
                "price": 650.11,
                "results": {}
            }
        },
        "AAPL": {
            "2015-11-09": {
                "quantity": 92,
                "price": 31.21,
                "results": {"trades": 5000.72}
            }
        }
    }'''
