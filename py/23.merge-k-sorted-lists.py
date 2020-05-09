#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## 两两合并，前一半的每个链表和后面一半对应的链接合并，并放回至前一半
class Solution:
    def mergeTwo(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if l1:
            point.next = l1
        if l2 :
            point.next = l2
        return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists :
            return None
        n = len(lists)
        while n > 1 :
            k = (n + 1) // 2
            for i in range(0, n // 2):
                lists[i] = self.mergeTwo(lists[i], lists[i + k])
            n = k
        return lists[0]
        
# @lc code=end

