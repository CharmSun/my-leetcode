#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        MIN = -2 ** 31
        num = abs(x)
        if num % 10 == 0:
            num = num // 10
        revertedNum = 0
        while num > 0:
            revertedNum = revertedNum * 10 + num % 10
            num = num // 10
        if x < 0:
            revertedNum = -revertedNum
        if (revertedNum > MAX) or (revertedNum < MIN):
            return 0
        return revertedNum
        
# @lc code=end

