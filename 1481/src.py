#########################################################################################################################################################
# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
#
#
#
# Example 1:
#
# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
#
#
# Constraints:
#
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^9
# 0 <= k <= arr.length
#########################################################################################################################################################
from typing import List
from collections import defaultdict, Counter


class Solution:

    def find_least_num_of_unique_ints(self, arr: List[int], k: int) -> int:
        """
        My first solution (see below) was slow because of the decrement method of k
        I think the list operations where slow.
        Also:
        - I learned about the Counter class
        - no need to sort with the keys, only the values were necessary

        Runtime 316 ms
        Beats 92.47 % of users with Python3
        Memory 33.32 MB
        Beats 84.81 % of users with Python3
        """

        counts = Counter(arr)
        sorted_counts = list(counts.values())
        sorted_counts.sort()

        r = len(sorted_counts)
        for e in sorted_counts:
            if k >= e:
                k -= e
                r -= 1
            if k < e:
                break

        return r

    def find_least_num_of_unique_ints_SLOW(self, arr: List[int], k: int) -> int:
        """
        Count appearance of elements in a defaultdict
        Sort with increasing count value
        Going through the elements, reduce k by counts. If a count gets to 0, pop the element.
        Then count the nb of elements lefts in the dict


        Runtime 1153 ms
        Beats 5.01 % of users with Python3
        Memory 36.84 MB
        Beats 40.07 % of users with Python3
        """

        def default_to_zero():
            return 0

        counts = defaultdict(default_to_zero)
        for e in arr:
            counts[e] = counts[e] + 1

        sorted_counts = [v for k, v in sorted(counts.items(), key=lambda e: e[1])]

        while k > 0:
            k -= sorted_counts[0]
            if k >= 0:
                sorted_counts.pop(0)

        return len(sorted_counts)
