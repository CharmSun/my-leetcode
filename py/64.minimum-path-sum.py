#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
from typing import List

## 与前两题类似，变成求和
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for i in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif j > 0 and j > 0:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        return dp[n-1][m-1]

input = [
  [1]
]
print(Solution().minPathSum(input))

# @lc code=end

