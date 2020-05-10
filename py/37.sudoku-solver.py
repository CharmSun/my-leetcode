#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
from typing import List

## 回溯：试验每个值，判断是否有效，不行就重置为'.'，继续下一个
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.solve(board)

    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for num in range(1, 10):
                        if self.isValid(board, i, j, num):
                            board[i][j] = str(num)
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
    
    def isValid(self, board, i, j, num):
        for row in range(9):
            if board[row][j] == str(num):
                return False
        for col in range(9):
            if board[i][col] == str(num):
                return False
        top = i // 3 * 3
        left = j // 3 * 3
        for row in range(top, top+3):
            for col in range(left, left+3):
                if board[row][col] == str(num):
                    return False
        return True
        
# @lc code=end

