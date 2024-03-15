# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node, depth, ans) -> int:
            if not node:
                return ans
            if not node.left and not node.right:
                return min(ans, depth)
            leftDepth = dfs(node.left, depth + 1, ans)
            rightDepth = dfs(node.right, depth + 1, ans)
            return min(leftDepth, rightDepth)
        return dfs(root, 1, 10**6)


"""
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""