#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## 加个dummy节点，开始判断重复的节点
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next != None:
            q = p.next
            while q.next != None and q.val == q.next.val:
                q = q.next
            if p.next != q:
                p.next = q.next
            else:
                p = q
        return dummy.next
        
# @lc code=end

