#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
from typing import List

## 1、倒着找到第一个递增值 first
## 2、对递增值之后的递减值各位互换，形成最小递增的数
## 3、在递增数中找到刚好大于 first 的数，与 first 互换
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        first = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                first = i - 1
                break
        i = first + 1
        j = len(nums) - 1
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1
        if first > -1:
            nextMinIdx = first + 1
            while nums[nextMinIdx] <= nums[first]:
                nextMinIdx += 1
            nextMin = nums[nextMinIdx]
            nums[nextMinIdx] = nums[first]
            nums[first] = nextMin

nums = [1,2,4,3]
Solution().nextPermutation(nums)
print(nums)        
# @lc code=end

