"""Test the JSON interface."""

from __future__ import absolute_import

from .test_json import TestJSON


class TestJSONCase0000(TestJSON):
    """One operation."""

    json_input = """{
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
                "quantity": 100,
                "price": 1,
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
                "volume": 0,
                "operations": 0
            },
            "purchases": {
                "volume": 100,
                "operations": 1
            },
            "operations": 1,
            "daytrades": 0,
            "results": {}
        },
        "assets": {
            "GOOG": {
                "totals": {
                    "sales": 0,
                    "purchases": 1,
                    "operations": 1,
                    "daytrades": 0,
                    "results": {}
                },
                "states": {
                    "2015-01-01": {
                        "results": {},
                        "price": 1.0,
                        "quantity": 100
                    }
                }
            }
        }
    }"""


class TestJSONCase0001(TestJSON):
    """Two operations with the same asset."""

    json_input = """{
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
                "quantity": 100,
                "price": 1,
                "commissions": {},
                "raw_results": {},
                "operations": []
            },
            {
                "type": "Operation",
                "subject": "GOOG",
                "date": "2015-01-02",
                "quantity": 100,
                "price": 2,
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
                "volume": 0,
                "operations": 0
            },
            "purchases": {
                "volume": 300,
                "operations": 2
            },
            "operations": 2,
            "daytrades": 0,
            "results": {}
        },
        "assets": {
            "GOOG": {
                "totals": {
                    "sales": 0,
                    "purchases": 2,
                    "operations": 2,
                    "daytrades": 0,
                    "results": {}
                },
                "states": {
                    "2015-01-02": {
                        "price": 1.5,
                        "quantity": 200,
                        "results": {}
                    },
                    "2015-01-01": {
                        "price": 1.0,
                        "quantity": 100,
                        "results": {}
                    }
                }
            }
        }
    }"""


class TestJSONCase0002(TestJSON):
    """Two operations with different assets on the same date."""

    json_input = """{
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
                "quantity": 100,
                "price": 650.0,
                "commissions": {},
                "raw_results": {},
                "operations": []
            },
            {
                "type": "Operation",
                "subject": "ATVI",
                "date": "2015-01-01",
                "quantity": 10,
                "price": 35.0,
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
                "volume": 0,
                "operations": 0
            },
            "purchases": {
                "volume": 65350.0,
                "operations": 2
            },
            "operations": 2,
            "daytrades": 0,
            "results": {}
        },
        "assets": {
            "GOOG": {
                "totals": {
                    "sales": 0,
                    "purchases": 1,
                    "operations": 1,
                    "daytrades": 0,
                    "results": {}
                },
                "states": {
                    "2015-01-01": {
                        "quantity": 100,
                        "price": 650.0,
                        "results": {}
                    }
                }
            },
            "ATVI": {
                "totals": {
                    "sales": 0,
                    "purchases": 1,
                    "operations": 1,
                    "daytrades": 0,
                    "results": {}
                },
                "states": {
                    "2015-01-01": {
                        "quantity": 10,
                        "price": 35.0,
                        "results": {}
                    }
                }
            }
        }
    }"""


class TestJSONCase0003(TestJSON):
    """Multiple operations with multiple assets."""

    json_input = """{
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
                "quantity": 100,
                "price": 650.0,
                "commissions": {},
                "raw_results": {},
                "operations": []
            },
            {
                "type": "Operation",
                "subject": "ATVI",
                "date": "2015-01-01",
                "quantity": 10,
                "price": 35.0,
                "commissions": {},
                "raw_results": {},
                "operations": []
            },
            {
                "type": "Operation",
                "subject": "ATVI",
                "date": "2015-01-02",
                "quantity": 20,
                "price": 34.0,
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
                "volume": 0,
                "operations": 0
            },
            "purchases": {
                "volume": 66030.0,
                "operations": 3
            },
            "operations": 3,
            "daytrades": 0,
            "results": {}
        },
        "assets": {
            "GOOG": {
                "totals": {
                    "sales": 0,
                    "purchases": 1,
                    "operations": 1,
                    "daytrades": 0,
                    "results": {}
                },
                "states": {
                    "2015-01-01": {
                        "quantity": 100,
                        "price": 650.0,
                        "results": {}
                    }
                }
            },
            "ATVI": {
                "totals": {
                    "sales": 0,
                    "purchases": 2,
                    "operations": 2,
                    "daytrades": 0,
                    "results": {}
                },
                "states": {
                    "2015-01-02": {
                        "quantity": 30,
                        "price": 34.333333333333336,
                        "results": {}
                    },
                    "2015-01-01": {
                        "quantity": 10,
                        "price": 35.0,
                        "results": {}
                    }
                }
            }
        }
    }"""


class TestJSONCase0004(TestJSON):
    """Multiple operations with multiple assets."""

    json_input = """{
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
                "quantity": 100,
                "price": 650.0,
                "commissions": {},
                "raw_results": {},
                "operations": []
            },
            {
                "type": "Operation",
                "subject": "ATVI",
                "date": "2015-01-01",
                "quantity": 10,
                "price": 35.0,
                "commissions": {},
                "raw_results": {},
                "operations": []
            },
            {
                "type": "Operation",
                "subject": "GOOG",
                "date": "2015-01-02",
                "quantity": 20,
                "price": 651.35,
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
                "volume": 0,
                "operations": 0
            },
            "purchases": {
                "volume": 78377.0,
                "operations": 3
            },
            "operations": 3,
            "daytrades": 0,
            "results": {}
        },
        "assets": {
            "GOOG": {
                "totals": {
                    "sales": 0,
                    "purchases": 2,
                    "operations": 2,
                    "daytrades": 0,
                    "results": {}
                },
                "states": {
                    "2015-01-02": {
                        "quantity": 120,
                        "price": 650.225,
                        "results": {}
                    },
                    "2015-01-01": {
                        "quantity": 100,
                        "price": 650.0,
                        "results": {}
                    }
                }
            },
            "ATVI": {
                "totals": {
                    "sales": 0,
                    "purchases": 1,
                    "operations": 1,
                    "daytrades": 0,
                    "results": {}
                },
                "states": {
                    "2015-01-01": {
                        "quantity": 10,
                        "price": 35.0,
                        "results": {}
                    }
                }
            }
        }
    }"""
