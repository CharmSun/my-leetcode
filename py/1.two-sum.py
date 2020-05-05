#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List

# hash一趟遍历
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length < 2:
            return None
        dict = {}
        for i in range(length):
            complement = target - nums[i]
            if(complement in dict):
                return [dict[complement], i]
            dict[nums[i]] = i
        return None
        
# @lc code=end

