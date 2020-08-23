#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        low = min(p.val, q.val)
        high = max(p.val, q.val)
        if root.val <= high and root.val >= low:
            return root
        elif root.val > high:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < low:
            return self.lowestCommonAncestor(root.right, p, q)

# @lc code=end

