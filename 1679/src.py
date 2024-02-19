#########################################################################################################################################################
# You are given an integer array nums and an integer k.
#
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
#
# Return the maximum number of operations you can perform on the array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:
#
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109
#########################################################################################################################################################
from typing import List


class Solution:
    def max_operations(self, nums: List[int], k: int) -> int:
        """
        Intuition: the naive solution of checking the whole list for each item will be too slow quick
        But with 2 indexes we could optimize this, as for a sorted list, the complement of a number on the left should be on the right

        Approach: Lets start by sorting, and remove all numbers that are >= k (they won't have a complement
        Use 2 index left/right.
        left index is slow.
        If l+r > k, move the r index (there won't be a matching l for that r because all other l are higher)
        If l+r == k, one operation counted
        If l+r < k, move l index

        Runtime 533 ms
        Beats 55.37 % of users with Python3
        Memory 31.70 MB
        Beats 83.74 % of users with Python3
        """

        nums = [num for num in nums if num < k]
        nums.sort()

        count, l, r = 0, 0, len(nums) - 1

        while l < r:
            if nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                count += 1
                l += 1
                r -= 1

        return count
