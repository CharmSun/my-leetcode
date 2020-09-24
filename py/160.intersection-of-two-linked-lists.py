#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## 精妙解法，pa, pb指向两个链表，不等时分别向后移动，
## pa为空时转向B链表，pb为空时转向A链表，直到相遇，或者均为null
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            if pa is None:
                pa = headB
                continue
            if pb is None:
                pb = headA
                continue
            pa = pa.next
            pb = pb.next
        return pa
        
# @lc code=end

