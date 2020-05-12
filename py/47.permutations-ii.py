#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List

## 1、先排序
## 2、用对应数组标记元素是否使用过
## 3、减枝和之前重复的元素
## 4、添加过得元素得标记，用完后得去掉该元素和恢复标记
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        if not nums:
            return result
        nums.sort()
        used = [False] * len(nums)
        def helper(tmpList: List[int]):
            if len(tmpList) == len(nums):
                result.append(tmpList.copy())
                return
            for i,_ in enumerate(nums):
                if i != 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                if used[i]:
                    continue
                tmpList.append(nums[i])
                used[i] = True
                helper(tmpList)
                tmpList.pop()
                used[i] = False
        
        helper([])
        return result

nums = [2,2,1,1]
print(Solution().permuteUnique(nums))
        
# @lc code=end

