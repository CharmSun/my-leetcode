#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
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

## 建立一个dummy结点来指向每层的首结点的前一个结点，然后指针t用来遍历这一层，
## 我们实际上是遍历一层，然后连下一层的next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dummy = Node(0)
        t = dummy
        p = root
        while p:
            if p.left:
                t.next = p.left
                t = t.next
            if p.right:
                t.next = p.right
                t = t.next
            p = p.next
            if not p:
                p = dummy.next
                dummy.next = None
                t = dummy
        return root
        
# @lc code=end

