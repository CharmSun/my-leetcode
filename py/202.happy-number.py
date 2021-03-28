#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start

## 用cache 记录已经算过的值，在cache中说明数字开始重复，不会是happy
class Solution:
    def isHappy(self, n: int) -> bool:
        def calSquare(n):
            num = n
            sum = 0
            while num != 0:
                d = num % 10
                num = num // 10
                sum += d * d
            return sum
        cache = {}
        s = n
        while True:
            s = calSquare(s)
            if s == 1:
                return True
            if s in cache:
                return False
            else:
                cache[s] = 1
        
# @lc code=end

