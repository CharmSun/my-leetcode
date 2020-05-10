#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start

from typing import List

## 二分查找
## 先判断中间值在左一半还是右一半，再判断target 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

print(Solution().search([4,5,6,7,0,1,2], 3))
        
# @lc code=end

