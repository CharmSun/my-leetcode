#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
from typing import List

class Solution:
    # 双指针移动
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        right = -1
        sum = 0
        length = len(nums) + 1
        while left < len(nums) and right < len(nums):
            if right < len(nums) - 1 and sum < target:
                right += 1
                sum += nums[right]
            else:
                sum -= nums[left]
                left += 1
            if sum >= target:
                length = min(length, right - left + 1)
        if length == len(nums) + 1:
            return 0
        return length
        
# @lc code=end

