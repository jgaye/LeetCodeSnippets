#########################################################################################################################################################
# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
#
# The test cases are generated so that the length of the output will never exceed 105.
#
#
#
# Example 1:
#
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
#
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
#
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
#
#
# Constraints:
#
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].
#########################################################################################################################################################
from typing import List
from collections import defaultdict, Counter, deque


class Solution:

    def decode_string(self, s: str) -> str:
        """
        Using stacks as a way to store the external string.
        When we are in the deepest local stack, we rebuild the local encoded string, then we build it back with the previous string and num

        Runtime 55 ms
        Beats 82.03 % of users with Python3
        Memory 16.74 MB
        Beats 66.94 % of users with Python3
        """

        stack, nums, curr_s, curr_n = [], [], "", ""
        for char in s:
            if char == "[":
                nums.append(int(curr_n))
                stack.append(curr_s)
                curr_s, curr_n = "", ""
            elif char == "]":
                curr_s = stack.pop() + nums.pop() * curr_s
            elif char.isdigit():
                curr_n += char
            else:
                curr_s += char

        return curr_s
