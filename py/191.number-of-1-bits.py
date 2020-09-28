#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start

## n & (n-1) 可以消掉二进制最右侧的 1
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n = n & (n-1)
        return res
        
# @lc code=end

