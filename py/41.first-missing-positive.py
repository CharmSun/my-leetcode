#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
from typing import List

## 时间： O(n), 空间： O(1)
## 在原数组上 i 位置上放置数字 i+1
## r 代表最大有效值，不可能超过整个数组的长度，遇到非法值时，需要 r -= 1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        while l < r:
            if nums[l] == l+1:
                l += 1
            elif (nums[l] < l+1) or (nums[l] > r) or (nums[l] == nums[nums[l] - 1]):
                r -= 1
                nums[l] = nums[r]
            else:
                temp = nums[l]
                nums[l] = nums[temp - 1]
                nums[temp - 1] = temp
        return l + 1
        
# @lc code=end

