#########################################################################################################################################################
# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
#
# You should rearrange the elements of nums such that the modified array follows the given conditions:
#
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
#
#
#
# Example 1:
#
# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
# Explanation:
# The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
# The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
# Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.
# Example 2:
#
# Input: nums = [-1,1]
# Output: [1,-1]
# Explanation:
# 1 is the only positive integer and -1 the only negative integer in nums.
# So nums is rearranged to [1,-1].
#
#
# Constraints:
#
# 2 <= nums.length <= 2 * 105
# nums.length is even
# 1 <= |nums[i]| <= 105
# nums consists of equal number of positive and negative integers.
#########################################################################################################################################################
from math import floor, ceil, prod
from typing import List


class Solution:
    def rearrange_array(self, nums: List[int]) -> List[int]:
        """
        extract the positive and negative values in 2 arrays in the SAME ORDER
        zip the 2 resulting array

        Runtime 1015 ms
        Beats 65.00 % of users with Python3
        Memory 47.30 MB
        Beats 70.08 % of users with Python3
        """
        pos = []
        neg = []

        # No zeros (based on constraints)
        for e in nums:
            if e > 0:
                pos.append(e)
            else:
                neg.append(e)
        r = []
        for t in list(zip(pos, neg)):
            r.append(t[0])
            r.append(t[1])

        return r

    def recursive_rearrange_array(self, nums: List[int]) -> List[int]:
        """
        Try a recursive sort

        O(nlogn) I think
        Too slow and very dirty
        """

        if len(nums) == 2:
            if nums[0] < nums[1]:
                return [nums[1], nums[0]]
            return [nums[0], nums[1]]

        for i in range(0, len(nums) - 1, 2):
            if nums[i] > 0:
                j = 2
                while prod(nums[i : i + j]) > 0:
                    j += 1
                nums[i : i + j] = [nums[i], nums[i + j - 1], *nums[i + 1 : i + j - 1]]

            else:
                j = 2
                while prod(nums[i : i + j]) * pow(-1, j - 1) < 0:
                    j += 1
                nums[i : i + j] = [nums[i + j - 1], nums[i], *nums[i + 1 : i + j - 1]]

        return nums
