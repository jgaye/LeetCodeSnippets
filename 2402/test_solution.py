from typing import List

import pytest
import src


@pytest.mark.parametrize(
    "n, meetings, expected",
    [
        (2, [[0, 10], [1, 5], [2, 7], [3, 4]], 0),
        (2, [[2, 7], [0, 10], [3, 4], [1, 5]], 0),
        (3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]], 1),
        (100, [[0, 1]], 0),
        (2, [[0, 10], [1, 2], [12, 14], [13, 15]], 0),
        (3, [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6]], 1),
        (
            4,
            [
                [12, 44],
                [27, 37],
                [48, 49],
                [46, 49],
                [24, 44],
                [32, 38],
                [21, 49],
                [13, 30],
            ],
            1,
        ),
        (
            4,
            [
                [48, 49],
                [22, 30],
                [13, 31],
                [31, 46],
                [37, 46],
                [32, 36],
                [25, 36],
                [49, 50],
                [24, 34],
                [6, 41],
            ],
            0,
        ),
    ],
)
def test_find_least_num_of_unique_ints(
    n: int, meetings: List[List[int]], expected: int
):
    assert src.Solution().most_booked(n, meetings) == expected


if __name__ == "__main__":
    test_find_least_num_of_unique_ints()
