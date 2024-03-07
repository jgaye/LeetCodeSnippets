from typing import List

import pytest
import src


@pytest.mark.parametrize(
    # NOTE you need more complex examples to test all scenarios
    "s, expected",
    [
        ("3[a]", "aaa"),
        ("aaaaa", "aaaaa"),
        ("3[a2[c]]", "accaccacc"),
        ("3[a2[c]a2[b]]", "accabbaccabbaccabb"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        (
            "100[leetcode]",
            "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode",
        ),
        (
            "5[a5[b5[c]de]]",
            "abcccccdebcccccdebcccccdebcccccdebcccccdeabcccccdebcccccdebcccccdebcccccdebcccccdeabcccccdebcccccdebcccccdebcccccdebcccccdeabcccccdebcccccdebcccccdebcccccdebcccccdeabcccccdebcccccdebcccccdebcccccdebcccccde",
        ),
    ],
)
def test_decode_string(s: str, expected: str):
    assert src.Solution().decode_string(s) == expected


if __name__ == "__main__":
    test_decode_string()
