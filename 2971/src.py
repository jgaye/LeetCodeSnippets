#########################################################################################################################################################
# You are given an array of positive integers nums of length n.
#
# A polygon is a closed plane figure that has at least 3 sides. The longest side of a polygon is smaller than the sum of its other sides.
#
# Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak, then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.
#
# The perimeter of a polygon is the sum of lengths of its sides.
#
# Return the largest possible perimeter of a polygon whose sides can be formed from nums, or -1 if it is not possible to create a polygon.
#
#
#
# Example 1:
#
# Input: nums = [5,5,5]
# Output: 15
# Explanation: The only possible polygon that can be made from nums has 3 sides: 5, 5, and 5. The perimeter is 5 + 5 + 5 = 15.
# Example 2:
#
# Input: nums = [1,12,1,2,5,50,3]
# Output: 12
# Explanation: The polygon with the largest perimeter which can be made from nums has 5 sides: 1, 1, 2, 3, and 5. The perimeter is 1 + 1 + 2 + 3 + 5 = 12.
# We cannot have a polygon with either 12 or 50 as the longest side because it is not possible to include 2 or more smaller sides that have a greater sum than either of them.
# It can be shown that the largest possible perimeter is 12.
# Example 3:
#
# Input: nums = [5,5,50]
# Output: -1
# Explanation: There is no possible way to form a polygon from nums, as a polygon has at least 3 sides and 50 > 5 + 5.
#
#
# Constraints:
#
# 3 <= n <= 105
# 1 <= nums[i] <= 109
#########################################################################################################################################################
from math import floor, ceil, prod
from typing import List


class Solution:
    def largest_perimeter(self, nums: List[int]) -> int:
        """
        We will remove all the sides that are too long and construct the final polygon after that
        A side x is too long if x >= sum(other sides)

        I will do a recursive solution (from sorted) checking a head (list) and a tail (int)
        The tail is a candidate side, that could be too long
        The head is the rest of the polygon sides
        If the tail is not too long, we can construct a polygon -> return the perimeter
        If the tail is too long, the last element of the head become a candidate -> run next recursion
        If we end up with less than 3 sides, we cannot construct a polygon -> return -1

        Runtime 533 ms
        Beats 55.37 % of users with Python3
        Memory 31.70 MB
        Beats 83.74 % of users with Python3
        """

        # Edge case: input too small to construct a polygon
        if len(nums) < 3:
            return -1

        nums.sort()

        def rec_pol_check(head: List[int], tail: int) -> int:
            if len(head) < 2:
                return -1

            sum_head = sum(head)
            if tail >= sum_head:
                return rec_pol_check(head[:-1], head[-1])

            return sum_head + tail

        return rec_pol_check(nums[:-1], nums[-1])
