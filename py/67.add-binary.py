#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start

## 倒着按位相加吧
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ''
        i, j= len(a) - 1, len(b) - 1
        while i > -1 and j > -1:
            s = int(a[i]) + int(b[j]) + carry
            res = str(s % 2) + res
            carry = s // 2
            i -= 1
            j -= 1
        while i > -1:
            s = int(a[i]) + carry
            res = str(s % 2) + res
            carry = s // 2
            i -= 1
        while j > -1:
            s = int(b[j]) + carry
            res = str(s % 2) + res
            carry = s // 2
            j -= 1
        if carry > 0:
            res = str(carry) + res
        return res

a = "100"
b = "110010"
print(Solution().addBinary(a, b))        
# @lc code=end

