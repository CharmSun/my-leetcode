#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
from typing import List

## 从四边开始dfs 寻找，为'O'则记录为'-', 则剩下的'0' 为被包围的
# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return None
        row = len(board)
        col = len(board[0])
        for i in range(0, row):
            self.dfs(board, i, 0)
            self.dfs(board, i, col - 1)
        for j in range(0, col):
            self.dfs(board, 0, j)
            self.dfs(board, row - 1, j)
        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '-':
                    board[i][j] = 'O'


    def dfs(self, board, i, j) -> None:
        row = len(board)
        col = len(board[0])
        if i < 0 or i >= row or j < 0 or j >= col or board[i][j] != 'O':
            return None
        board[i][j] = '-'
        self.dfs(board, i-1, j)
        self.dfs(board, i+1, j)
        self.dfs(board, i, j+1)
        self.dfs(board, i, j-1)

input=[
    ['X','X','X','X'],
    ['X','O','O','X'],
    ['X','X','O','X'],
    ['X','O','X','X'],
]
Solution().solve(input)
print(input)
        
# @lc code=end

