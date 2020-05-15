#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start

## DP:  dp[i][j] = dp[i-1][j] + dp[i][j-1]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * m for i in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

print(Solution().uniquePaths(3, 2))
        
# @lc code=end

