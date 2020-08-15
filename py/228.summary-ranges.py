#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [str(nums[0])]
        res = []
        start = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                end = i -1
                if start != end:
                    res.append(str(nums[start])+'->'+str(nums[end]))
                else:
                    res.append(str(nums[start]))
                start = i
        if start != n -1:
            res.append(str(nums[start])+'->'+str(nums[n-1]))
        else:
            res.append(str(nums[start]))
        return res

nums = [0,2,3,4,6,8,9]
print(Solution().summaryRanges(nums))
        

# @lc code=end

