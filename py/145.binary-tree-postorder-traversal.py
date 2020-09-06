#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## 算法：将前序遍历“根左右”变换为“根右左”，倒过来就是后序遍历“左右根”。
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        p = root
        stack1 = []
        stack2 = []
        while p or stack1:
            if p:
                stack2.append(p.val)
                stack1.append(p)
                p = p.right
            else:
                node = stack1.pop()
                p = node.left
        stack2.reverse()
        return stack2
        
# @lc code=end

