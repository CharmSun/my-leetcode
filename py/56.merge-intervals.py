#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List

## 将数组第一个元素排序，将当前间隔对，与后续的间隔一一比较，能合并的合并，直到遇到不能合并的
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = sorted(intervals, key = lambda arr: arr[0])
        res = []
        i = 0
        while i < len(l):
            cur = l[i]
            j = i + 1
            while j < len(l) and l[j][0] <= cur[1]:
                cur[1] = max(cur[1], l[j][1])
                j += 1 
            res.append(cur)    
            i = j
        return res

input = [[1,4],[4,5]]
print(Solution().merge(input))
        
# @lc code=end

