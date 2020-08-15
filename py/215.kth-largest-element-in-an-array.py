#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.qSelect(nums, k, 0, len(nums) - 1)
    
    def qSelect(self, nums, k, left, right) -> int:
        pivot = nums[left]
        i, j = left, right
        while i < j:
            while i < j and nums[j] <= pivot:
                j -= 1
            while i < j and nums[i] >= pivot:
                i += 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[j] = nums[j], nums[left]
        
        which_max = j - left + 1
        if which_max == k:
            return pivot
        elif which_max < k:
            return self.qSelect(nums, k - which_max, j + 1, right)
        else:
            return self.qSelect(nums, k, left, j-1)

nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))
        
# @lc code=end

