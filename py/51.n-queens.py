#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from typing import List

## 回溯：对每一行，每个有效可填的位置，填'Q', 直到走完所有行，结果加入结果集，回溯回来，继续下一个试探
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queen = [['.'] * n for i in range(n)]
        def queen2Str(queen):
            l = []
            for row in queen:
                l.append(''.join(row))
            return l

        def isValid(queen, row, col):
            for i in range(row):
                for j in range(n):
                    if queen[i][j] == 'Q' and ( j == col or abs(i - row) == abs(j - col)):
                        return False
            return True

        def backtrack(queen, row):
            if row == n:
                res.append(queen2Str(queen))
                return
            for col in range(n):
                if isValid(queen, row, col):
                    queen[row][col] = 'Q'
                    backtrack(queen, row + 1)
                    queen[row][col] = '.'
        backtrack(queen, 0)
        return res

input = 4
print(Solution().solveNQueens(4)) 
        
# @lc code=end

