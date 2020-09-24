#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
from typing import List

## 二分查找：
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # less than the r so search left
            if nums[mid] < nums[right]: 
                right = mid
            # greater than r so search right
            elif nums[mid] > nums[right]: 
                left = mid + 1
            # equals?
            else: 
                right -= 1
        return nums[left]

input = [2,2,2,0,1,2]
print(Solution().findMin(input))
        
# @lc code=end

