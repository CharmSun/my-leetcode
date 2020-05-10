#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List

## 二分查找：找左边界和右边界
## 左边界：target <= nums[mid]: 缩小end; 使用start
## 右边界：target >= nums[mid]: 放大start; 使用end
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = right = -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        if start < len(nums) and nums[start] == target:
            left = start
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target >= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        if end > -1 and nums[end] == target:
            right = end
        return [left, right]

nums = [5,7,7,8,8,10]
print(Solution().searchRange(nums, 7)) 

# @lc code=end

