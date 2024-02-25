class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

"""
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
"""