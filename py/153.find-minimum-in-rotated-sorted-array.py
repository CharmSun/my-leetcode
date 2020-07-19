#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List

## 二分查找：
## nums[mid] > nums[mid+1]， 返回nums[mid+1]；
## nums[mid-1] > nums[mid]，返回nums[mid]
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        if nums[right] > nums[0]:
            return nums[0]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1

input = [3,1,2] 
print(Solution().findMin(input))

        
# @lc code=end

