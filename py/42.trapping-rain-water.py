#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List

## 双指针：左侧较低，移动左侧；右侧较低，移动右侧
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = right_max = 0
        ans = 0
        while left < right :
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1 
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans

test_input = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(test_input))
# @lc code=end

