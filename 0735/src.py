#########################################################################################################################################################
# We are given an array asteroids of integers representing asteroids in a row.
#
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
#
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
#
#
#
# Example 1:
#
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:
#
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:
#
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
#
#
# Constraints:
#
# 2 <= asteroids.length <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0
#########################################################################################################################################################
from typing import List
from collections import deque


class Solution:

    def asteroid_collision(self, asteroids: List[int]) -> List[int]:
        """
        It's a LIFO stack solution.
        For each asteroid, check if it should go in the stack, or destroy the last element of the stack.

        Runtime 84 ms
        Beats 57.13 % of users with Python3
        Memory 17.97 MB
        Beats 58.93 % of users with Python3
        """
        stack = deque()
        stack.append(asteroids.pop(0))

        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
                continue

            # not the same direction if product is negative
            # handling the case where it IS the same direction
            if stack[-1] * asteroid > 0:
                stack.append(asteroid)
                continue

            # crash only if the last stack goes right, and this asteroid goes left
            # let's handle the other case first
            if stack[-1] < 0:
                stack.append(asteroid)
                continue

            # we get to the meat of it, need to handle collisions
            handle_collision(stack, asteroid)

        return list(stack)


def handle_collision(stack: deque[int], ast: int) -> None:
    # If we destroyed all the stack or both the ast go left
    if not stack or (stack[-1] < 0 and ast < 0):
        stack.append(ast)
        return

    # if both ast are the same size
    if abs(ast) == abs(stack[-1]):
        # the stack ast is destroyed, we end the recursion
        stack.pop()
        return

    # if the stack asteroid is bigger
    if abs(ast) < abs(stack[-1]):
        # we leave the stack as is and end the recursion
        return

    # if the collision ast is bigger
    if abs(ast) > abs(stack[-1]):
        # we destroy the stack ast and go to the next recursion
        stack.pop()
        return handle_collision(stack, ast)
