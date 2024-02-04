#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
from typing import List

## 对所有数的每一bit位，求和，然后对3求余就是只出现1次的数在当前位的值（0或1）。
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            temp = 0
            bit = 1 << i
            for num in nums:
                if num & bit != 0:
                    temp += 1
            if temp % 3 != 0:
                res |= bit

        return res - 2**32 if res > 2**31-1 else res

print(Solution().singleNumber([-1, -1, -1, -3]))        
# @lc code=end

