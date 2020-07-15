#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode()
        p = head
        while p:
            cur = p
            p = p.next
            q = dummy
            while q.next and q.next.val < cur.val:
                q = q.next
            cur.next = q.next
            q.next = cur
        return dummy.next


        
# @lc code=end

