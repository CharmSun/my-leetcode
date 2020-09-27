#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start

## 要看5有多少个，在25的时候，会有两个零，以此类推，对于5**n都要做处理
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res, k = 0, 5
        while k <= n:
            res += n//k
            k *= 5
        return res

print(Solution().trailingZeroes(30))
# @lc code=end

