#########################################################################################################################################################
# You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.
#
# You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
#
# While moving from building i to building i+1 (0-indexed),
#
# If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
# If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
# Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
#
#
#
# Example 1:
#
#
# Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
# Output: 4
# Explanation: Starting at building 0, you can follow these steps:
# - Go to building 1 without using ladders nor bricks since 4 >= 2.
# - Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
# - Go to building 3 without using ladders nor bricks since 7 >= 6.
# - Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
# It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
# Example 2:
#
# Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
# Output: 7
# Example 3:
#
# Input: heights = [14,3,19,3], bricks = 17, ladders = 0
# Output: 3
#
#
# Constraints:
#
# 1 <= heights.length <= 105
# 1 <= heights[i] <= 106
# 0 <= bricks <= 109
# 0 <= ladders <= heights.length
#########################################################################################################################################################
import heapq
import itertools
from typing import List
from collections import defaultdict, Counter


class Solution:

    def furthest_building(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Extracted from the most upvoted solution, as my other implem were too slow

        Runtime 410 ms
        Beats 90.55 % of users with Python3
        Memory 31.15 MB
        Beats 57.95 % of users with Python3
        """

        heap = []
        for i in range(len(heights) - 1):
            d = heights[i + 1] - heights[i]
            if d > 0:
                heapq.heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(heights) - 1

    def furthest_building_less_slow(
        self, heights: List[int], bricks: int, ladders: int
    ) -> int:
        """
        All depends what you do with the ladders
        Strategies
        1. try to optimize ladders with an holistic approach
        2. Test all paths

        Holistic approach: we should have used a ladder for the BIGGEST jump
        Iterating through the jump, keeping the value of the one where we needed to use bricks or ladders
        For each climb, if the climb is bigger than one before, we will swap with a previous ladder use

        This also times out on big use cases

        Runtime 55 ms
        Beats 82.03 % of users with Python3
        Memory 16.74 MB
        Beats 66.94 % of users with Python3
        """

        ladder_climbs: list[int] = []
        min_ladder_climb = 0
        brick_clims: int = 0

        for i in range(0, len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            if ladders > 0:
                ladder_climbs.append(diff)
                ladders -= 1
            else:
                if ladder_climbs and diff > min(ladder_climbs):
                    brick_clims += min(ladder_climbs)
                    ladder_climbs.remove(min(ladder_climbs))
                    ladder_climbs.append(diff)
                else:
                    brick_clims += diff

            if brick_clims > bricks:
                return i

        return len(heights) - 1

    def furthest_building_slow(
        self, heights: List[int], bricks: int, ladders: int
    ) -> int:
        """
        All depends what you do with the ladders
        Strategies
        1. try to optimize ladders with an holistic approach
        2. Test all paths

        This implementation tests all paths
        Too slow for big inputs

        Runtime 55 ms
        Beats 82.03 % of users with Python3
        Memory 16.74 MB
        Beats 66.94 % of users with Python3
        """

        def try_permutation(heights: list[int], bricks: int, ladder_arr: list[int]):
            for i in range(0, len(heights) - 1):
                diff = heights[i + 1] - heights[i]
                if diff <= 0:
                    continue

                if ladder_arr[i] == 1:
                    continue

                bricks -= diff
                if bricks < 0:
                    return i

            return len(heights) - 1

        init_perm = [1] * ladders + [0] * (len(heights) - ladders)
        ladder_arrs = set(itertools.permutations(init_perm))

        x = 0
        for ladder_arr in ladder_arrs:
            x = max(try_permutation(heights, bricks, list(ladder_arr)), x)

        return x
