#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

## 要求用O(1)的空间复杂度
## 用两个指针start和cur，其中start标记每一层的起始节点，cur用来遍历该层的节点，设计思路之巧妙，不得不服。
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        start = root
        cur = None
        while start.left:
            cur = start
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            start = start.left
        return root
        
# @lc code=end

