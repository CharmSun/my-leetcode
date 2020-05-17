#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
from typing import List

## 利用上一题的算法，height对应每行1的高度
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        height = [0] * (n+1)
        for i in range(m):
            stack = []
            for j in range(n+1):
                if j < n:
                    height[j] = height[j] + 1 if matrix[i][j] == '1' else 0
                while stack and height[stack[-1]] >= height[j]:
                    cur = stack.pop()
                    length = j - stack[-1] - 1 if stack else j
                    res = max(res, height[cur] * length)
                stack.append(j)
        return res 

input = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
print(Solution().maximalRectangle(input)) 
        
# @lc code=end

