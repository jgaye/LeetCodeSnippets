#########################################################################################################################################################
# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
#
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
#
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
#
#
#
# Example 1:
#
# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
# Example 2:
#
# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
# Example 3:
#
# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
#
#
# Constraints:
#
# 1 <= points.length <= 105
# points[i].length == 2
# -231 <= xstart < xend <= 231 - 1
#########################################################################################################################################################
from typing import List
import heapq


class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        First we by the end value, then
        Take example:
          3  4
         2    5
          3    6
                7 8
        You want to shoot your arrow for the first 3 when there is overlap
        What we do is that we do not shoot while our current ballons overlap with all the previous ones
        = the start of current is before or equals to the end of the smallest end considered
        As soon as we are out of the interval, we shoot, and the currently considered ballon becomes the one with the lowest end

        Runtime 971 ms
        Beats 98.88 % of users with Python3
        Memory 62.78 MB
        Beats 72.76 % of users with Python3
        """
        min_end, cnt = float("-inf"), 0
        for s, e in sorted(
            points, key=lambda x: x[1]
        ):  # not that using 2 variables unpack the value
            if s <= min_end:
                pass
            else:
                cnt += 1
                min_end = e
        return cnt
