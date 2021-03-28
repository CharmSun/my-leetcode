#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List

class Solution:
    ## left ,right 分别记录i左右的元素乘积
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return None
        left, right = 1, 1
        res = [1] * n
        for i in range(0, n):
            res[i] *= left
            left *= nums[i]

            res[n-1-i] *= right
            right *= nums[n-1-i]
        return res

        
# @lc code=end

