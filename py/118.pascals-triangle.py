#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
from typing import List

## 根据上一层计算
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows <= 0:
            return res
        res.append([1])
        for i in range(1, numRows):
            tmp = []
            tmp.append(1)
            for j in range(0, len(res[i-1]) - 1):
                tmp.append(res[i-1][j] + res[i-1][j+1])
            tmp.append(1)
            res.append(tmp)
        return res
        
# @lc code=end

