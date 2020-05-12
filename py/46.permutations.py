#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List

## 回溯：两两交换，包括和自己
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        def helper(i: int) -> int:
            if i == n:
                res.append(nums.copy())
                return
            for k in range(i, n):
                nums[i], nums[k] = nums[k], nums[i]
                helper(i + 1)
                nums[k], nums[i] = nums[i], nums[k]

        helper(0)
        return res

input = [1,2,3]
print(Solution().permute(input))
        
# @lc code=end

