from typing import List

import pytest
import src


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([5, 5, 5], 15),
        ([1, 12, 1, 2, 5, 50, 3], 12),
        ([5, 5, 50], -1),
        ([5], -1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 69, 70], 184),
        ([1, 2, 3, 10, 11, 12], 39),
    ],
)
def test_largest_perimeter(test_input: List[int], expected: List[int]):
    assert src.Solution().largest_perimeter(test_input) == expected


if __name__ == "__main__":
    test_largest_perimeter()
