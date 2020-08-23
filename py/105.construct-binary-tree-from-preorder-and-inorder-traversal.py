#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## 递归
## 从前序中取第一个做root, 在中序中找到该root 的位置，递归构建左右子树
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+i], inorder[0:i])
        root.right = self.buildTree(preorder[1+i:], inorder[i+1:])

        return root
        
# @lc code=end

