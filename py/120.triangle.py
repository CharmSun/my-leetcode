#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
from typing import List

## 复制了三角形最后一行，作为用来更新的一维数组。
# 然后逐个遍历这个DP数组，对于每个数字，和它之后的元素比较选择较小的再加上上面一行相邻位置的元素做为新的元素，
# 然后一层一层的向上扫描

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        dp = triangle[-1].copy()
        n = len(triangle)
        for i in range(n-2, -1, -1):
            for j in range(0, i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(Solution().minimumTotal(triangle))   

# @lc code=end

