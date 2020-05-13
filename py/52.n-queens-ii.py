#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start

## 与上一题类似，求结果总数，可以只用一个数组存棋盘每行皇后的列位置
class Solution:
    def __init__(self):
        self.res = 0

    def isValid(self, queen, row):
        for i in range(row):
            if queen[i] == queen[row] or abs(row - i) == abs(queen[row] - queen[i]):
                return False
        return True

    def totalNQueens(self, n: int) -> int:
        queen = [-1] * n # 存棋盘每行皇后的列位置
        
        def backtrack(row):
            if row == n:
                self.res += 1
                return
            for col in range(n):
                queen[row] = col
                if self.isValid(queen, row):
                    backtrack(row + 1)
        backtrack(0)
        return self.res

input = 4
print(Solution().totalNQueens(input))
        
# @lc code=end

