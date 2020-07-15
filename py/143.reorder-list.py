#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## 1、快慢指针找到中间节点
## 2、反转后半段链接
## 3、合并前后两端链表
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return None
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        p = slow.next
        slow.next = None
        dummy = ListNode()
        while p:
            cur = p
            p = p.next
            cur.next = dummy.next
            dummy.next = cur
        p = head
        q = dummy.next
        while p and q:
            tmp = q
            q = q.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next

        
        
# @lc code=end

