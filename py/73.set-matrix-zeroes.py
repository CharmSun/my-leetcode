#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
from typing import List

## 1、先计算第0行，第0列是否该置0
## 2、遍历每个数，将为0的值，投影到对应的第0行，第0列
## 3、根据第0行和第0列的0的值，取更新其他行列
## 4、最后，处理第0行第0列，是否置为0
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return None
        m = len(matrix)
        n = len(matrix[0])
        zeroRow = zeroCol = False
        for j in range(n):
            if matrix[0][j] == 0:
                zeroRow = True
        for i in range(m):
            if matrix[i][0] == 0:
                zeroCol = True
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if zeroRow:
            for j in range(n):
                matrix[0][j] = 0
        if zeroCol:
            for i in range(m):
                matrix[i][0] = 0

input = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Solution().setZeroes(input)
print(input)
# @lc code=end

