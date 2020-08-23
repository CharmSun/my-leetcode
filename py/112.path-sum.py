#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        return self.dfs(root, sum, 0)

    def dfs(self, node, sum, val):
        val += node.val
        if not node.left and not node.right:
            return val == sum
        if node.left and self.dfs(node.left, sum, val):
            return True
        if node.right and self.dfs(node.right, sum, val):
            return True
        return False
        
# @lc code=end

