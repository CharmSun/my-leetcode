#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
from typing import List

class Solution:
    ## 分桶
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        buckets = {}
        w = t + 1
        for i in range(len(nums)):
            m = nums[i] // w
            if m in buckets:
                return True
            if m-1 in buckets and abs(buckets[m-1] - nums[i]) <= t:
                return True
            if m+1 in buckets and abs(buckets[m+1] - nums[i]) <= t:
                return True
            buckets[m] = nums[i]
            if i >= k: 
                del buckets[nums[i - k] // w]
        return False
        
# @lc code=end

