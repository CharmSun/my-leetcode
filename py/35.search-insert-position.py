#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List

## 二分查找： 取左值
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left
        
# @lc code=end

