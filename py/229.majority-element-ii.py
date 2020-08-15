#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        if not nums:
            return res
        candidate = [0] * 2
        count = [0] * 2
        for num in nums:
            if num == candidate[0]:
                count[0] += 1
            elif num == candidate[1]:
                count[1] += 1
            elif count[0] == 0:
                candidate[0] = num
                count[0] = 1
            elif count[1] == 0:
                candidate[1] = num
                count[1] = 1
            else:
                count[0] -= 1
                count[1] -= 1
        count[0] = 0
        count[1] = 0
        for num in nums:
            if num == candidate[0]:
                count[0] += 1
            elif num == candidate[1]:
                count[1] += 1
        if count[0] > len(nums) // 3:
            res.append(candidate[0])
        if candidate[1] != candidate[0] and count[1] > len(nums) // 3:
            res.append(candidate[1])
        return res

nums = [1,2,2,3,2,1,1,3]
print(Solution().majorityElement(nums))       
        
# @lc code=end

