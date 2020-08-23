#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## 递归：
## 先递归平整左子树，再递归平整右子树
## 连接平整后的左右子树
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        if root.left:
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)
        if root.left:
            p = root.left
            while p.right:
                p = p.right
            p.right = root.right
            root.right = root.left
            root.left = None

        
# @lc code=end

