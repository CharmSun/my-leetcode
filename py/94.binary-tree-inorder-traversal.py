#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## 二叉树中序遍历：
## 使用栈，沿着左节点入栈，为叶子节点时，退栈 -> p.val -> p = p.right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        p = root
        stack = []
        while p != None or len(stack) > 0:
            if p != None:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                result.append(p.val)
                p = p.right
        return result
        
# @lc code=end

