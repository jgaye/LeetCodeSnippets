#########################################################################################################################################################
# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
#
# A string is palindromic if it reads the same forward and backward.
#
#
#
# Example 1:
#
# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.
# Example 2:
#
# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".
# Example 3:
#
# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.
#
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists only of lowercase English letters.
#########################################################################################################################################################
from math import floor
from typing import List


class Solution:
    def first_palindrome(self, words: List[str]) -> str:
        """
        Compare word to its reversed
        Complexity: reversed is O(nb_chars), and we go through the list once at worst so O(nm)

        Runtime 93ms
        Beats 23.14% of users with Python3
        Memory 16.74MB
        Beats 59.17% of users with Python3
        """
        for word in words:
            if "".join(reversed(word)) == word:
                return word
        return ""

    def first_palindrome_faster(self, words: List[str]) -> str:
        """
        Compare char at beginning to the end for half the word

        It's actually slower...
        Runtime 103ms
        Beats 16% of users with Python3
        Memory 16.83MB
        Beats 51% of users with Python3
        """
        for word in words:
            i = 0
            while i < floor(len(word) / 2) and word[i] == word[-1 - i]:
                i += 1
            if i == floor(len(word) / 2):
                return word
        return ""

    set().difference()
