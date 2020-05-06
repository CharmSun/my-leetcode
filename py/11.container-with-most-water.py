#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List

## two pointers
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            h = min(height[l], height[r])
            res = max(res, h * (r - l))
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return res
        
# @lc code=end

