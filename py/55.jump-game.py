#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List

## end 表示某个位置下，所能到的最远位置，不断更新
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0
        i = 0
        while i <= end and i < len(nums):
            end = max(end, i + nums[i])
            i += 1
        if end >= len(nums) - 1:
            return True
        return False

input = [3,2,1,0,4]
print(Solution().canJump(input))  
        
# @lc code=end

