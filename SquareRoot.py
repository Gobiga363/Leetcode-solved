class Solution:
    def mySqrt(self, x: int) -> int:
        number=1
        while number * number <= x:
            number+=1
        return number - 1

"""
Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
"""