from typing import List

import pytest
import src


@pytest.mark.parametrize(
    "temperatures, expected,",
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        (
            [78, 77, 76, 75, 74, 73, 72, 71, 70, 71, 72, 73, 74, 75, 76, 77],
            [0, 0, 13, 11, 9, 7, 5, 3, 1, 1, 1, 1, 1, 1, 1, 0],
        ),
    ],
)
def test_daily_temperatures(temperatures: List[int], expected: List[int]):
    assert src.Solution().daily_temperatures(temperatures) == expected


if __name__ == "__main__":
    test_daily_temperatures()
