#########################################################################################################################################################
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
#
#
#
# Example 1:
#
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
#
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
#
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
#
#
# Constraints:
#
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100
#########################################################################################################################################################
import heapq
from collections import defaultdict, deque
from typing import List


class Solution:

    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        # The solutions was stack, but also to be smart and consider that we can remove all temps that are below the current
        # from the end of the stack. As when we check it, only the most recent higher temperature is important
        # I think I would still do it reversed if I could
        results = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                results[index] = i - index
            stack.append(i)
        return results

    def daily_temperatures_not_so_slow(self, temperatures: List[int]) -> List[int]:
        # Still slow, but not TOO slow
        # There must be a way to ot have to rebuild the sorted_last_temps everytime
        last_temps = {}
        for i in range(len(temperatures) - 1, -1, -1):
            temp, temperatures[i] = temperatures[i], 0
            sorted_last_temps = [i for i in last_temps.items()]
            sorted_last_temps.sort(key=lambda x: x[1])

            for e in sorted_last_temps:
                if e[0] > temp:
                    temperatures[i] = e[1] - i
                    break

            last_temps[temp] = i

        return temperatures

    def slow_daily_temperatures(self, temperatures: List[int]) -> List[int]:
        # This one works but is too slow for big lists
        # So need to find the trick
        r = []

        for i, e in enumerate(temperatures):
            r.append(check_temps(e, temperatures[i + 1 :]) + 1)

        return r


def check_temps(temperature: int, others: List[int]) -> int:
    for j, e2 in enumerate(others):
        if e2 > temperature:
            return j
    return -1
