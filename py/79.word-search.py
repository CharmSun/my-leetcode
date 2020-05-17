#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False

    def dfs(self, board, i, j, word, charIdx):
        # 边界条件，不满足即跳出
        # 如果当前元素不是我们想要的元素，即跳出
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[charIdx] != board[i][j]:
            return False
        # 字符串word中所有元素都被查找到，说明已经找到了，返回true
        if charIdx == len(word) - 1:
            return True
        tmp = board[i][j]
        # 将当前位置的值设置成#，避免查找到之前走过的路径
        board[i][j] = '#'
        # 上下左右四个方向进行查找
        res = self.dfs(board, i+1, j, word, charIdx+1) or self.dfs(board, i-1, j, word, charIdx+1) \
            or self.dfs(board, i, j+1, word, charIdx+1) or self.dfs(board, i, j-1, word, charIdx+1)
        board[i][j] = tmp
        return res
        
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(Solution().exist(board, word))
        
# @lc code=end

