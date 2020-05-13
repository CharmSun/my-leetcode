#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from typing import List

## 按上，右，下，左的顺序依次读取
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        top = left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        res = []
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            for j in range(top, bottom + 1):
                res.append(matrix[j][right])
            right -= 1
            if left > right:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break
            for j in range(bottom, top - 1, -1):
                res.append(matrix[j][left])
            left += 1
            if left > right:
                break
        return res

input = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(Solution().spiralOrder(input))
        
# @lc code=end

