#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## 这种建树问题一般来说都是用递归来解，这道题也不例外，划分左右子树，递归构造。
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.getTrees(1, n)
    
    def getTrees(self, start:int, end:int) -> List[TreeNode]:
        res = []
        ## 注意边界
        if start > end:
            res.append(None)
        else:
            for i in range(start, end+1):
                leftTrees = self.getTrees(start, i-1)
                rightTrees = self.getTrees(i+1, end)
                for l in leftTrees:
                    for r in rightTrees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
        return res
        
# @lc code=end

