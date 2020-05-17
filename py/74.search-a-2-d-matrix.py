#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List

## 1、先判断是否在矩阵范围内
## 2、确定所在行
## 3、在所在行内使用二分查找
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        row = m - 1
        for i in range(1, m):
            if target < matrix[i][0]:
                row = i - 1
                break
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
print(Solution().searchMatrix(matrix, target))
        
# @lc code=end

