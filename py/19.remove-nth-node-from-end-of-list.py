#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## 注意边界情况
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None or n <= 0:
            return head
        p = q = head
        i = 1
        while q.next:
            if i > n:
                p = p.next
            q = q.next
            i += 1
        if i == n:
            head = p.next
            del p
            return head
        if i > n:
            k = p.next
            p.next = k.next
            del k
        return head
        
# @lc code=end

