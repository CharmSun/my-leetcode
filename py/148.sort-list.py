#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## 归并排序
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(right)
        return self.mergeList(l1, l2)

    def mergeList(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        r = dummy
        p = l1
        q = l2
        while p and q:
            if p.val <= q.val:
                r.next = p
                p = p.next
            else:
                r.next = q
                q = q.next
            r = r.next
        if p:
            r.next = p
        elif q:
            r.next = q
        return dummy.next
    
## 快速排序    
class Solution1:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        self.quick_sort(head, None)
        return head

    def quick_sort(self, head: ListNode, end: ListNode):
        if head != end:
            node = self.partition(head, end)
            self.quick_sort(head, node)
            self.quick_sort(node.next, end)

    def partition(self, head: ListNode, end: ListNode) -> ListNode:
        # p2是遍历指针，p1是小数的指针
        p1 = head
        p2 = head.next
        while p2 != end:
            if p2.val < head.val:
                p1 = p1.next

                tmp = p2.val
                p2.val = p1.val
                p1.val = tmp
            p2 = p2.next
        
        tmp = head.val
        head.val = p1.val
        p1.val = tmp

        return p1
        
# @lc code=end

