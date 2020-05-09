#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l2:
            return l1
        if not l1:
            return l2
        p = l1
        q = l2
        dummy= k = ListNode(0)
        while p and q:
            if p.val <= q.val:
                k.next = p
                p = p.next
            else:
                k.next = q
                q = q.next
            k = k.next
        if p != None:
            k.next = p
        if q != None:
            k.next = q
        return dummy.next
        
# @lc code=end

