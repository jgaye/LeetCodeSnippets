from typing import List

import pytest
import src


@pytest.mark.parametrize(
    "nums, k,expected",
    [([1, 2, 3, 4], 5, 2), ([3, 1, 3, 4, 3], 6, 1)],
)
def test_max_operations(nums: List[int], k: int, expected: List[int]):
    assert src.Solution().max_operations(nums, k) == expected


if __name__ == "__main__":
    test_max_operations()
