#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## dfs
class Solution:
    def __init__(self):
        self.sum = 0

    def sumNumbers(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.sum

    def dfs(self, root, cur):
        if not root:
            return
        cur = cur * 10 + root.val
        if not root.left and not root.right:
            self.sum += cur
        self.dfs(root.left, cur)
        self.dfs(root.right, cur)
        
# @lc code=end

