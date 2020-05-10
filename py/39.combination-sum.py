#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List

## 回溯：可重复取，注意值的拷贝
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        if not candidates:
            return output
        def helper(ans, sum, nums):
            if sum == target:
                output.append(ans)
            elif sum < target:
                for i,num in enumerate(nums):
                    helper(ans+[num], sum + num, nums[i:])
        helper([], 0, candidates)
        return output

candidates = [2,3,6,7]
print(Solution().combinationSum(candidates, 7))
        
# @lc code=end

