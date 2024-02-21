from typing import List

import pytest
import src


@pytest.mark.parametrize(
    # NOTE you need more complex examples to test all scenarios
    "left, right, expected",
    [
        (5, 7, 4),
        (0, 0, 0),
        (1, 12345678, 0),
        (600000000, 2147483645, 0),
        (1073741824, 2147483647, 1073741824),
    ],
)
def test_range_bitwise_and(left: int, right: int, expected: int):
    assert src.Solution().range_bitwise_and(left, right) == expected


if __name__ == "__main__":
    test_range_bitwise_and()
