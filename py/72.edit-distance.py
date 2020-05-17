#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start

## DP: dp[i][j] 代表word1的长度i, word2的长度j
## word1[i] == word2[j] 时，dp[i+1][j+1] = dp[i][j]
## 不等时，add, delete, replace三种操作中找出最小的，加上1
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
        return dp[m][n]

word1 = "intention"
word2 = "execution"
print(Solution().minDistance(word1, word2))
        
# @lc code=end

