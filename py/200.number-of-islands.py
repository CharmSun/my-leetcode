#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from typing import List

## DFS的思想。
## 遍历矩阵，每遇到'1'后, 开始向四个方向DFS，搜'1'到后该位置变为’0’，因为相邻的属于一个island，然后开始继续找下一个’1’。
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    self.dfs(row, col, grid)
        return count
    
    def dfs(self, row, col, grid):
        if row < 0 or row >= len(grid) or \
        col < 0 or col >= len(grid[0]) or \
            grid[row][col] == '0':
            return
        grid[row][col] = '0'
        self.dfs(row + 1, col, grid)
        self.dfs(row - 1, col, grid)
        self.dfs(row, col + 1, grid)
        self.dfs(row, col - 1, grid)

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(Solution().numIslands(grid))

# @lc code=end

