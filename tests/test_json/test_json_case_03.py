"""Test the JSON interface."""

from __future__ import absolute_import

from .test_json import TestJSON


class TestJSONCase0300(TestJSON):
    """One operation."""

    json_input = """{
        "subjects": {
            "ASST1": {
                "type": "Asset",
                "name": "Asset 1"
            },
            "ASST2": {
                "type": "Asset",
                "name": "Asset 2",
                "underlying_assets": {"ASST1":1}
            }
        },
        "occurrences": [
            {
                "type": "Operation",
                "subject": "ASST2",
                "date": "2016-01-01",
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
            "ASST2": {
                "totals": {
                    "sales": 0,
                    "purchases": 1,
                    "operations": 1,
                    "daytrades": 0,
                    "results": {}
                },
                "states": {
                    "2016-01-01": {
                        "results": {},
                        "price": 1.0,
                        "quantity": 100
                    }
                }
            }
        }
    }"""
