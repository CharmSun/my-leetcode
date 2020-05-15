#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start

## 斐波那契，DP，dp[i] = dp[i-1] + dp[i-2]
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

n = 4
print(Solution().climbStairs(n))
        
# @lc code=end

