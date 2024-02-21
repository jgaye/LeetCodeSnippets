#########################################################################################################################################################
# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
#
# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
#
#
#
# Example 1:
#
#
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
# Example 2:
#
#
# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]
#
#
# Constraints:
#
# n == grid.length == grid[i].length
# 1 <= n <= 200
# 1 <= grid[i][j] <= 105
#########################################################################################################################################################
import heapq
from heapq import heapify
from typing import List
from collections import defaultdict, Counter


class Solution:
    def equal_pairs(self, grid: List[List[int]]) -> int:
        """
        I've dealt with grid before, so maybe this will be easy?
        Make the rows and columns and just compare?

        Make the columns by using zip
        Then use counters / sets to find the common elements (you need to transform the elements of the lists into str)
        The common elements multiply: count_1 * count_2 must be added to the accumulator

        Runtime 422 ms
        Beats 57.58 % of users with Python3
        Memory 21.40 MB
        Beats 72.91 % of users with Python3
        """
        # rows = grid
        # columns = [list(e) for e in zip(*grid)]
        #
        # acc = 0
        # for r in rows:
        #     columns.
        #     for c in columns:
        #         if r == c:
        #             acc += 1
        # return acc

        # counter solutions
        rows = [str(e) for e in grid]
        columns = [str(list(e)) for e in zip(*grid)]
        rc, cc = Counter(rows), Counter(columns)

        acc = 0
        for e in set(rc).intersection(set(cc)):
            acc += rc[e] * cc[e]
        return acc
