#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        p = root
        i = 0
        while stack or p:
            while p:
                stack.append(p)
                p = p.left
            node = stack.pop()
            i += 1
            if i == k:
                return node.val
            p = node.right
        return 0
            
        

        
# @lc code=end

