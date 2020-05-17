#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Morris遍历： 
## 线索二叉树：利用叶子节点中的左右空指针指向某种顺序遍历下的前驱节点或后继节点
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        pre = None
        first = second = past = None
        while cur:
            if not cur.left:
                if past and past.val > cur.val:
                    if not first:
                        first = past
                    second = cur
                past =cur
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    if past.val > cur.val:
                        if not first:
                            first = past
                        second = cur
                    past = cur
                    cur = cur.right
        if first and second:
            tmp = first.val
            first.val = second.val
            second.val = tmp
        
# @lc code=end

