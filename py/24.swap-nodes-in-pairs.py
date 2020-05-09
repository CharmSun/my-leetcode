#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## 链接节点交换，通过画图辅助
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        p2 = dummy.next
        while p2 and p2.next:
            tmp = p2.next.next
            p1.next = p2.next
            p2.next.next = p2
            p2.next = tmp
            p1 = p2
            p2 = tmp
        return dummy.next
        
# @lc code=end

