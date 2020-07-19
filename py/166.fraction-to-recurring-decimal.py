#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        res = []
        # 首先判断结果正负, 符号不同需要负号
        if (numerator > 0) != (denominator > 0):
            res.append('-')
        
        numerator, denominator = abs(numerator), abs(denominator)
        a, b = divmod(numerator, denominator)
        res.append(str(a))
        # 判读到底有没有小数
        if b == 0:
            return ''.join(res)
        res.append('.')

        # 把所有出现过的余数记录下来，对应小数的位置
        loc = {b: len(res)}
        while b:
            b *= 10
            a, b = divmod(b, denominator)
            res.append(str(a))
            # 余数前面出现过,说明开始循环了,加括号
            if b in loc:
                res.insert(loc[b], '(')
                res.append(')')
                break
            loc[b] = len(res)
        return ''.join(res)

numerator = 2
denominator = 3
print(Solution().fractionToDecimal(numerator, denominator))

# @lc code=end

