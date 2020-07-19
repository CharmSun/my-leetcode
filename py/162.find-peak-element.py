#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
from typing import List

## 二分查找，注意边界
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1]:
                r = mid 
            else:
                l = mid + 1
        return l

input = [1,2,1,3,5,6,4]
print(Solution().findPeakElement(input))       
# @lc code=end

