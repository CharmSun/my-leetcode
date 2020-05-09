#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## 1.先解决倒转K个节点的链表
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head
        def reverseK(head: ListNode, k: int):
            dummy = ListNode(0)
            p = head
            i = 0
            while p and i < k:
                tmp = p.next
                p.next = dummy.next
                dummy.next = p
                p = tmp
                i += 1
            return dummy.next
        i = 0
        ret = first = p = head
        last = None
        while p:
            i += 1
            tmp = p.next
            if i % k == 1:
                first = p
                if last:
                    last.next = p
            if i % k == 0:
                reverseK(first, k)
                if i == k:
                    ret = p
                if last:
                    last.next = p
                last = first
            p = tmp
        return ret

        
# @lc code=end

