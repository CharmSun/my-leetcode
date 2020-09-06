#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## 1. fast速度2，slow速度1，直到第一次相遇
## 2. slow回到起点，fast不动
## 3. fast和slow速度1运动，再次相遇时的位置一定是成环的位置
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                slow = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
        
# @lc code=end

