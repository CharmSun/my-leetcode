#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List

## curMax表示当前最大，curMin表示当前最小(再遇到负数，负负得正)，maxres表示全局最大
## curMax(x + 1) = Math.max( curMax(x)*A[x] , curMin(x)*A[x] , A[x] )
## curMin(x + 1) = Math.min( curMax(x)*A[x] , curMin(x)*A[x], A[x])
## maxres = Math.max (maxres, curMax)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = nums[0]
        resMax = curMax
        for i in range(1, len(nums)):
            tmp1 = curMax * nums[i]
            tmp2 = curMin * nums[i]
            curMax = max(tmp1, tmp2, nums[i])
            curMin = min(tmp1, tmp2, nums[i])
            resMax = max(resMax, curMax)
        return resMax
        
# @lc code=end

