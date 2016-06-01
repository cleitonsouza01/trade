"""Logs."""

from fixtures.accumulator_states import (
    EXPECTED_STATE0
)


EXPECTED_LOG17 = {
    '2015-09-24': EXPECTED_STATE0
}

EXPECTED_LOG18 = {
    '2015-09-25': EXPECTED_STATE0,
    '2015-09-24': EXPECTED_STATE0
}
