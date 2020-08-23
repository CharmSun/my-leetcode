#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## 递归构建
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[0:i], postorder[0:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])

        return root
        
# @lc code=end

