from typing import List

import pytest
import src


@pytest.mark.parametrize(
    "heights, bricks, ladders, expected",
    [
        ([4, 2, 7, 6, 9, 14, 12], 5, 1, 4),
        ([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2, 7),
        ([14, 3, 19, 3], 17, 0, 3),
        ([4, 2, 7, 6, 9, 11, 12], 5, 1, 5),
    ],
)
def test_furthest_building(
    heights: List[int], bricks: int, ladders: int, expected: int
):
    assert src.Solution().furthest_building(heights, bricks, ladders) == expected


if __name__ == "__main__":
    test_furthest_building()
