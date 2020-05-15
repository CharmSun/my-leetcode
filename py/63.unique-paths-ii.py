#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
from typing import List

## 从起始位置开始，标记障碍物 的值为0
## 最上面一行 dp[i][j] = dp[i][j-1] 
## 最左边一列 dp[i][j] = dp[i-1][j]
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0] * m for i in range(n)]

        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i-1][j]
                elif i > 0 and j > 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

input = [
  [0,0,1],
  [0,1,0],
  [1,0,0]
]
print(Solution().uniquePathsWithObstacles(input)) 
        
# @lc code=end

