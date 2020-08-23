#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
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
        if not root or not p or not q:
            return None
        path1 = []
        self.getNodePath(root, p, path1)
        path2 = []
        self.getNodePath(root, q, path2)
        i = 0
        j = 0
        lastCommonNode = None
        while i < len(path1) and j < len(path2) and path1[i] == path2[j]:
            lastCommonNode = path1[i]
            i += 1
            j += 1
        return lastCommonNode

    def getNodePath(self, root, node, path):
        if not root:
            return False
        path.append(root)
        if root == node:
            return True
        elif self.getNodePath(root.left, node, path):
            return True
        elif self.getNodePath(root.right, node, path):
            return True
        path.pop()
        return False
        
        

        
# @lc code=end

