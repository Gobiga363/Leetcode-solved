class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=''

        for i in s:
            if i.isalnum():
                string+=i.lower()
            else:
                continue
        index_comp=(len(string)+1)//2
        for i in range(index_comp):
            if string[i]==string[len(string)-1-i]:
                continue
            else:
                return False
        return True


"""
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: s = "race a car"
Output: false

Example 3:
Input: s = " "
Output: true
"""