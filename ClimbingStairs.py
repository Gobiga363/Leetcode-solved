class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one

"""
Example 1:
Input: n = 2
Output: 2

Example 2:
Input: n = 3
Output: 3
"""