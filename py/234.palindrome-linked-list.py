#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ## 快慢指针找中间节点
    ## 反转后半段
    ## 比较
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l1 = head
        l2 = self.reverse(slow)
        return self.compare(l1, l2)
    
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        return prev
    
    def compare(self, l1: ListNode, l2: ListNode) -> bool:
        while l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True

        
# @lc code=end

