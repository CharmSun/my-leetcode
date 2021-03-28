#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    ## 等价于 求范围内所有数据的二进制字符串的公共前缀
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right = right & (right-1)
        return right

    def rangeBitwiseAnd1(self, m: int, n: int) -> int:
        num = 0
        while m != n:
            m >>= 1
            n >>= 1
            num += 1
        return m << num
        
# @lc code=end

