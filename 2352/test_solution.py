from typing import List

import pytest
import src


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1),
        ([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], 3),
    ],
)
def test_equal_pairs(grid: List[List[int]], expected: int):
    assert src.Solution().equal_pairs(grid) == expected


if __name__ == "__main__":
    test_equal_pairs()
