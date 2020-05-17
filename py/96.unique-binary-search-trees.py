#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start

## DP: 左右子树种类的乘积
## for j in [0, i-1], dp[i] += dp[j] * dp[i-1-j]
class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] = dp[i] + dp[j] * dp[i-1-j]
        return dp[n]

print(Solution().numTrees(3))
        
# @lc code=end

