#########################################################################################################################################################
# Given a binary array nums, you should delete one element from it.
#
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
#
#
#
# Example 1:
#
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:
#
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:
#
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
#########################################################################################################################################################
from typing import List
from collections import defaultdict, Counter


class Solution:

    def longest_subarray(self, nums: List[int]) -> int:
        """
        Is there a binary solution to this?
        I can't figure it out, so let's just do a sliding window

        Runtime 414 ms
        Beats 97.21 % of users with Python3
        Memory 43.52 MB
        Beats 5.00 % of users with Python3
        """
        acc = []
        a_ones = extract_arrays_ones(0, nums, acc)

        if not a_ones:
            return 0

        # init_max on the first element
        mx = a_ones[0][1] - a_ones[0][0] + 1
        if len(a_ones) == 1:
            # if there was another 0 to delete, the max is correct
            # but if there was only those 1s, we need to delete one
            if mx == len(nums):
                return mx - 1
            return mx

        for i in range(1, len(a_ones)):
            if a_ones[i][0] == a_ones[i - 1][1] + 2:
                mx = max(
                    mx,
                    (a_ones[i][1] - a_ones[i][0] + 1)
                    + (a_ones[i - 1][1] - a_ones[i - 1][0] + 1),
                )
            else:
                mx = max(mx, a_ones[i][1] - a_ones[i][0] + 1)
        return mx


def extract_arrays_ones(offset: int, nums: List[int], acc: List[tuple]):
    try:
        l = nums.index(1)
    except ValueError:
        return acc

    try:
        r = l + nums[l:].index(0) - 1
    except ValueError:
        acc.append((offset + l, offset + len(nums) - 1))
        return acc

    acc.append((offset + l, offset + r))
    acc = extract_arrays_ones(offset + 1 + r, nums[r + 1 :], acc)
    return acc
