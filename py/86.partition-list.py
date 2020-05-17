#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## 两个dummy节点来链接
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l1 = dummy1= ListNode(0)
        l2 = dummy2= ListNode(0)
        p = head
        
        while p != None:
            if p.val < x:
                l1.next = p
                l1 = l1.next
            else:
                l2.next = p
                l2 = l2.next
            p = p.next
        
        l1.next = dummy2.next
        l2.next = None
        return dummy1.next
        
# @lc code=end

