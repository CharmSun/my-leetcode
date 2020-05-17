#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List

## 对等二进制数0 ~ 2**n，1代表选中，0代表不选中
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        for i in range(2**n):
            ans = []
            for j in range(n):
                if i >> j & 1:
                    ans.append(nums[j])
            output.append(ans)
        return output

nums = [1,2,3]    
print(Solution().subsets(nums))
        
# @lc code=end

