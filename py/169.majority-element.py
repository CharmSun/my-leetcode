#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List

## 摩尔投票法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        return candidate

input = [2,2,1,1,1,2,2]
print(Solution().majorityElement(input))
        
# @lc code=end

