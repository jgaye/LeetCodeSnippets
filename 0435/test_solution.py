from typing import List

import pytest
import src


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
        ([[1, 2], [3, 4]], 0),
        ([[1, 3], [2, 5], [4, 5]], 1),
        ([[1, 3], [2, 5]], 1),
        ([[1, 5], [2, 4]], 1),
        ([[1, 100], [11, 22], [1, 11], [2, 12]], 2),
        ([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]], 2),
        ([[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]], 4),
        (
            [
                [-25322, -4602],
                [-35630, -28832],
                [-33802, 29009],
                [13393, 24550],
                [-10655, 16361],
                [-2835, 10053],
                [-2290, 17156],
                [1236, 14847],
                [-45022, -1296],
                [-34574, -1993],
                [-14129, 15626],
                [3010, 14502],
                [42403, 45946],
                [-22117, 13380],
                [7337, 33635],
                [-38153, 27794],
                [47640, 49108],
                [40578, 46264],
                [-38497, -13790],
                [-7530, 4977],
                [-29009, 43543],
                [-49069, 32526],
                [21409, 43622],
                [-28569, 16493],
                [-28301, 34058],
            ],
            19,
        ),
    ],
)
def test_erase_overlap_intervals(intervals: List[List[int]], expected: int):
    assert src.Solution().erase_overlap_intervals(intervals) == expected


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], True),
        ([[1, 2], [1, 2], [1, 2]], True),
        ([[1, 2], [2, 3]], False),
        ([[1, 2], [3, 4]], False),
        ([[1, 3], [2, 5], [4, 5]], True),
        ([[1, 3], [2, 5]], True),
        ([[1, 5], [2, 4]], True),
    ],
)
def test_check_overlap(intervals: List[List[int]], expected: bool):
    assert src.check_overlap(intervals) == expected


if __name__ == "__main__":
    test_erase_overlap_intervals()
