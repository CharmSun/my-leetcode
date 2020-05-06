#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
from typing import List

## 排序，化成3Sum, 双指针移动，注意去重
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        l = len(nums)
        nums.sort()
        for i in range(l):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, l):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j+1
                right = l-1
                twoSum = target - nums[i] - nums[j]
                while left < right:
                    if nums[left] + nums[right] == twoSum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif nums[left] + nums[right] < twoSum:
                        left += 1
                    else:
                        right -= 1
        return res
        
# @lc code=end

