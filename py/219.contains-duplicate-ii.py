#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
from typing import List

class Solution:
    # hash
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in dict:
                dis = i - dict[num]
                if dis <= k:
                    return True
            dict[num] = i
        return False
        
# @lc code=end

