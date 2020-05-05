#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start

## 倒转一半进行比较
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or (x % 10 == 0 and x != 0):
            return False
        revertedNum = 0
        while x > revertedNum:
            revertedNum = revertedNum * 10 + x % 10
            x = x // 10
        return (x == revertedNum) or (revertedNum // 10 == x)
        
# @lc code=end

