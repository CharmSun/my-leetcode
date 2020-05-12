#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from typing import List

## steps: 所需要的步数
## maxReach: 当前位置以前，所能到的最远位置
## end: 某个steps步数下，所能到的最远位置

class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        maxReach = 0
        end = 0
        for i in range(len(nums)):
            if i > end:
                steps += 1
                end = maxReach
            maxReach = max(maxReach, i + nums[i])
        return steps

input = [2,3,1,1,4]
print(Solution().jump(input))
        
# @lc code=end

