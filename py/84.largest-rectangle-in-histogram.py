#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from typing import List

## 用递增栈来维持一个递增序列，栈中保存的是当前元素的索引。
## 如果当前值比栈顶元素小，那么栈中元素就需要弹出，直到栈为空或者栈顶元素小于当前元素
## 当元素弹出时，以它为最低高度的最大矩阵面积就很好求出来了
## heights 末尾补一个0，能保证最后所有元素都弹出
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        heights.append(0)
        for i,num in enumerate(heights):
            while stack and heights[stack[-1]] >= num:
                cur = stack.pop()
                length = i - stack[-1] - 1 if stack else i
                area = heights[cur] * length
                res = max(res, area)
            stack.append(i)
        return res

nums = [2,1,5,6,2,3]
print(Solution().largestRectangleArea(nums))  
        
# @lc code=end

