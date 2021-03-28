#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 按后序递归
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        left_child = self.invertTree(root.left)
        right_child = self.invertTree(root.right)
        root.left = right_child
        root.right = left_child
        return root
        
# @lc code=end

