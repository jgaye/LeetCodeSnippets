#########################################################################################################################################################
# Given an array of characters chars, compress it using the following algorithm:
#
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
#
# After you are done modifying the input array, return the new length of the array.
#
# You must write an algorithm that uses only constant extra space.
#
#
#
# Example 1:
#
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# Example 2:
#
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.
# Example 3:
#
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
#
#
# Constraints:
#
# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
#########################################################################################################################################################
from typing import List
from collections import defaultdict, Counter


class Solution:

    def compress(self, chars: List[str]) -> (int, List[str]):
        """
        Enumerate through the array.
        For each new char detected, count the similar ones in a while loop (includes all conditions to break)
        Replace char elements with the count

        Runtime 55 ms
        Beats 82.03 % of users with Python3
        Memory 16.74 MB
        Beats 66.94 % of users with Python3
        """
        i = 0
        while i < len(chars):
            j = i
            cnt = 1
            while j + 1 < len(chars) and chars[j + 1] == chars[i]:
                cnt += 1
                j += 1
            if cnt > 1:
                chars[i + 1 : j + 1] = list(str(cnt))
                i += len(list(str(cnt))) + 1
            else:
                i += 1

        return len(chars), chars
