from typing import List

import pytest
import src


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["abc", "car", "ada", "racecar", "cool"], "ada"),
        (["notapalindrome", "racecar"], "racecar"),
        (["def", "ghi"], ""),
    ],
)
def test_first_palindrome(test_input: List[str], expected: str):
    assert src.Solution().first_palindrome(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["abc", "car", "ada", "racecar", "cool"], "ada"),
        (["notapalindrome", "racecar"], "racecar"),
        (["def", "ghi"], ""),
    ],
)
def test_first_palindrome_faster(test_input: List[str], expected: str):
    assert src.Solution().first_palindrome_faster(test_input) == expected


if __name__ == "__main__":
    test_first_palindrome()
