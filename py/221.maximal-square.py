#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
from typing import List

class Solution:
    # 用 dp(i,j) 表示以 (i,j) 为右下角，且只包含 1 的正方形的边长最大值。
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        maxLen = 0
        dp = [[0] * (cols+1) for i in range(rows+1)]
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxLen = max(maxLen, dp[i][j])
        return maxLen ** 2
        
# @lc code=end

