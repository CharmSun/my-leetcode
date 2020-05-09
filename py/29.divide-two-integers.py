#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start

## 1、找到小于被除数的最大的除数的2倍数
## 2、再取余数进行循环
## 3、注意边界
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = (1 << 31) -1
        INT_MIN = -(1 << 31)
        if dividend == 0:
            return 0
        if divisor == 0:
            return INT_MIN
        dividendA = abs(dividend)
        divisorA = abs(divisor)
        quotient = 0
        while dividendA >= divisorA:
            q = 0
            maxDivisor = divisorA
            while maxDivisor < dividendA - maxDivisor:
                maxDivisor = maxDivisor << 1  
                q += 1
            quotient += 1 << q
            dividendA -= maxDivisor
        posA = dividend > 0
        posB = divisor > 0
        if posA != posB:
            quotient = -quotient
        if quotient > INT_MAX:
            return INT_MAX
        if quotient < INT_MIN:
            return INT_MIN
        return quotient
        
# @lc code=end

