#########################################################################################################################################################
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#
#
# Example 1:
#
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:
#
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:
#
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
#
#
# Constraints:
#
# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104
#########################################################################################################################################################
from typing import List
import heapq


class Solution:

    def erase_overlap_intervals(self, intervals: List[List[int]]) -> int:
        """
        Algo from the solutions tab
        Sort the intervals by end time and pick the smallest end time
        As long as another interval has the same end time, we remove it and count it
        (Could be done with the latest start time and going in reverse)

        Runtime 991 ms
        Beats 98.62 % of users with Python3
        Memory 55.30 MB
        Beats 51.93 % of users with Python3
        """
        end, cnt = float("-inf"), 0
        # intervals.sort(key=lambda x: x[1])
        # for e in intervals:
        for s, e in sorted(
            intervals, key=lambda x: x[1]
        ):  # not that using 2 variables unpack the value
            if s >= end:
                end = e
            else:
                cnt += 1
        return cnt

        # AFTER MULTIPLE ITERATIONS
        # My solution does not work (see tests)
        # My heuristic of removing the interval with the most overlaps ends up not working for complex examples
        # and it's too complex to figure out
        """
        Greedy, algo:
        Sort by size, remove the biggest one, check if the rest overlaps

        Runtime 55 ms
        Beats 82.03 % of users with Python3
        Memory 16.74 MB
        Beats 66.94 % of users with Python3
        """
        # fisrt, remove duplicates
        init_len = len(intervals)
        intervals = list({range(i[0], i[1]) for i in intervals})
        intervals, max_overlap = sort_by_overlaps(intervals)

        while max_overlap > 0:
            intervals.pop()
            intervals, max_overlap = sort_by_overlaps(intervals)

        return init_len - len(intervals)


def sort_by_overlaps(intervals: list[range]) -> (list[range], int):
    counted_overlaps = [count_overlaps(e, intervals) for e in intervals]
    max_overlap = max(counted_overlaps)
    intervals = list(zip(counted_overlaps, intervals))
    intervals.sort(key=lambda x: x[0])
    intervals = [x[1] for x in intervals]
    return intervals, max_overlap


def count_overlaps(interval: range, others: list[range]):
    count = 0
    for other in others:
        if not other == interval:
            count += len(set(interval).intersection(set(other)))
    return count


def check_overlap(intervals: List[List[int]]) -> bool:
    acc = set()
    for i in intervals:
        if acc.intersection(set(range(i[0], i[1]))):
            return True
        acc = acc.union(set(range(i[0], i[1])))
    return False
