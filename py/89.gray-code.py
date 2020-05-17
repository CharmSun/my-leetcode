#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
from typing import List

## 这题没意思，最简单的方式是使用格雷码转换公式，如下：
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(pow(2, n)):
            res.append((i >> 1) ^ i)
        return res

print(Solution().grayCode(2))

# @lc code=end

