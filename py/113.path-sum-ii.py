#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.dfs(root, sum, 0, [], res)
        return res

    def dfs(self, node, sum, val, path, res):
        if not node:
            return
        val += node.val
        if not node.left and not node.right:
            if val == sum:
                res.append(path + [node.val])
            return
        self.dfs(node.left, sum, val, path + [node.val] , res)
        self.dfs(node.right, sum, val, path + [node.val] , res)
        
# @lc code=end

