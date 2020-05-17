#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        i = 0
        dummy = ListNode(0)
        ## 头部加一个哑结点，方便操作
        dummy.next = head
        l = r = p = dummy
        ## sub用来连接反转的子链表
        sub = ListNode(0)
        while p != None and i <=n :
            if i == m - 1:
                ## l,r分别指向要断开的两端
                l = p
                r = p.next
            ## 先把p移到下一个，处理当前这个，链到sub
            tmp = p
            p = p.next
            if i >= m and i <= n:
                tmp.next = sub.next
                sub.next = tmp
            i += 1
        ## 循环结束，将sub连接回去
        l.next = sub.next
        r.next = p
        return dummy.next
        
# @lc code=end

