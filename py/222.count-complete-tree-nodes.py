#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        pLeft = root
        hLeft = 0
        while pLeft:
            hLeft += 1
            pLeft = pLeft.left
        pRight = root
        hRight = 0
        while pRight:
            hRight += 1
            pRight = pRight.right
        if hLeft == hRight:
            return (1 << hLeft) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
        

# @lc code=end

