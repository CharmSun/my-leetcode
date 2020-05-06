#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
from typing import List

## 与上一题思路类似，先排序然后双指针移动
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return None
        res = nums[0] + nums[1] + nums[2]
        ab = abs(res - target)
        nums.sort()
        k = 0
        while k < len(nums) - 2:
            i = k + 1
            j = len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if abs(s - target) < ab:
                    ab = abs(s - target)
                    res = s
                if s < target:
                    i += 1
                elif s > target:
                    j -= 1
                else:
                    return target
            k += 1
            while k < len(nums) - 2 and nums[k] == nums[k-1]:
                k += 1
        return res
        
# @lc code=end

