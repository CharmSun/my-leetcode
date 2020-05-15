#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## 1、求节点总数n，k = k % n
## 2、双指针移动，间隔k
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        p, n = head, 0
        while p != None:
            n += 1
            p = p.next
        k = k % n       
        r = l = head
        i = 0
        while r.next != None:
            r = r.next
            i += 1
            if i > k:
                l = l.next
        r.next = head
        res = l.next
        l.next = None
        return res
        
# @lc code=end

