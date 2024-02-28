class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum =  int(a,2) + int(b,2)
        return bin(sum) [2:]

"""
Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

"""