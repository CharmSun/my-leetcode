#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
from typing import List

## 思路有点像是数字电路设计一个计数器.
# 此题的情况就是为每一位二进制进行计数,计数三次归零,
# 那么最后没有归零的数就是出现一次的那个数.
# 设计思路与逻辑门电路设计一样.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            tempA = (~a & b & num) + (a & ~b & ~num)
            b = (~a & ~b & num) + (~a & b & ~num)
            a = tempA
        return b
        
# @lc code=end

