"""Tests for the JSON interface with options and exercise operations."""

from __future__ import absolute_import

from .test_json import TestJSON


class TestJSONCase0300(TestJSON):
    """Option operations."""

    json_input = """{
        "subjects": {
            "ASSET": {
                "type": "Asset",
                "name": "Some Asset"
            },
            "OPTION": {
                "type": "Option",
                "name": "Some Option",
                "underlying_assets": {"ASSET":1},
                "expiration_date": "2015-12-23"
            }
        },
        "occurrences": [
            {
                "type": "Operation",
                "subject": "OPTION",
                "date": "2015-01-01",
                "quantity": 10,
                "price": 650.33
            },
            {
                "type": "Operation",
                "subject": "ASSET",
                "date": "2015-01-02",
                "quantity": 10,
                "price": 650.33
            },
            {
                "type": "Operation",
                "subject": "ASSET",
                "date": "2015-01-02",
                "quantity": -10,
                "price": 651.33
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
            "OPTION": {
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
                        "price": 650.33,
                        "results": {}
                    }
                }
            },
            "ASSET": {
                "totals": {
                    "sales": 1,
                    "purchases": 1,
                    "operations": 2,
                    "daytrades": 1,
                    "results": {
                        "daytrades": 10.0
                    }
                },
                "states": {
                    "2015-01-02": {
                        "quantity": 0,
                        "price": 0,
                        "results": {
                            "daytrades": 10.0
                        }
                    }
                }
            }
        }
    }"""


class TestJSONCase0301(TestJSON):
    """An exercise operation."""

    json_input = """{
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
    }"""


    json_output = """{
        "totals": {
            "sales": {
                "volume": 0,
                "operations": 0
            },
            "purchases": {
                "volume": 50,
                "operations": 2
            },
            "operations": 2,
            "daytrades": 0,
            "results": {}
        },
        "assets": {
            "OPTION": {
                "totals": {
                    "sales": 0,
                    "purchases": 2,
                    "operations": 2,
                    "daytrades": 0,
                    "results": {}
                },
                "states": {
                    "2015-01-01": {
                        "quantity": 10,
                        "price": 1.0,
                        "results": {}
                    },
                    "2015-01-03": {
                        "quantity": 0,
                        "price": 0,
                        "results": {}
                    }
                }
            },
            "ASSET": {
                "totals": {
                    "sales": 0,
                    "purchases": 0,
                    "operations": 0,
                    "daytrades": 0,
                    "results": {}
                },
                "states": {
                    "2015-01-03": {
                        "quantity": 10,
                        "price": 5,
                        "results": {}
                    }
                }
            }
        }
    }"""



class TestJSONCase0302(TestJSON):
    """An exercise operation that generates results."""

    json_input = """{
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
                "type": "Operation",
                "subject": "ASSET",
                "date": "2015-01-02",
                "quantity": -10,
                "price": 7
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
    }"""


    json_output = """{
        "totals": {
            "sales": {
                "volume": 70,
                "operations": 1
            },
            "purchases": {
                "volume": 50,
                "operations": 2
            },
            "operations": 3,
            "daytrades": 0,
            "results": {
                "trades": 20
            }
        },
        "assets": {
            "OPTION": {
                "totals": {
                    "sales": 0,
                    "purchases": 2,
                    "operations": 2,
                    "daytrades": 0,
                    "results": {}
                },
                "states": {
                    "2015-01-01": {
                        "quantity": 10,
                        "price": 1.0,
                        "results": {}
                    },
                    "2015-01-03": {
                        "quantity": 0,
                        "price": 0,
                        "results": {}
                    }
                }
            },
            "ASSET": {
                "totals": {
                    "sales": 1,
                    "purchases": 0,
                    "operations": 1,
                    "daytrades": 0,
                    "results": {
                        "trades": 20
                    }
                },
                "states": {
                    "2015-01-02": {
                        "quantity": -10,
                        "price": 7,
                        "results": {}
                    },
                    "2015-01-03": {
                        "quantity": 0,
                        "price": 0,
                        "results": {
                            "trades": 20
                        }
                    }
                }
            }
        }
    }"""
