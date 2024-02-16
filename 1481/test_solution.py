from typing import List

import pytest
import src


@pytest.mark.parametrize(
    "test_input,test_input_k, expected",
    [
        ([5, 5, 4], 1, 1),
        ([4, 3, 1, 1, 3, 3, 2], 3, 2),
        ([5, 5, 4, 4, 3, 3], 3, 2),
        ([5, 5, 4, 4, 3, 3], 1, 3),
    ],
)
def test_find_least_num_of_unique_ints(
    test_input: List[int], test_input_k: int, expected: int
):
    assert (
        src.Solution().find_least_num_of_unique_ints(test_input, test_input_k)
        == expected
    )


if __name__ == "__main__":
    test_find_least_num_of_unique_ints()
