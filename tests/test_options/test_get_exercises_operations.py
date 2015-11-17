"""Test the trade.plugins.fetch_exercises task from the Option plugin."""

from __future__ import absolute_import

from tests.test_operation_container.container_test_base import TestFetchPositions
from tests.fixtures.operations import (
    EXERCISE_OPERATION2, EXERCISE_OPERATION3
)
from tests.fixtures.assets import OPTION1


class TestFetchExercisesCase00(TestFetchPositions):
    """Test the fetch_exercises() task of the Accumulator."""

    volume = 100
    operations = [EXERCISE_OPERATION2]
    exercises = {
        OPTION1.symbol: {
            'quantity': 100,
            'price': 1,
            'volume': 0,
        }
    }


class TestFetchExercisesCase01(TestFetchPositions):
    """Test the fetch_exercises() task of the Accumulator."""

    volume = 400
    operations = [EXERCISE_OPERATION2, EXERCISE_OPERATION3]
    exercises = {
        OPTION1.symbol: {
            'quantity': 200,
            'price': 2,
            'volume': 0,
        }
    }
