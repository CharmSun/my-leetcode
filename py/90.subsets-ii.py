#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
from typing import List

## 先排序，然后回溯，遇到重复的就剪枝
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        ans = []
        output.append(ans)
        if not nums:
            return output
        nums.sort()
        self.dfs(nums, 0, ans, output)
        return output
    
    def dfs(self, nums, pos, ans, output):
        for i in range(pos, len(nums)):
            if i > pos and nums[i] == nums[i-1]:
                continue
            ans.append(nums[i])
            output.append(ans.copy())
            self.dfs(nums, i+1, ans, output)
            ans.pop()

nums = [1,2,2]
print(Solution().subsetsWithDup(nums))

# @lc code=end

