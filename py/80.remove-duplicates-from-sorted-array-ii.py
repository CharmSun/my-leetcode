#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
from typing import List

## j遍历数组，i指向已排好的下一个位置，注意nums是已排好的数组
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if i < 2 or nums[j] > nums[i-2]:
                nums[i] = nums[j]
                i += 1
        return i

nums = [1,2,2]
print(Solution().removeDuplicates(nums))
print(nums)
        
# @lc code=end

