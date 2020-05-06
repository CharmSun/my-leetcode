#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List

## 1. 先排序
## 2. 双指针前后向中间移动，注意去重
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        k = 0
        while k < len(nums) - 2:
            target = 0 - nums[k]
            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] == target:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
            k += 1
            while k < len(nums) - 2 and nums[k] == nums[k-1]:
                k += 1
        return res
        
# @lc code=end

