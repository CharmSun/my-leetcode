#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List

## 双指针，用来划分区域，将整个数组划分为三段
## 遍历数组，0放在前面，2放在后面
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        low, high = -1, len(nums)
        # [0, low]: 0, [high, len(nums) - 1]: 2
        while i < high:
            if nums[i] == 0:
                low += 1
                nums[low], nums[i] = nums[i], nums[low]
                i += 1
            elif nums[i] == 2:
                high -= 1
                nums[high], nums[i] = nums[i], nums[high]
            else:
                i += 1

nums = [1,0,2]
Solution().sortColors(nums)
print(nums)
        
# @lc code=end

