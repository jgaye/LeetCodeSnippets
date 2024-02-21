from typing import List

import pytest
import src


@pytest.mark.parametrize(
    "asteroids, expected,",
    [
        # ([5, 10, -5], [5, 10]),
        ([-2, -1, 1, 2], [-2, -1, 1, 2]),
        # ([8, -8], []),
        # ([10, 2, -5], [10]),
        ([-2, -2, 1, -2], [-2, -2, -2]),
    ],
)
def test_asteroid_collision(asteroids: List[int], expected: List[int]):
    assert src.Solution().asteroid_collision(asteroids) == expected


if __name__ == "__main__":
    test_asteroid_collision()
