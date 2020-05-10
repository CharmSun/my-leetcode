#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List

## 每行，每列，每块进行判断
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.checkRow(board, i):
                return False
        for i in range(9):
            if not self.checkCol(board, i):
                return False
        for i in range(9):
            if not self.checkBlock(board, i):
                return False
        return True
    
    def checkRow(self, board, rowIndex):
        vals = set()
        for i in range(9):
            if board[rowIndex][i] != '.':
                if board[rowIndex][i] in vals:
                    return False
                else:
                    vals.add(board[rowIndex][i])
        return True

    def checkCol(self, board, colIndex):
        vals = set()
        for i in range(9):
            if board[i][colIndex] != '.':
                if board[i][colIndex] in vals:
                    return False
                else:
                    vals.add(board[i][colIndex])
        return True

    def checkBlock(self, board, index):
        rowNum = (index // 3) * 3
        colNum = (index % 3) * 3
        vals = set()
        for i in range(3):
            for j in range(3):
                if board[rowNum+i][colNum+j] != '.':
                    if board[rowNum+i][colNum+j] in vals:
                        return False
                    else:
                        vals.add(board[rowNum+i][colNum+j])
        return True
        
# @lc code=end

