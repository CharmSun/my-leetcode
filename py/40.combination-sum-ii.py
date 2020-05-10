#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List

## 先排序，再使用回溯，每个元素只使用一次
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def backtrack(res, total, remains):
            if total == target and res not in output:
                output.append(res)
            elif total > target:
                return
            for i, num in enumerate(remains):
                backtrack(res+[num], total + num, remains[i+1:])
            return

        candidates.sort()
        backtrack([], 0, candidates)
        return output

candidates = [2,5,2,1,2]
target = 5
print(Solution().combinationSum2(candidates, target))
        
# @lc code=end

