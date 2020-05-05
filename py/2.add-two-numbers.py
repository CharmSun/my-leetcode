#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## 链接移动，注意边界
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        carry = 0
        rLink = p = None
        while (node1 != None or node2 != None):
            v1 = v2 = 0
            if node1 != None:
                v1 = node1.val
            if node2 != None:
                v2 = node2.val
            r = v1 + v2 + carry
            carry = r // 10
            if rLink == None:
                p = rLink = ListNode(r % 10) 
            else :
                p.next = ListNode(r % 10)
                p = p.next
            
            if node1 != None:
                node1 = node1.next
            if node2 != None:
                node2 = node2.next
        if carry != 0:
            p.next = ListNode(carry)
        return rLink

        
# @lc code=end

