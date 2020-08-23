#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
from typing import List

## 层层递推，old为上一层当前位置旧值
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [0] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            old = res[0] = 1
            for j in range(1, i + 1):
                tmp = res[j]
                res[j] = old + res[j]
                old = tmp
        return res

# @lc code=end

