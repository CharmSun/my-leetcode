#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
from typing import List

## (di，dj)表示运行向量，左：(0,1), 下(1,0)，右(0,-1)，上(-1,0)，遇到有值时就变换方向
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(1, n**2 + 1):
            res[i][j] = k  
            if res[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
            
        return res

print(Solution().generateMatrix(4))
        
# @lc code=end

