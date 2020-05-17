#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
from typing import List

## 有左边的数来比较中间的数，如果相等，则剔除左边的数
## 如果中间的数大于最左边的数，则左半段是有序的，若中间数小于于最左边数，则左半段是有序的
## （也可以用最右边的数来比较中间数）
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return True
            if nums[left] == nums[mid]:
                left += 1
            elif nums[left] < nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

nums = [1,3,1,1,1]
target = 3
print(Solution().search(nums, target))
        
# @lc code=end

