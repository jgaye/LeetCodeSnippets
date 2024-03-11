#########################################################################################################################################################
# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
#
# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.
#
# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.
#
#
#
# Example 1:
#
# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.
# Example 2:
#
# Input: spells = [3,1,2], potions = [8,5,8], success = 16
# Output: [2,0,2]
# Explanation:
# - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
# - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful.
# - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful.
# Thus, [2,0,2] is returned.
#
#
# Constraints:
#
# n == spells.length
# m == potions.length
# 1 <= n, m <= 105
# 1 <= spells[i], potions[i] <= 105
# 1 <= success <= 1010
#########################################################################################################################################################
import bisect
import heapq
import math
from heapq import heapify
from typing import List
from collections import defaultdict, Counter


class Solution:
    def successful_pairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        """
        For each spell we identified the min_potion value that will then give only successes
        Then using a bisect search to find the first value of potions that would give a success
        len - index will give us the number of successes

        Runtime 890 ms
        Beats 82.48 % of users with Python3
        Memory 39.78 MB
        Beats 44.24 % of users with Python3
        """

        r = []

        potions.sort()
        for s in spells:
            min_potion = success / s
            r.append(len(potions) - search_first_higher(potions, min_potion))

        return r

    def successful_pairs_slow(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        """Works but times out for big sizes of potions/spell array (with thousands of items in each)"""
        r = []
        for s in spells:
            pt = [1 for p in potions if s * p >= success]
            r.append(sum(pt))

        return r


def search_first_higher(elements: List[int], threshold: float) -> int:
    """
    Assumes a sorted list of int
    Returns the index of the first element higher than threshold
    Use binary search with bisect
    """
    return bisect.bisect_left(elements, threshold)
