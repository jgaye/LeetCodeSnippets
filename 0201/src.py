#########################################################################################################################################################
# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
#
#
#
# Example 1:
#
# Input: left = 5, right = 7
# Output: 4
# Example 2:
#
# Input: left = 0, right = 0
# Output: 0
# Example 3:
#
# Input: left = 1, right = 2147483647
# Output: 0
#
#
# Constraints:
#
# 0 <= left <= right <= 231 - 1
#########################################################################################################################################################
from typing import List
from collections import defaultdict, Counter


class Solution:

    def range_bitwise_and(self, left: int, right: int) -> int:
        """
        It feels like there could be a smart solution based on the power of 2 of the leftmost number
        Every time you add a number there is less and less AND ones...
        What we are trying to figure out is what is the matching prefix of those 2 numbers
        which is what their And would return
        I'm using bit shifts to figure that out

        Runtime 58 ms
        Beats 35.82 % of users with Python3
        Memory 16.60 MB
        Beats 56.93 % of users with Python3
        """
        # case 1: not the same pow of 2
        # then it will always be 0
        # because left will be 01<n-1 digits> and we will pass the number 10<n-1 ZEROS>
        # CODE RUN FASTER WITHOUT THIS CASE
        # for i in range(0, 32):
        #     if right >= pow(2, i) > left:
        #         return 0

        # What we are trying to figure out is what is the matching prefix of those 2 numbers
        # which is what their And would return
        # I'm using bit shifts to figure that out
        acc = 0
        while left != right:
            left, right, acc = left >> 1, right >> 1, acc + 1
        return left << acc

    def range_bitwise_and_slow(self, left: int, right: int) -> int:
        """
        Naive solution, too slow for big numbers
        """
        acc = left
        for i in range(left + 1, right + 1):
            acc = acc & i
            if acc == 0:
                return 0

        print(acc)
        return acc
