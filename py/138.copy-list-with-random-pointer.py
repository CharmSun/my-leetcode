#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
## 1、在每个节点后创建一个该节点的复制
## 2、设置复制节点的random
## 3、将链表分成两个
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        l1 = head
        while l1:
            l2 = Node(l1.val)
            l2.next = l1.next
            l1.next = l2
            l1 = l2.next
        l1 = head
        while l1:
            if l1.random != None:
                l1.next.random = l1.random.next
            l1 = l1.next.next
        l1 = head
        newHead = head.next
        while l1:
            l2 = l1.next
            l1.next = l2.next
            if l2.next:
                l2.next = l2.next.next
            l1 = l1.next
        return newHead
        
# @lc code=end

