#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p != None:
            if p.next != None and p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
        
# @lc code=end

