from typing import List

import pytest
import src


@pytest.mark.parametrize(
    "test_input, expected",
    [
        # ([1, 1, 0, 1], 3),
        # ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
        ([1, 1, 1], 2),
        # ([0], 0),
        # ([0, 0, 0, 0, 0], 0),
        # ([0, 0, 1, 0, 0], 1),
    ],
)
def test_longest_subarray(test_input: List[int], expected: int):
    assert src.Solution().longest_subarray(test_input) == expected


if __name__ == "__main__":
    test_longest_subarray()
