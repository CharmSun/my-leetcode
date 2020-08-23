#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = []
        queue.append(root)
        while queue:
            level = len(res)  ## 当前第几层
            levelVals = []    ## 当前层的值
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if level % 2 == 0:
                    levelVals.append(node.val)
                else:
                    levelVals.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(levelVals)
        return res

# @lc code=end

