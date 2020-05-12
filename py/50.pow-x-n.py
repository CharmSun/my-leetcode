#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start

## 1、判断正负
## 2、将n看做二进制进行计算，pow(x, 0b11) = pow(x, 0b10) * pow(x, 0b1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n > 0:
            if n & 1 == 1:
                res *= x
            x *= x
            n = n >> 1
        return round(res, 5)

x = 2.00000
n = -2
print(Solution().myPow(x, n))

# @lc code=end

