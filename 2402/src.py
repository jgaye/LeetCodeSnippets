#########################################################################################################################################################
# You are given an integer n. There are n rooms numbered from 0 to n - 1.
#
# You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.
#
# Meetings are allocated to rooms in the following manner:
#
# Each meeting will take place in the unused room with the lowest number.
# If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
# When a room becomes unused, meetings that have an earlier original start time should be given the room.
# Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.
#
# A half-closed interval [a, b) is the interval between a and b including a and not including b.
#
#
#
# Example 1:
#
# Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
# Output: 0
# Explanation:
# - At time 0, both rooms are not being used. The first meeting starts in room 0.
# - At time 1, only room 1 is not being used. The second meeting starts in room 1.
# - At time 2, both rooms are being used. The third meeting is delayed.
# - At time 3, both rooms are being used. The fourth meeting is delayed.
# - At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
# - At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
# Both rooms 0 and 1 held 2 meetings, so we return 0.
# Example 2:
#
# Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
# Output: 1
# Explanation:
# - At time 1, all three rooms are not being used. The first meeting starts in room 0.
# - At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
# - At time 3, only room 2 is not being used. The third meeting starts in room 2.
# - At time 4, all three rooms are being used. The fourth meeting is delayed.
# - At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
# - At time 6, all three rooms are being used. The fifth meeting is delayed.
# - At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
# Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1.
#
#
# Constraints:
#
# 1 <= n <= 100
# 1 <= meetings.length <= 105
# meetings[i].length == 2
# 0 <= starti < endi <= 5 * 105
# All the values of starti are unique.
#########################################################################################################################################################
import heapq
from heapq import heapify
from typing import List
from collections import defaultdict, Counter


class Solution:
    def most_booked(self, n: int, meetings: List[List[int]]) -> int:
        """
        First heap usage and first hard problem \o/

        Runtime 1156 ms
        Beats 88.42 % of users with Python3
        Memory 62.40 MB
        Beats 82.95 % of users with Python3
        """

        # edge: only one meeting room
        # or only one meeting
        if n == 1 or len(meetings) == 1:
            return 0

        # We need the meetings to be a file of time, duration
        # choosing the right data structure to put meetings in empty slots is important
        # Let's try with a heap
        free_rooms = list(range(0, n))
        heapify(free_rooms)
        nb_meetings = [0] * n

        mts = []
        heapify(mts)

        meetings.sort(key=lambda e: e[0])

        for meeting in meetings:
            # free the rooms that would end BEFORE this meeting starts
            while mts and mts[0][0] <= meeting[0]:
                meeting_room = heapq.heappop(mts)[1]
                heapq.heappush(free_rooms, meeting_room)

            try:
                # If there is an empty room, assign the meeting to it
                # Take the room out of the meeting room list, and put the pair in the heap of happening meetings
                meeting_room = heapq.heappop(free_rooms)
                nb_meetings[meeting_room] += 1
                heapq.heappush(mts, (meeting[1], meeting_room))
            except IndexError:
                # If no empty room, add the meeting to the next available room
                # ie the first of the meeting happening heap, by adding the time
                meeting_room = mts[0][1]
                nb_meetings[meeting_room] += 1
                heapq.heapreplace(
                    mts, (mts[0][0] + (meeting[1] - meeting[0]), meeting_room)
                )

        return nb_meetings.index(max(nb_meetings))
