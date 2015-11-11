"""Tests for the JSON interface."""

from __future__ import absolute_import

from .test_json import TestJSON


class TestJSONCase0200(TestJSON):
    """One operation with a initial state."""

    json_input = """{
        "subjects": {
            "GOOG": {
                "type": "Asset",
                "name": "Google Inc",
                "expiration_date": ""
            },
            "AAPL": {
                "type": "Asset",
                "name": "Apple, Inc",
                "expiration_date": ""
            }
        },
        "occurrences": [
            {
                "type": "Operation",
                "subject": "AAPL",
                "date": "2015-01-01",
                "quantity": 10,
                "price": 650.33,
                "commissions": {},
                "raw_results": {},
                "operations": []
            },
            {
                "type": "Operation",
                "subject": "AAPL",
                "date": "2015-01-02",
                "quantity": 10,
                "price": 650.33,
                "commissions": {},
                "raw_results": {},
                "operations": []
            },
            {
                "type": "Operation",
                "subject": "AAPL",
                "date": "2015-01-02",
                "quantity": -10,
                "price": 651.33,
                "commissions": {},
                "raw_results": {},
                "operations": []
            }
        ],
        "initial state": {}
    }"""

    json_output = """{
        "totals": {
            "sales": {
                "volume": 6513.3,
                "operations": 1
            },
            "purchases": {
                "volume": 13006.6,
                "operations": 2
            },
            "operations": 3,
            "daytrades": 1,
            "results": {
                "daytrades": 10.0
            }
        },
        "assets": {
            "AAPL": {
                "totals": {
                    "sales": 1,
                    "purchases": 2,
                    "operations": 3,
                    "daytrades": 1,
                    "results": {
                        "daytrades": 10.0
                    }
                },
                "states": {
                    "2015-01-01": {
                        "quantity": 10,
                        "price": 650.33,
                        "results": {}
                    },
                    "2015-01-02": {
                        "quantity": 10,
                        "price": 650.33,
                        "results": {
                            "daytrades": 10.0
                        }
                    }
                }
            }
        }
    }"""


class TestJSONCase0201(TestJSON):
    """One operation with a initial state."""

    json_input = """{
        "subjects": {
            "GOOG": {
                "type": "Asset",
                "name": "Google Inc",
                "expiration_date": ""
            },
            "AAPL": {
                "type": "Asset",
                "name": "Apple, Inc",
                "expiration_date": ""
            }
        },
        "occurrences": [
            {
                "type": "Operation",
                "subject": "AAPL",
                "date": "2015-01-01",
                "quantity": 10,
                "price": 650.33,
                "commissions": {},
                "raw_results": {},
                "operations": []
            },
            {
                "type": "Operation",
                "subject": "AAPL",
                "date": "2015-01-02",
                "quantity": 10,
                "price": 650.33,
                "commissions": {},
                "raw_results": {},
                "operations": []
            },
            {
                "type": "Operation",
                "subject": "AAPL",
                "date": "2015-01-02",
                "quantity": -10,
                "price": 651.33,
                "commissions": {},
                "raw_results": {},
                "operations": []
            }
        ],
        "initial state": {
            "GOOG": {
                "date": "2015-01-01",
                "quantity": 100,
                "price": 654.21,
                "results": {"trades": 1200}
            }
        }
    }"""

    json_output = """{
        "totals": {
            "sales": {
                "volume": 6513.3,
                "operations": 1
            },
            "purchases": {
                "volume": 13006.6,
                "operations": 2
            },
            "operations": 3,
            "daytrades": 1,
            "results": {
                "daytrades": 10.0,
                "trades": 1200
            }
        },
        "assets": {
            "GOOG": {
                "totals": {
                    "sales": 0,
                    "purchases": 0,
                    "operations": 0,
                    "daytrades": 0,
                    "results": {
                        "trades": 1200
                    }
                },
                "states": {
                    "2015-01-01": {
                        "quantity": 100,
                        "price": 654.21,
                        "results": {
                            "trades": 1200
                        }
                    }
                }
            },
            "AAPL": {
                "totals": {
                    "sales": 1,
                    "purchases": 2,
                    "operations": 3,
                    "daytrades": 1,
                    "results": {
                        "daytrades": 10.0
                    }
                },
                "states": {
                    "2015-01-01": {
                        "quantity": 10,
                        "price": 650.33,
                        "results": {}
                    },
                    "2015-01-02": {
                        "quantity": 10,
                        "price": 650.33,
                        "results": {
                            "daytrades": 10.0
                        }
                    }
                }
            }
        }
    }"""
