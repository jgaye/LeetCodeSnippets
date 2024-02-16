from typing import List

import pytest
import src


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([3, 1, -2, -5, 2, -4], [3, -2, 1, -5, 2, -4]),
        ([-1, 1], [1, -1]),
        (
            list(range(1, 100000, 10000)) + list(range(-100000, -1, 10000)),
            [
                1,
                -100000,
                10001,
                -90000,
                20001,
                -80000,
                30001,
                -70000,
                40001,
                -60000,
                50001,
                -50000,
                60001,
                -40000,
                70001,
                -30000,
                80001,
                -20000,
                90001,
                -10000,
            ],
        ),
    ],
)
def test_rearrange_array(test_input: List[int], expected: List[int]):
    assert src.Solution().rearrange_array(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([3, 1, -2, -5, 2, -4], [3, -2, 1, -5, 2, -4]),
        ([-1, 1], [1, -1]),
        ([3, 1, 2, -2, -5, -4], [3, -2, 1, -5, 2, -4]),
        ([-2, -5, -4, 3, 1, 2], [3, -2, 1, -5, 2, -4]),
        # (
        #     list(range(1, 100000, 10000)) + list(range(-100000, -1, 10000)),
        #     [
        #         1,
        #         -100000,
        #         10001,
        #         -90000,
        #         20001,
        #         -80000,
        #         30001,
        #         -70000,
        #         40001,
        #         -60000,
        #         50001,
        #         -50000,
        #         60001,
        #         -40000,
        #         70001,
        #         -30000,
        #         80001,
        #         -20000,
        #         90001,
        #         -10000,
        #     ],
        # ),
    ],
)
def test_recursive_rearrange_array(test_input: List[int], expected: List[int]):
    assert src.Solution().recursive_rearrange_array(test_input) == expected


if __name__ == "__main__":
    test_rearrange_array()
